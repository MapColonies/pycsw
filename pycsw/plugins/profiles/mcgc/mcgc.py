import os
from typing import NoReturn
import constants
from pycsw.core.etree import etree
from pycsw.core import config, util
from pycsw.ogc.csw.csw2 import write_boundingbox
from pycsw.plugins.profiles import profile
from pycsw.plugins.profiles.base_profile.models.models import Queryable


class MCGC(profile.Profile):
    ''' MCGC class '''
    
    def __init__(self, model, namespaces, context):

        prefix = 'mc'
        typename = '%s:MCGCRecord' % (prefix)

        self.context = context

        self.namespaces = {
            'mc': 'http://schema.mapcolonies.com',
            'mcgc': 'http://schema.mapcolonies.com',
        }

        self.repository = {
            typename: {
                'outputschema': self.namespaces[prefix],
                'queryables': {
                    'MGCGQueryables': {
                        'mcgc:accessRights': {'dbcol': self.context.md_core_model['mappings']['pycsw:Classification'], 'xpath': 'dct:accessRights'},
                        'mcgc:created': {'dbcol': self.context.md_core_model['mappings']['pycsw:CreationDate'], 'xpath': 'dct:created'},
                        'mcgc:creator': {'dbcol': self.context.md_core_model['mappings']['pycsw:Creator'], 'xpath': 'dc:creator'},
                        'mcgc:crs': {'dbcol': self.context.md_core_model['mappings']['pycsw:CRS'], 'xpath':'dct:spatial'},
                        'mcgc:references': {'dbcol': self.context.md_core_model['mappings']['pycsw:Links'], 'xpath':'dct:references'},
                        'mcgc:abstract': {'dbcol': self.context.md_core_model['mappings']['pycsw:Abstract'], 'xpath':'dct:abstract'},
                        'mcgc:anyText': {'dbcol': self.context.md_core_model['mappings']['pycsw:AnyText']},
                        'mcgc:relation': {'dbcol': self.context.md_core_model['mappings']['pycsw:Relation'], 'xpath':'dc:relation'},
                        'mcgc:boundingBox': {'dbcol': self.context.md_core_model['mappings']['pycsw:BoundingBox'], 'xpath':'ows:BoundingBox'},
                        'mcgc:format': {'dbcol': self.context.md_core_model['mappings']['pycsw:Format'], 'xpath':'dc:format'},
                        'mcgc:identifier': Queryable(self.context.md_core_model['mappings']['pycsw:Identifier'],'dc:identifier'),
                        'mcgc:dateModified': {'dbcol': self.context.md_core_model['mappings']['pycsw:Modified'], 'xpath': 'dct:modified'},
                        'mcgc:subject': {'dbcol': self.context.md_core_model['mappings']['pycsw:Keywords'], 'xpath': 'dc:subject'},
                        'mcgc:temporalExtentStart': {'dbcol': self.context.md_core_model['mappings']['pycsw:TempExtent_begin'], 'xpath': 'TemporalExtent/begin'},
                        'mcgc:temporalExtentEnd': {'dbcol': self.context.md_core_model['mappings']['pycsw:TempExtent_end'], 'xpath': 'TemporalExtent/end'},
                        'mcgc:title': {'dbcol': self.context.md_core_model['mappings']['pycsw:Title'], 'xpath': 'dc:title'},
                        'mcgc:type': {'dbcol': self.context.md_core_model['mappings']['pycsw:Type'], 'xpath': 'dc:type'},
                        'mcgc:region': {'dbcol': 'region', 'xpath': 'mc:region'},
                        'mcgc:sensorName': {'dbcol': 'sensor_name', 'xpath': 'mc:sensor/name'},
                        'mcgc:sensorType': {'dbcol': 'sensor_type', 'xpath': 'mc:sensor/type'},
                        'mcgc:version': {'dbcol': 'version', 'xpath': 'mc:version'}
                    }
                },
                'mappings': {
                    'csw:Record': {}
                }
            }
        }

        profile.Profile.__init__(self,
                                 name='mcgc',
                                 version='1.0.0',
                                 title='Map Colonies General profile of CSW',
                                 url='https://github.com/MapColonies',
                                 namespace=self.namespaces[prefix],
                                 typename=typename,
                                 outputschema=self.namespaces[prefix],
                                 prefixes=[prefix],
                                 model=model,
                                 core_namespaces=namespaces,
                                 added_namespaces=self.namespaces,
                                 repository=self.repository[typename])

    def extend_core(self, model, namespaces, config):
        ''' Extend core configuration '''
        return None

    def check_parameters(self, kvp):
        '''Check for Language parameter in GetCapabilities request'''
        return None

    def get_extendedcapabilities(self):
        ''' Add child to ows:OperationsMetadata Element '''
        return None

    def get_schemacomponents(self):
        ''' Return schema components as lxml.etree.Element list '''

        node = etree.Element(
            util.nspath_eval('csw:SchemaComponent', self.context.namespaces),
            schemaLanguage='XMLSCHEMA', targetNamespace=self.namespace)

        schema_file = os.path.join(self.context.pycsw_home, 'plugins',
                                   'profiles', 'mcgc', 'schemas', 'mc-record.xsd')

        schema = etree.parse(schema_file, self.context.parser).getroot()

        node.append(schema)

        return [node]

    def check_getdomain(self, kvp):
        '''Perform extra profile specific checks in the GetDomain request'''
        return None

    def write_record(self, result, esn, outputschema, queryables):
        ''' Return csw:SearchResults child as lxml.etree.Element '''

        specialPycswKeys = [constants.PYCSW_BOUNDING_BOX,constants.PYCSW_KEYWORDS,constants.PYCSW_LINKS]
        
        specialDbcols = [queryables[x] for x in specialPycswKeys]

        typename = util.getqattr(
            result, self.context.md_core_model['mappings'][constants.PYCSW_TYPENAME])

        if esn == 'full' and typename == self.typename:
            # dump record as is and exit
            return etree.fromstring(util.getqattr(result, queryables[constants.PYCSW_XML]), self.context.parser)

        if esn == 'full':
            dbcol2xpath = _get_dbcol_to_xpath_dict(self.repository['queryables'])

            record = etree.Element(util.nspath_eval(
                self.typename, self.namespaces))

            for dbcol, value in vars(result).items():
                if not dbcol.startswith('_') and value is not None:
                    elementName = dbcol2xpath.get(dbcol, None)
                    if elementName is not None:
                        if dbcol not in specialDbcols:   
                            _build_xpath(record, elementName, self.context.namespaces, value)

                        elif dbcol == queryables[constants.PYCSW_KEYWORDS]:
                            for keyword in value.split(','):
                                etree.SubElement(record, util.nspath_eval(elementName, self.context.namespaces)).text = keyword

                        elif dbcol == queryables[constants.PYCSW_LINKS]:
                            for link in value.split('^'):
                                linkComponents = link.split(',')
                                scheme = linkComponents[2]
                                uri = linkComponents[-1]
                                etree.SubElement(record, util.nspath_eval(elementName, self.context.namespaces), scheme=scheme).text = uri
                        
                        elif dbcol == queryables[constants.PYCSW_BOUNDING_BOX]:
                            bbox = write_boundingbox(value, self.context.namespaces)
                            record.append(bbox)

            return record
    
def _get_dbcol_to_xpath_dict(queryables):  
    flatQueryables = {}

    for qblsCategory in queryables.values():
        flatQueryables.update(qblsCategory)

    dbcol2xpath = {}

    for qbl in flatQueryables.values():
        if type(qbl) is Queryable:
            dbcol = qbl.dbcol
            xpath = qbl.xpath
        else:
            dbcol = qbl.get('dbcol', None)
            xpath = qbl.get('xpath', None)
        if xpath != None and dbcol != None:
            dbcol2xpath[dbcol] = xpath

    return dbcol2xpath

def _build_xpath(node, path, namespaces, text):
    components = path.split("/")
    if util.nspath_eval(components[0],namespaces) == node.tag:
        components.pop(0)
    while components:
        # take in account positional  indexes in the form /path/para[3] or /path/para[location()=3]
        if "[" in components[0]:
            component, trail = components[0].split("[",1)
            target_index = int(trail.split("=")[-1].strip("]"))
        else:
            component = components[0]
            target_index = 0

        components.pop(0)
        found_index = -1
        for child in node.getchildren():
            if child.tag == util.nspath_eval(component,namespaces):
                found_index += 1
                if found_index == target_index:
                    node = child
                    break

        if found_index < target_index:
            new_node = None

            for i in range(target_index - found_index):
                new_node = etree.Element(util.nspath_eval(component,namespaces))
                node.append(new_node)

            node = new_node
    
    node.text = text
    return node
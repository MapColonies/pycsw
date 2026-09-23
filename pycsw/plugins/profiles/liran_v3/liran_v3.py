from pycsw.plugins.profiles.base_profile.models.models import ProfileRepository, Queryable, TypenameModel
from pycsw.plugins.profiles.base_profile import base_profile


class LiranV3(base_profile.base_profile):
    '''POC profile: two JSONB columns
    jsonb_data:  {"parameters": {"isPublic": "false", "value": 15}}
    jsonb_data2: {"parameters": {"what": "false", "value": 12}}
    '''

    def __init__(self, model, namespaces, context):

        prefix = 'liran'
        typename = '%s:LiranV3Record' % prefix
        main_namespace = 'http://schema.mapcolonies.com/poc/v3'

        schemas_pathes = [['plugins', 'profiles', 'liran_v3', 'schemas', 'liran_v3-record.xsd']]

        added_namespaces = {
            prefix: main_namespace
        }

        profileRepository: ProfileRepository = {
            typename: TypenameModel(
                added_namespaces[prefix],
                {
                    'LiranV3Queryables': {
                        'liran:id': Queryable(context.md_core_model['mappings']['pycsw:Identifier'], 'liran:id'),
                        'liran:title': Queryable(context.md_core_model['mappings']['pycsw:Title'], 'liran:title'),
                        'liran:description': Queryable(context.md_core_model['mappings']['pycsw:Abstract'], 'liran:description'),
                        'liran:type': Queryable(context.md_core_model['mappings']['pycsw:Type'], 'liran:type'),
                        'liran:links': Queryable(context.md_core_model['mappings']['pycsw:Links'], 'liran:links'),
                        'liran:boundingBox': Queryable(context.md_core_model['mappings']['pycsw:BoundingBox'], 'liran:boundingBox'),
                        'liran:keywords': Queryable(context.md_core_model['mappings']['pycsw:Keywords'], 'liran:keywords'),
                        'liran:insertDate': Queryable(context.md_core_model['mappings']['pycsw:InsertDate'], 'liran:insertDate'),
                        # JSONB column 2: {"parameters": {"what": "false", "value": 12}}
                        'liran:what': Queryable(context.md_core_model['mappings']['pycsw:What'], 'liran:what'),
                        'liran:value': Queryable(context.md_core_model['mappings']['pycsw:JsonValue2'], 'liran:value'),
                    }
                })
        }

        super().__init__(name='liran_v3',
                         version='1.0.0',
                         title='MapColonies POC v3 - two JSONB columns',
                         url='https://github.com/MapColonies',
                         typename=typename,
                         model=model,
                         core_namespaces=namespaces,
                         added_namespaces=added_namespaces,
                         repositories=profileRepository,
                         schemas_paths=schemas_pathes,
                         context=context,
                         prefix=prefix,
                         main_namespace=main_namespace
                         )

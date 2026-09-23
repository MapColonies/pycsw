from pycsw.plugins.profiles.base_profile.models.models import ProfileRepository, Queryable, TypenameModel
from pycsw.plugins.profiles.base_profile import base_profile


class LiranV2(base_profile.base_profile):
    '''POC profile: one JSONB column - {"parameters": {"isPublic": "false", "value": 15}}'''

    def __init__(self, model, namespaces, context):

        prefix = 'liran'
        typename = '%s:LiranV2Record' % prefix
        main_namespace = 'http://schema.mapcolonies.com/poc/v2'

        schemas_pathes = [['plugins', 'profiles', 'liran_v2', 'schemas', 'liran_v2-record.xsd']]

        added_namespaces = {
            prefix: main_namespace
        }

        profileRepository: ProfileRepository = {
            typename: TypenameModel(
                added_namespaces[prefix],
                {
                    'LiranV2Queryables': {
                        'liran:id': Queryable(context.md_core_model['mappings']['pycsw:Identifier'], 'liran:id'),
                        'liran:title': Queryable(context.md_core_model['mappings']['pycsw:Title'], 'liran:title'),
                        'liran:description': Queryable(context.md_core_model['mappings']['pycsw:Abstract'], 'liran:description'),
                        'liran:type': Queryable(context.md_core_model['mappings']['pycsw:Type'], 'liran:type'),
                        'liran:links': Queryable(context.md_core_model['mappings']['pycsw:Links'], 'liran:links'),
                        'liran:boundingBox': Queryable(context.md_core_model['mappings']['pycsw:BoundingBox'], 'liran:boundingBox'),
                        'liran:keywords': Queryable(context.md_core_model['mappings']['pycsw:Keywords'], 'liran:keywords'),
                        'liran:insertDate': Queryable(context.md_core_model['mappings']['pycsw:InsertDate'], 'liran:insertDate'),
                        # JSONB column 1: {"parameters": {"isPublic": "false", "value": 15}}
                        'liran:isPublic': Queryable(context.md_core_model['mappings']['pycsw:IsPublic'], 'liran:isPublic'),
                        'liran:value': Queryable(context.md_core_model['mappings']['pycsw:JsonValue1'], 'liran:value'),
                    }
                })
        }

        super().__init__(name='liran_v2',
                         version='1.0.0',
                         title='MapColonies POC v2 - one JSONB column',
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

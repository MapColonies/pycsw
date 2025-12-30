MD_CORE_MODEL = {
    'typename': 'pycsw:CoreMetadata',
    'outputschema': 'http://pycsw.org/metadata',
    'mappings': {
        # Needed for PYCSW
        'pycsw:Identifier': 'identifier',
        'pycsw:Typename': 'typename', #TODO: unused in profile
        'pycsw:Schema': 'schema', #TODO: unused in profile
        'pycsw:MdSource': 'mdsource', #TODO: unused in profile
        'pycsw:InsertDate': 'insert_date_utc',
        'pycsw:XML': 'xml', #TODO: unused in profile
        'pycsw:AnyText': 'anytext', #TODO: unused in profile
        'pycsw:BoundingBox': 'wkt_geometry', #TODO: wkt is not BoundingBox ???
        'pycsw:Links': 'links',
        'pycsw:Keywords': 'keywords',

        # Common profile fields
        'pycsw:Type': 'type',
        'pycsw:Classification': 'classification',
        'pycsw:AccessConstraints': 'classification', #TODO: unused in profile
        'pycsw:ProductId': 'product_id',
        'pycsw:Title': 'product_name',
        'pycsw:AlternateTitle': 'product_name', #TODO: unused in profile
        'pycsw:ProductVersion': 'product_version',
        'pycsw:ProductType': 'product_type',
        'pycsw:Abstract': 'description',
        'pycsw:CRS': 'srs_id',
        'pycsw:CRSName': 'srs_name',
        'pycsw:Creator': 'producer_name',
        'pycsw:Publisher': 'producer_name', #TODO: unused in profile
        'pycsw:Contributor': 'producer_name', #TODO: unused in profile
        'pycsw:CreationDate': 'creation_date_utc', #TODO: unused in profile
        'pycsw:Date': 'creation_date_utc', #TODO: unused in profile
        'pycsw:Format': 'type', #TODO: unused in profile
        'pycsw:Modified': 'update_date_utc', #TODO: unused in profile
        'pycsw:updateDateUTC': 'update_date_utc',
        'pycsw:IngestionDateUTC': 'ingestion_date_utc', #TODO: unused in profile
        'pycsw:TempExtent_begin': 'acquisition_time_begin_utc',
        'pycsw:TempExtent_end': 'acquisition_time_end_utc',
        'pycsw:maxResolutionDegree': 'max_resolution_degree',
        'pycsw:minResolutionDegree': 'min_resolution_degree',
        'pycsw:maxResolutionMeter': 'max_resolution_meter',
        'pycsw:minResolutionMeter': 'min_resolution_meter',
        'pycsw:maxHorizontalAccuracyCEP90': 'max_horizontal_accuracy_cep_90',
        'pycsw:minHorizontalAccuracyCEP90': 'min_horizontal_accuracy_cep_90',
        'pycsw:maxAbsoluteAccuracyLEP90': 'max_absolute_accuracy_lep_90',
        'pycsw:minAbsoluteAccuracyLEP90': 'min_absolute_accuracy_lep_90',
        'pycsw:maxRelativeAccuracyLEP90': 'max_relative_accuracy_lep_90',
        'pycsw:minRelativeAccuracyLEP90': 'min_relative_accuracy_lep_90',
        'pycsw:sensorType': 'sensors',
        'pycsw:region': 'region',
        'pycsw:footprint': 'footprint_geojson',
        'pycsw:Source': 'product_name', #TODO: not used in profile
        'pycsw:noDataValue': 'no_data_value',
        'pycsw:areaOrPoint': 'area_or_point'
        'pycsw:dataType': 'data_type',
        'pycsw:displayPath': 'display_path', #TODO: db field needed?
        'pycsw:geoidModel': 'geoid_model',
        # 'pycsw:Relation': '',
        # 'pycsw:Language': '',
        # 'pycsw:TopicCategory': '',

        'pycsw:productBBox':'product_bbox',
        'pycsw:productStatus': 'product_status',
    }
}

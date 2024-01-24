MD_CORE_MODEL = {
    'typename': 'pycsw:CoreMetadata',
    'outputschema': 'http://pycsw.org/metadata',
    'mappings': {
        # Needed for PYCSW
        'pycsw:Identifier': 'identifier',
        'pycsw:Typename': 'typename',
        'pycsw:Schema': 'schema',
        'pycsw:MdSource': 'mdsource',
        'pycsw:InsertDate': 'insert_date',
        'pycsw:XML': 'xml',
        'pycsw:AnyText': 'anytext',
        'pycsw:BoundingBox': 'wkt_geometry',
        'pycsw:Links': 'links',
        'pycsw:Keywords': 'keywords',

        # MUST BE DEFINED IN PROFILE
        'pycsw:Type': 'type',
        'pycsw:Title': 'product_name',
        'pycsw:Abstract': 'description',
        'pycsw:AlternateTitle': 'product_name',
        'pycsw:AccessConstraints': 'classification',
        'pycsw:Creator': 'producer_name',
        'pycsw:CRS': 'srs',
        'pycsw:Publisher': 'producer_name',
        'pycsw:Contributor': 'producer_name',
        'pycsw:CreationDate': 'insert_date',
        'pycsw:Date': 'insert_date',
        'pycsw:Format': 'typename',
        'pycsw:Modified': 'update_date',
        'pycsw:Source': 'product_name',
        'pycsw:Relation': '',
        'pycsw:Language': '',
        'pycsw:TopicCategory': '',

        # DEM profile fields
        'pycsw:imagingTimeEndUTC': 'source_end_date',
        'pycsw:resolutionMeter': 'resolution_meter',
        'pycsw:imagingSortieAccuracyCEP90': 'imaging_sortie_accuracy_cep_90',
        'pycsw:heightRangeFrom': 'height_range_from',
        'pycsw:heightRangeTo': 'height_range_to',
        'pycsw:productStatus': 'product_status',
        'pycsw:hasTerrain': 'has_terrain',
        'pycsw:geographicArea': 'geographic_area',
        'pycsw:undulationModel': 'undulation_model',
        'pycsw:dataType': 'data_type',
        'pycsw:noDataValue': 'no_data_value',
        'pycsw:Classification': 'classification',
        'pycsw:ProductId': 'product_id',
        'pycsw:ProductType': 'product_type',
        'pycsw:CRSName': 'srs_name',
        'pycsw:UpdateDate': 'update_date',
        'pycsw:TempExtent_begin': 'source_start_date',
        'pycsw:TempExtent_end': 'source_end_date',
        'pycsw:absoluteAccuracyLEP90': 'absolute_accuracy_lep_90',
        'pycsw:relativeAccuracyLEP90': 'relative_accuracy_lep_90',
        'pycsw:resolutionDeg': 'resolution_degree',
        'pycsw:sensorType': 'sensor_type',
        'pycsw:Region': 'region',
        'pycsw:footprint': 'footprint_geojson',
        'pycsw:layerPolygonParts': 'layer_polygon_parts',
        'pycsw:productBBox':'product_bbox',
    }
}
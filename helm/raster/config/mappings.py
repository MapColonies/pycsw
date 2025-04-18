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

        # Common profile fields
        'pycsw:Type': 'type',
        'pycsw:Classification': 'classification',
        'pycsw:AccessConstraints': 'classification',
        'pycsw:ProductId': 'product_id',
        'pycsw:Title': 'product_name',
        'pycsw:AlternateTitle': 'product_name',
        'pycsw:ProductVersion': 'product_version',
        'pycsw:ProductType': 'product_type',
        'pycsw:productSubType': 'product_sub_type',
        'pycsw:Abstract': 'description',
        'pycsw:CRS': 'srs',
        'pycsw:CRSName': 'srs_name',
        'pycsw:Creator': 'producer_name',
        'pycsw:Publisher': 'producer_name',
        'pycsw:Contributor': 'producer_name',
        'pycsw:CreationDate': 'creation_date_utc',
        'pycsw:Date': 'creation_date_utc',
        'pycsw:Format': 'type',
        'pycsw:Modified': 'update_date_utc',
        'pycsw:UpdateDate': 'update_date_utc',
        'pycsw:IngestionDate': 'ingestion_date',
        'pycsw:TempExtent_begin': 'imaging_time_begin_utc',
        'pycsw:TempExtent_end': 'imaging_time_end_utc',
        'pycsw:Resolution': 'max_resolution_deg',
        'pycsw:minResolutionDeg': 'min_resolution_deg',
        'pycsw:horizontalAccuracyCE90': 'min_horizontal_accuracy_ce_90',
        'pycsw:maxHorizontalAccuracyCE90': 'max_horizontal_accuracy_ce_90',
        'pycsw:sensorType': 'sensors',
        'pycsw:Region': 'region',
        'pycsw:footprint': 'footprint_geojson',
        'pycsw:Source': 'product_name',
        'pycsw:transparency': 'transparency',
        'pycsw:MimeType': 'tile_mime_format',
        
        'pycsw:Relation': '',
        'pycsw:Language': '',
        'pycsw:TopicCategory': '',

        'pycsw:maxResolutionMeter': 'max_resolution_meter',
        'pycsw:minResolutionMeter': 'min_resolution_meter',
        'pycsw:productBBox':'product_bbox',
        'pycsw:productStatus': 'product_status',

        # Added for mc-raster 
        'pycsw:Rms': 'rms',
        'pycsw:Scale': 'scale',
    }
}

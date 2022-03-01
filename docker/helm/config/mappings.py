MD_CORE_MODEL = {
    'typename': 'pycsw:CoreMetadata',
    'outputschema': 'http://pycsw.org/metadata',
    'mappings': {

        # Update of Nati
        # Needed fot PYCSW

        'pycsw:Links': 'links',
        'pycsw:Type': 'type',
        'pycsw:Typename': 'typename',
        'pycsw:Schema': 'schema',
        'pycsw:MDSource': 'mdsource',
        'pycsw:XML': 'xml',
        'pycsw:AnyText': 'anytext',
        'pycsw:InsertDate': 'insert_date',
        'pycsw:BoundingBox': 'wkt_geometry',
        'pycsw:Keywords': 'keywords',


        # Not in xml

        'pycsw:Identifier': 'identifier',
        'pycsw:Title': 'title',
        'pycsw:AlternateTitle': 'title',
        'pycsw:Creator': 'producer_name',
        'pycsw:Abstract': 'description',
        'pycsw:Publisher': 'producer_name',
        'pycsw:Contributor': 'producer_name',
        'pycsw:Modified': 'update_date',
        'pycsw:Date': 'creation_date',
        'pycsw:Format': 'type',
        'pycsw:Source': 'product_name',
        'pycsw:AccessConstraints': 'classification',
        'pycsw:CRS': 'srs',
        'pycsw:Relation': '',
        'pycsw:Language': '',
        'pycsw:Keywords': '',
        'pycsw:TopicCategory': '',



        # Profile 3D fields
        'pycsw:productId': 'product_id',
        'pycsw:title': 'product_name',
        'pycsw:productVersion': 'product_version',
        'pycsw:productType': 'product_type',
        'pycsw:abstract': 'description',
        'pycsw:creationDate': 'creation_date',
        'pycsw:tempExtentBegin': 'source_start_date',
        'pycsw:tempExtentEnd': 'source_end_date',
        'pycsw:minResolution': 'min_resolution',
        'pycsw:maxResolution': 'max_resolution',
        'pycsw:nominalResolution': 'nominal_resolution',
        'pycsw:horizontalAccuracyCE90': 'horizontal_accuracy_ce_90',
        'pycsw:accuracyLE90': 'accuracy_le_90',
        'pycsw:accuracySE90': 'accuracy_se_90',
        'pycsw:relativeAccuracyLE90': 'relative_accuracy_le_90',
        'pycsw:visualAccuracy': 'visual_accuracy',
        'pycsw:sensorType': 'sensor_type',
        'pycsw:footprint': 'footprint',
        'pycsw:heightRangeFrom': 'height_range_from',
        'pycsw:heightRangeTo': 'height_range_to',
        'pycsw:CRS': 'srs',
        'pycsw:CRSName': 'srs_name',
        'pycsw:CRSOrigin': 'srs_origin',
        'pycsw:region': 'region',
        'pycsw:classification': 'classification',
        'pycsw:compartmentalization': 'compartmentalization',
        'pycsw:productionSystem': 'production_system',
        'pycsw:productionSystemVersion': 'production_system_version',
        'pycsw:creator': 'producer_name',
        'pycsw:productionMethod': 'production_method',
        'pycsw:minFlightAlt': 'min_flight_alt',
        'pycsw:maxFlightAlt': 'max_flight_alt',
        'pycsw:geographicArea': 'geographic_area',
        'pycsw:productBBox': 'product_bbox'
    }
}

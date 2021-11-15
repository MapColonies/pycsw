# -*- coding: utf-8 -*-
# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2015 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

# sample mappings.py
#
# use this file to bind to an existing alternate metadata database model
#
# steps:
# - update the 'mappings' dict to the column names of your existing database
# - set repository.mappings to the location of this file
# - if new fields are needed add them with the 'pycsw' prefix (to avoid collision with actual profile queryables)

MD_CORE_MODEL = {
    'typename': 'pycsw:CoreMetadata',
    'outputschema': 'http://pycsw.org/metadata',
    'mappings': {

        # Update of Nati
        # Needed fot PYCSW

        'pycsw:links': 'links',
        'pycsw:type': 'type',
        'pycsw:typeName': 'typename',
        'pycsw:schema': 'schema',
        'pycsw:MDSource': 'mdsource',
        'pycsw:XML': 'xml',
        'pycsw:anyText': 'anytext',
        'pycsw:insertDate': 'insert_date',
        'pycsw:boundingBox': 'wkt_geometry',
        'pycsw:keywords': 'keywords',


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

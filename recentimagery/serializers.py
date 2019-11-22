"""Serializers"""


def serialize_recent_data(analysis, type_str):
    """Convert output of images to json"""
    output = []
    for e in range(0, len(analysis)):
        temp_output = {
            'attributes': {
                'instrument': analysis[e].get('spacecraft', None),
                'source': analysis[e].get('source', None),
                'cloud_score': analysis[e].get('cloud_score', None),
                'date_time': analysis[e].get('date', None),
                'tile_url': analysis[e].get('tile_url', None),
                'thumbnail_url': analysis[e].get('thumb_url', None),
                'bbox': analysis[e].get('bbox', None)
            }
        }
        output.append(temp_output)
    return {
        'tiles': output,
        'id': None,
        'type': type_str
    }


def serialize_recent_url(analysis, type_str):
    """Convert output of images to json"""
    tmp_output = []
    output = {}
    if type_str == 'recentimages-thumbs':
        output['id'] = None
        output['type'] = type_str
        for e in range(len(analysis)):
            temp_obj = {
                'source': analysis[e].get('source', None),
                'thumbnail_url': analysis[e].get('thumb_url', None)
            }
            tmp_output.append(temp_obj)
        output['attributes'] = tmp_output
    elif type_str == 'recentimages-tiles':
        output['id'] = None
        output['type'] = type_str
        for e in range(len(analysis)):
            temp_obj = {
                'source_id': analysis[e].get('source', None),
                'tile_url': analysis[e].get('tile_url', None)
            }
            tmp_output.append(temp_obj)
        output['attributes'] = tmp_output
    return output

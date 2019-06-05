from adapterearthengine.utils.files import BASE_DIR

settings={
    'logging': {
        'level': 'DEBUG'
    },
    'service': {
        'name': 'Earth Engine Adapter',
        'uri': 'http://mymachine:5700',
        'port': 5700
    },
    'gee': {
        'service_account': 'skydipper@skydipper-196010.iam.gserviceaccount.com',
        'privatekey_file': '/opt/adapter-earth-engine/adapterearthengine/privatekey.json'
    }
}

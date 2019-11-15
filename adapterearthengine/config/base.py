from adapterearthengine.utils.files import BASE_DIR

SETTINGS = {
    'logging': {
        'level': 'WARN'
    },
    'service': {
        'name': 'Earth Engine Adapter',
        'uri': 'http://mymachine:5700',
        'port': 5700
    },
    'gee': {
        'service_account': 'skydipper@skydipper-196010.iam.gserviceaccount.com',
        'privatekey_file': './privatekey.json'
    }
}

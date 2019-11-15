import os
import json
import logging
import ee
import CTRegisterMicroserviceFlask
from flask import Flask
from adapterearthengine.config import SETTINGS
from adapterearthengine.routes.api import error
from adapterearthengine.routes.api.v1 import earth_engine_endpoints
from adapterearthengine.utils.files import load_config_json


# Logging
logging.basicConfig(
    level=SETTINGS.get('logging', {}).get('level'),
    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
    datefmt='%Y%m%d-%H:%M%p',
)

# Initializing GEE

gee = SETTINGS.get('gee')
ee_user = gee.get('service_account')
logging.debug(f"ee_user: {ee_user}")
private_key_file = gee.get('privatekey_file')
logging.debug(f"private_key_file: {private_key_file}")
#json_creds = os.path.exists('privatekey.json')
if private_key_file:
    logging.info('Initilizing EE with privatekey.json credential file')
    credentials = ee.ServiceAccountCredentials(ee_user, private_key_file)
    ee.Initialize(credentials)
    ee.data.setDeadline(60000)
else:
    raise ValueError("privatekey.json file not found. Unable to authenticate EE.")

# Flask
app = Flask(__name__)

# Config
app.config.from_object(SETTINGS)

# Routing
app.register_blueprint(earth_engine_endpoints, url_prefix='/api/v1/earthengine')

# CT
info = load_config_json('register')
swagger = load_config_json('swagger')
CTRegisterMicroserviceFlask.register(
    app=app,
    name='adapter-earth-engine',
    info=info,
    swagger=swagger,
    mode=CTRegisterMicroserviceFlask.AUTOREGISTER_MODE if os.getenv('CT_REGISTER_MODE') and os.getenv('CT_REGISTER_MODE') == 'auto' else CTRegisterMicroserviceFlask.NORMAL_MODE,
    ct_url=os.getenv('CT_URL'),
    url=os.getenv('LOCAL_URL')
)

@app.errorhandler(403)
def forbidden(e):
    logging.error('Forbidden')
    return error(status=403, detail='Forbidden')


@app.errorhandler(404)
def page_not_found(e):
    logging.error('Not Found')
    return error(status=404, detail='Not Found')


@app.errorhandler(405)
def method_not_allowed(e):
    logging.error('Method Not Allowed')
    return error(status=405, detail='Method Not Allowed')


@app.errorhandler(410)
def gone(e):
    logging.error('Gone')
    return error(status=410, detail='Gone')


@app.errorhandler(500)
def internal_server_error(e):
    logging.error('Internal Server Error')
    return error(status=500, detail='Internal Server Error')

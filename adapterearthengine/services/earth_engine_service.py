import logging

from adapterearthengine.errors import GEEQueryError
from sql2gee import SQL2GEE
from sql2gee.utils.jsonSql import JsonSql

def execute_query(query, geojson=None):
    logging.info('Executing Query: '+query)

    try:
        q = SQL2GEE(JsonSql(query).to_json(), geojson=geojson)
        logging.info(f'q: {q}')
        response = q.response
    except Exception as error:
        raise GEEQueryError(error)
    return response

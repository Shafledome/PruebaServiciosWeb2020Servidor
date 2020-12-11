from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
from entities.geocaches_entity import Geocache
from entities.logbook_entity import Logbook

import json
import datetime

app = Flask(__name__)
CORS(app)
mimetype = 'application/json'


# GET
@app.route('/geocaches/id/<int:geo_id>')
def get_geocache_by_id(geo_id: int):
    result = Geocache.get_geocache(geo_id)
    status = 200
    if result is None:
        status = 404
        result = f'Error 404. Geocache with id: {geo_id} not found.'
    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/geocaches/all')
def get_all_users():
    result = Geocache.get_all_geocaches()
    print(result)
    status = 200
    if result is None:
        status = 400
        result = f'Error 400. There are no geocaches.'
    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/geocaches/hint/<string:hint>')
def get_geocache_by_hint(hint: str):
    result = Geocache.geocache_by_hint(hint)
    status = 200
    if result is None:
        status = 404
        result = f'Error 404. Geocache with hint: {hint} not found.'
    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/logbooks/all')
def get_all_logbooks():
    result = Logbook.get_all_logbooks()
    status = 200
    if result is None:
        status = 400
        result = f'Error 400. There are no logbooks.'
    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/logbooks/email/<string:email>')
def get_logbook_by_email(email: str):
    result = Logbook.logbook_by_email(email)
    status = 200
    if result is None:
        status = 400
        result = f'Error 400. There are no logbooks.'
    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/geocaches/notfound')
def get_geocaches_not_found():
    result = Logbook.geocache_not_found()
    status = 200
    if result is None:
        status = 400
        result = f'Error 400. There are no not found geocaches.'
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# CREATE
@app.route('/geocaches/create/geocache', methods=['POST'])
def create_user():
    if not request.json:
        return Response(json.dumps({'error': f'Bad Request.'}), mimetype=mimetype, status=400)
    geo_id = request.json['id']
    lat = request.json['lat']
    lon = request.json['lon']
    image = request.json['image']
    hint = request.json['hint']
    geocache = Geocache.get_geocache(geo_id)
    status = 200
    if geocache is None:
        Geocache.create_geocache(geo_id, lat, lon, image, hint)
        result = {'result': f'Status 200. The geocache was created.'}
    else:
        status = 400
        result = {'error': f'Error 400. The geocache with id: {geo_id} is already in the database'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/logbooks/create/logbook', methods=['POST'])
def create_logbook():
    if not request.json:
        return Response(json.dumps({'error': f'Bad Request.'}), mimetype=mimetype, status=400)
    log_id = request.json['id']
    email = request.json['email']
    geocache = request.json['geocache']
    stamp = datetime.datetime.now()
    logbook = Logbook.get_logbook(log_id)
    status = 200
    if logbook is None:
        Logbook.create_logbook(log_id, email, geocache, stamp)
        result = {'result': f'Status 200. The logbook was created.'}
    else:
        status = 400
        result = {'error': f'Error 400. The logbook with id: {log_id} is already in the database'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# UPDATE
@app.route('/geocaches/update', methods=['PUT'])
def update_geocache():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    geo_id = request.json['id']
    entry = request.json['entry']
    value = request.json['value']
    status = 200
    geo = Geocache.get_geocache(geo_id)
    if geo is None:
        status = 404
        result = {'error': f'Error 404. Geocache with id: {geo_id} not found.'}
    else:
        Geocache.update_geo_value(geo_id, entry, value)
        result = {'result': f'Status 200. The geocache: {geo_id} was updated.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/logbooks/update', methods=['PUT'])
def update_logbook():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    log_id = request.json['id']
    entry = request.json['entry']
    value = request.json['value']
    status = 200
    log = Logbook.get_logbook(log_id)
    if log is None:
        status = 404
        result = {'error': f'Error 404. Geocache with id: {log_id} not found.'}
    else:
        Logbook.update_log_value(log_id, entry, value)
        result = {'result': f'Status 200. The logbook: {log_id} was updated.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


# DELETE
@app.route('/geocaches/delete', methods=['DELETE'])
def delete_geocache_by_id():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    geo_id = request.json['id']
    geo = Geocache.search_by_id(geo_id)
    status = 200
    if geo is None:
        status = 404
        result = {'error': f'Error 404. Not found. Can not found a geocache with id: {id}'}
    else:
        Geocache.delete_geocache(geo_id)
        result = {'result': f'Status 200. The geocache: {geo_id} was deleted.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


@app.route('/logbooks/delete', methods=['DELETE'])
def delete_logbook_by_id():
    if not request.json:
        return Response(json.dumps({'error': f'Bad request.'}), mimetype=mimetype, status=400)
    log_id = request.json['id']
    log = Geocache.search_by_id(log_id)
    status = 200
    if log is None:
        status = 404
        result = {'error': f'Error 404. Not found. Can not found a logbook with id: {id}'}
    else:
        Logbook.delete_logbook(log_id)
        result = {'result': f'Status 200. The logbook: {log_id} was deleted.'}
    return Response(json.dumps(result), mimetype=mimetype, status=status)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=30006, debug=True)

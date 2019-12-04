#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth
from datetime import datetime
from extract_embeddings import *
from recognize import *
from train_model import *

users = {
    "yse": "yse",
    "qinghan": "qinghan",
}

app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username in users:
        return users.get(username)
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

recognitions = [
#    {
#        'id': datetime.now().strftime("%Y%m%d%H%M%S"),
#        'title': u'Buy groceries',
#        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#        'done': False
#    },
#    {
#        'id': 2,
#        'title': u'Learn Python',
#        'description': u'Need to find a good Python tutorial on the web',
#        'done': False
#    }
]

def make_public_task(recognition):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id = task['id'], _external = True)
        else:
            new_task[field] = task[field]
    return new_task

#@app.route('/todo/api/v1.0/recognitions', methods = ['GET'])
#@auth.login_required
#def get_recognitions():
#    return jsonify( { 'recognitions': map(make_public_task, recognitions) } )
#
#@app.route('/todo/api/v1.0/recognitions/<int:task_id>', methods = ['GET'])
#@auth.login_required
#def get_task(task_id):
#    task = filter(lambda t: t['id'] == task_id, tasks)
#    if len(task) == 0:
#        abort(404)
#    return jsonify( { 'task': make_public_task(task[0]) } )
#
@app.route('/todo/api/v1.0/recognitions', methods = ['POST'])
@auth.login_required
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': recognitions[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify( { 'task': make_public_task(task) } ), 201

#@app.route('/todo/api/v1.0/recognitions/<int:task_id>', methods = ['PUT'])
#@auth.login_required
#def update_task(task_id):
#    task = filter(lambda t: t['id'] == task_id, tasks)
#    if len(task) == 0:
#        abort(404)
#    if not request.json:
#        abort(400)
#    if 'title' in request.json and type(request.json['title']) != unicode:
#        abort(400)
#    if 'description' in request.json and type(request.json['description']) is not unicode:
#        abort(400)
#    if 'done' in request.json and type(request.json['done']) is not bool:
#        abort(400)
#    task[0]['title'] = request.json.get('title', task[0]['title'])
#    task[0]['description'] = request.json.get('description', task[0]['description'])
#    task[0]['done'] = request.json.get('done', task[0]['done'])
#    return jsonify( { 'task': make_public_task(task[0]) } )
#
@app.route('/todo/api/v1.0/recognitions/<int:task_id>', methods = ['DELETE'])
@auth.login_required
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, recognitions)
    if len(task) == 0 or users.get(username) != "yse":
        abort(404)
    recognitions.remove(task[0])
    return jsonify( { 'result': True } )

if __name__ == '__main__':
    app.run(debug = True)
    

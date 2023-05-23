import json
from flask import request, abort
from flask_api import FlaskAPI
from flask_cors import CORS

app = FlaskAPI(__name__)
CORS(app)


def loadData():
    global data
    global tasks
    data = json.load(open('data.json'))
    tasks = data["tasks"]


@app.after_request
def after_request(response):
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.set('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/tasks/<id>')
def get_status(id):
    result = None
    for i in range(len(tasks)):
        if tasks[i]['id'] == int(id):
            result = tasks[i]
            break
    if result == None:
        return abort(404)
    
    return (str(result))


@app.route('/tasks')
def get_idElement():
    status = request.args.get('status')
    if status != None:
        result = list(filter(lambda x: x['status'] == status, tasks))
        return (str(result))
    return (str(tasks))


@app.route('/tasks/add')
def add():
    name = request.args.get('name')
    data['number_of_id'] += 1
    result = {
        "id": data['number_of_id'],
        "name": name,
        "status": "todo"
    }
    tasks.append(result)
    json.dump(data, open('data.json', 'w'))
    return (result)

if __name__ == "__main__":
    loadData()
    app.run(host="10.66.10.71", port=5000, debug=True)

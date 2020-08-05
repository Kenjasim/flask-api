import flask
from flask import request, jsonify

app = flask.Flask(__name__)

app.config["DEBUG"] = True

# Create test data
tasks = [
        {'id': 0,
         'title': 'Do the dishes',
         'user': 'Kenan',
         'date': '19-07-20'},
        {'id': 1,
         'title': 'Cook Food',
         'user': 'Kenan',
         'date': '19-07-20'}
        ]


@app.route('/', methods=['GET'])
def home():
    return "<h1>API Site</h1>"

# Return all the avaliable entries of the task
@app.route('/api/resources/tasks/all', methods=['Get'])
def api_all():
    return jsonify(tasks)

@app.route('/api/resources/tasks', methods=['Get'])
def api_id():
    #Check if an ID has been specified
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No ID specified"
    
    results = []

    for task in tasks:
        if task['id'] == id:
            results.append(task)

    return jsonify(results)

@app.route('/api/resources/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort (404)
    return jsonify ({'task': task[0]})


app.run()

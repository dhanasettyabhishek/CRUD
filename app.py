from flask import Flask, make_response, request
from main import ToDo

result = []
todo = ToDo(result)
app = Flask(__name__)

@app.route("/add_new_tasks/", methods=["POST"])
def newTask():
    data = request.json
    return make_response(todo.uploadData(data))

# Get Details
@app.route("/tasks/", methods=["GET"])
def tasks():
    return make_response(todo.tasks(), 200)


# Update
@app.route("/update_task_by_id/", methods=["PUT"])
def updateValues():
    data = request.json
    return make_response(todo.updateTasks(data))

# Delete
@app.route("/delete_task_by_id/<id>", methods=["DELETE"])
def deleteValue(id):
    try:
        id = int(id)
    except:
        print("ID not an integer")
    return make_response(todo.deleteTask(id))

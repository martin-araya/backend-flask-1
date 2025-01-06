from flask import Blueprint, request, jsonify

tasks_bp = Blueprint('tasks', __name__)

# Mock database
tasks = []

# Crear una tarea
@tasks_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    task_id = len(tasks) + 1
    new_task = {'id': task_id, 'title': title, 'description': description}
    tasks.append(new_task)
    return jsonify(new_task), 201

# Leer las tareas
@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# Actualizar una tarea
@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    return jsonify(task), 200

# Eliminar una tarea
@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 200
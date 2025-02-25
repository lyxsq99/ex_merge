from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_item():
    if not request.json:
        return jsonify({"error": "No data provided"}), 400
    
    item = request.json.get('item')
    if not item or not isinstance(item, str):  # 假设 item 应为字符串
        return jsonify({"error": "Item data is invalid or missing"}), 400
    
    if item in todos:
        return jsonify({"error": "Item already exists"}), 400
    
    todos.append(item)
    return jsonify(item), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id >= len(todos) or todo_id < 0:
        return jsonify({'error': 'Todo not found'}), 404
    todo = request.json
    todos[todo_id] = todo
    return jsonify(todo), 200

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id >= len(todos) or todo_id < 0:
        return jsonify({'error': 'Todo not found'}), 404
    todo = todos.pop(todo_id)
    return jsonify(todo), 200

if __name__ == '__main__':
    app.run(debug=True)
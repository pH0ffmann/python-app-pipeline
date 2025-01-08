# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the simple Flask app!")

@app.route('/health')
def health():
    return jsonify(status="UP")

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify(received=data)

@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'POST':
        item = request.json.get('item')
        return jsonify(message=f"Item '{item}' added successfully!"), 201
    else:
        sample_items = ["item1", "item2", "item3"]
        return jsonify(items=sample_items)

@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def item_detail(item_id):
    if request.method == 'GET':
        return jsonify(item=f"item{item_id}")
    elif request.method == 'PUT':
        new_item = request.json.get('item')
        return jsonify(message=f"Item {item_id} updated to '{new_item}'")
    elif request.method == 'DELETE':
        return jsonify(message=f"Item {item_id} deleted"), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
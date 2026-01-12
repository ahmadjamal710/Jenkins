from flask import Flask, request, jsonify

app = Flask(__name__)

orders = [
    {"id": 1, "customer": "Ahmad", "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
    {"id": 2, "customer": "Ayman", "item": "Mouse", "quantity": 2, "price": 19.99, "status": "pending"}
]
next_id = 3

def find_order(order_id):
    return next((o for o in orders if o["id"] == order_id), None)

def validate(data):
    if not all(k in data for k in ['customer', 'item', 'quantity', 'price']):
        return "Missing fields", 400
    if not isinstance(data['quantity'], int) or data['quantity'] <= 0:
        return "Invalid quantity", 400
    if not isinstance(data['price'], (int, float)) or data['price'] <= 0:
        return "Invalid price", 400
    return None, 200

@app.route('/')
def home():
    return {"msg": "Welcome to the Orders API"}

@app.route('/orders', methods=['GET', 'POST'])
def orders_handler():
    global next_id
    if request.method == 'GET':
        return jsonify(orders)
    data = request.get_json()
    error, code = validate(data)
    if error:
        return jsonify({"error": error}), code
    order = {**data, "id": next_id, "status": "pending"}
    orders.append(order)
    next_id += 1
    return jsonify(order), 201

@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def order_handler(order_id):
    order = find_order(order_id)
    if not order:
        return jsonify({"error": "Not found"}), 404

    if request.method == 'GET':
        return jsonify(order)

    if request.method == 'PUT':
        data = request.get_json()
        error, code = validate(data)
        if error:
            return jsonify({"error": error}), code
        order.update(data)
        return jsonify(order)

    if request.method == 'DELETE':
        orders.remove(order)
        return jsonify({"msg": "Deleted"})

if __name__ == '__main__':
    app.run(debug=True, port=5050)
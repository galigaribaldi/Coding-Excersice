from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user():
    # Obtener el JSON de la petición
    data = request.get_json()
    
    # Validar que el JSON tiene el campo "name"
    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' field"}), 400
    
    # Crear la respuesta
    response = {
        "message": f"Welcome, {data['name']}!",
        "status": "success"
    }
    
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)

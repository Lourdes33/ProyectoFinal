from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Habilita la comunicación con Vue.js

# --- RUTAS PÚBLICAS (Estudiantes) ---
@app.route('/api/test/evaluar', methods=['POST'])
def evaluar_test():
    respuestas = request.json
    print("Respuestas recibidas del estudiante:", respuestas)
    
    # Aquí es donde, en el futuro, llamaremos a tu sistema probabilístico
    # ej: resultado = calcular_probabilidades(respuestas)
    
    return jsonify({
        "mensaje": "Test recibido correctamente (Simulado desde Flask)",
        "resultado": {
            "areaPrincipal": "Ingeniería y Ciencias Exactas",
            "descripcion": "Respuesta generada desde el servidor en Python."
        }
    }), 200

# --- RUTAS PRIVADAS (Administrador) ---
@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    datos = request.json
    email = datos.get('email')
    password = datos.get('password')
    
    print(f"Intento de login con email: {email}")
    
    # Lógica temporal para probar la ruta
    if email == 'adm@sistema.com' and password == 'admin':
        return jsonify({"token": "token_falso_del_backend_flask"}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

if __name__ == '__main__':
    # El modo debug reinicia el servidor al detectar cambios en el código
    app.run(debug=True, port=5000)
# app/routes.py
from flask import jsonify, request
from app import app, db
from app.models import User

# Endpoint para crear un usuario   FUNCIONA OK!
@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        # Obtener datos del JSON en la solicitud
        data = request.get_json()

        # Validar datos de entrada
        required_fields = ['nombres', 'email', 'username', 'password', 'cuenta', 'saldo']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Campo obligatorio faltante: {field}'}), 400

        # Crear un nuevo usuario
        new_user = User(
            nombres=data['nombres'],
            email=data['email'],
            username=data['username'],
            password=data['password'],
            cuenta=data['cuenta'],
            saldo=data['saldo']
        )

        # Agregar el nuevo usuario a la base de datos
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'Usuario creado correctamente'}), 201

    except KeyError as e:
        # Manejar errores de datos faltantes
        return jsonify({'error': f'Dato faltante: {str(e)}'}), 400

    except Exception as e:
        # Manejar posibles errores de manera adecuada
        return jsonify({'error': f'Error al crear usuario: {str(e)}'}), 500

#Obtener usuario segun ID FUNCIONA Ok!
@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        with app.app_context():
            user = User.query.get(user_id)

            if user:
                user_data = {
                    'id': user.id,
                    'nombres': user.nombres,
                    'email': user.email,
                    'username': user.username,
                    'cuenta': user.cuenta,
                    'saldo': user.saldo
                }
                return jsonify(user_data), 200
            else:
                return jsonify({'error': 'Usuario no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': f'Error al obtener usuario: {str(e)}'}), 500

# Endpoint para actualizar un usuario existente   FUNCION OK!
@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        # Obtener datos del JSON en la solicitud
        data = request.get_json()

        # Buscar el usuario en la base de datos por ID
        user = User.query.get(user_id)

        if user:
            # Actualizar los campos proporcionados en la solicitud
            user.nombres = data.get('nombres', user.nombres)
            user.email = data.get('email', user.email)
            user.username = data.get('username', user.username)
            user.password = data.get('password', user.password)
            user.cuenta = data.get('cuenta', user.cuenta)
            user.saldo = data.get('saldo', user.saldo)

            # Confirmar los cambios en la base de datos
            db.session.commit()

            return jsonify({'message': 'Usuario actualizado correctamente'}), 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404

    except Exception as e:
        # Manejar posibles errores de manera adecuada
        return jsonify({'error': str(e)}), 500

# Endpoint para borrar un usuario NO FUNCIONA :
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        # Buscar el usuario en la base de datos por ID
        user = User.query.get(user_id)

        if user:
            # Eliminar el usuario de la base de datos
            db.session.delete(user)
            db.session.commit()

            return jsonify({'message': 'Usuario eliminado correctamente'}), 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404

    except Exception as e:
        # Manejar posibles errores de manera adecuada
        return jsonify({'error': str(e)}), 500

# Endpoint para listar todos los usuarios  FUNCIONA OK!
@app.route('/list_users', methods=['GET'])
def list_users():
    try:
        # Obtener todos los usuarios de la base de datos
        users = User.query.all()

        # Crear una lista con los datos de los usuarios
        users_list = []
        for user in users:
            user_data = {
                'id': user.id,
                'nombres': user.nombres,
                'email': user.email,
                'username': user.username,
                'cuenta': user.cuenta,
                'saldo': user.saldo
            }
            users_list.append(user_data)

        # Devolver la lista de usuarios en formato JSON
        return jsonify({'users': users_list}), 200

    except Exception as e:
        # Manejar posibles errores de manera adecuada
        return jsonify({'error': str(e)}), 500

# Endpoint para transferir saldo entre usuarios FUNCIONA Ok!
@app.route('/transfer_balance', methods=['POST'])
def transfer_balance():
    try:
        # Obtener datos del JSON en la solicitud
        data = request.get_json()

        # Validar datos de entrada
        required_fields = ['remitente_username', 'beneficiario_username', 'amount']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Campo obligatorio faltante: {field}'}), 400

        # Obtener usuarios de la base de datos
        remitente = User.query.filter_by(username=data['remitente_username']).first()
        beneficiario = User.query.filter_by(username=data['beneficiario_username']).first()

        if not remitente or not beneficiario:
            return jsonify({'error': 'Usuario no encontrado'}), 404

        # Validar que el saldo del remitente sea suficiente
        if remitente.saldo < float(data['amount']):
            return jsonify({'error': 'Saldo insuficiente para la transferencia'}), 400

        # Realizar la transferencia
        remitente.saldo -= float(data['amount'])
        beneficiario.saldo += float(data['amount'])

        # Actualizar la base de datos
        db.session.commit()

        return jsonify({'message': 'Transferencia exitosa'}), 200

    except KeyError as e:
        return jsonify({'error': f'Dato faltante: {str(e)}'}), 400

    except Exception as e:
        return jsonify({'error': f'Error al realizar la transferencia: {str(e)}'}), 500
    
    #Realizar deposito en cuenta 
    # app/routes.py
from flask import jsonify, request
from app import app, db
from app.models import User

@app.route('/deposit', methods=['POST'])
def deposit():
    try:
        data = request.get_json()

        # Verifica si los campos requeridos están presentes
        required_fields = ['username', 'amount']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Campo obligatorio faltante: {field}'}), 400

        # Busca el usuario en la base de datos
        user = User.query.filter_by(username=data['username']).first()

        if user:
            # Realiza el depósito
            user.saldo += data['amount']
            db.session.commit()

            return jsonify({'message': f'Depósito de {data["amount"]} realizado correctamente'}), 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

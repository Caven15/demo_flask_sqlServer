from flask import Blueprint, jsonify, request
from app import db
from app.model import User

main = Blueprint('main', __name__)

# Route pour récupérer tous les utilisateurs
@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Route pour ajouter un nouvel utilisateur
@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

# Route pour récupérer un utilisateur par ID
@main.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404

# Route pour mettre à jour un utilisateur
@main.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if user:
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404

# Route pour supprimer un utilisateur
@main.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

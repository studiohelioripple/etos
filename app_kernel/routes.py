from flask import Blueprint, request, jsonify
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError


from app_kernel.db import SessionLocal
from app_kernel.models import User

bp = Blueprint("main", __name__)

@bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "name and email are required"}), 400

    with SessionLocal() as db:
        try:
            user = User(name=name, email=email)
            db.add(user)
            db.commit()
            db.refresh(user)

            return jsonify({
                "id": user.id,
                "name": user.name,
                "email": user.email
            }), 201

        except IntegrityError:
            db.rollback()
            return jsonify({"error": "Email already exists"}), 409

        except Exception as e:
            db.rollback()
            return jsonify({"error": str(e)}), 500


@bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    with SessionLocal() as db:
        result = db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()

        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
        

from flask import Flask, request, jsonify
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from db import SessionLocal, engine, Base
from models import User
from config import Config

app = Flask(__name__)

# Temporary for learning:
# Base.metadata.create_all(bind=engine)

@app.route("/")
def home():
    return {"message": "Flask + MySQL app is running"}

@app.route("/env")
def get_env():
    w= Config.__dict__
    return {"configs": str(w) }


# @app.route("/users", methods=["POST"])
# def create_user():
#     data = request.get_json()

#     if not data:
#         return jsonify({"error": "No JSON data provided"}), 400

#     name = data.get("name")
#     email = data.get("email")

#     if not name or not email:
#         return jsonify({"error": "name and email are required"}), 400

#     with SessionLocal() as db:
#         try:
#             user = User(name=name, email=email)
#             db.add(user)
#             db.commit()
#             db.refresh(user)

#             return jsonify({
#                 "id": user.id,
#                 "name": user.name,
#                 "email": user.email
#             }), 201

#         except IntegrityError:
#             db.rollback()
#             return jsonify({"error": "Email already exists"}), 409

#         except Exception as e:
#             db.rollback()
#             return jsonify({"error": str(e)}), 500

# @app.route("/users", methods=["GET"])
# def list_users():
#     with SessionLocal() as db:
#         result = db.execute(select(User))
#         users = result.scalars().all()

#         return jsonify([
#             {
#                 "id": user.id,
#                 "name": user.name,
#                 "email": user.email
#             }
#             for user in users
#         ])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

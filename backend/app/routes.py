from flask import Flask, jsonify, request

from .validators import validate_registration


def register_routes(app: Flask) -> None:
    @app.get("/health")
    def health():
        return jsonify({
            "success": True,
            "message": "Flask API is running."
        }), 200

    @app.post("/register")
    def register():
        if not request.is_json:
            return jsonify({
                "success": False,
                "message": "Content-Type must be application/json."
            }), 415

        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({
                "success": False,
                "message": "Request body must contain a valid JSON object."
            }), 400

        errors = validate_registration(data)

        if errors:
            return jsonify({
                "success": False,
                "message": "Validation failed.",
                "errors": errors
            }), 400

        # Intentionally do not persist or return the password.
        return jsonify({
            "success": True,
            "message": "Registration successful.",
            "data": {
                "name": str(data["name"]).strip(),
                "email": str(data["email"]).strip(),
                "mobile": str(data["mobile"]).strip()
            }
        }), 201

import re
from email_validator import EmailNotValidError, validate_email


def validate_registration(data: dict) -> dict:
    errors = {}

    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    mobile = str(data.get("mobile", "")).strip()
    password = str(data.get("password", ""))

    if not name:
        errors["name"] = "Name is required."
    elif len(name) < 2:
        errors["name"] = "Name must contain at least 2 characters."

    if not email:
        errors["email"] = "Email is required."
    else:
        try:
            validate_email(email, check_deliverability=False)
        except EmailNotValidError:
            errors["email"] = "Please provide a valid email address."

    if not mobile:
        errors["mobile"] = "Mobile number is required."
    elif not re.fullmatch(r"[0-9]{10,15}", mobile):
        errors["mobile"] = "Mobile number must contain 10–15 digits."

    if not password:
        errors["password"] = "Password is required."
    elif len(password) < 8:
        errors["password"] = "Password must contain at least 8 characters."

    return errors

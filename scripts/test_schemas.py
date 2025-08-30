# scripts/test_schemas.py
import sys, os

# Add the parent folder (project root) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.schemas import RegisterSchema, LoginSchema
from pydantic import ValidationError


good = {"email": "test@example.com", "password": "secret", "name": "Ektaa"}
bad = {"email": "not-an-email", "password": "pw"}

try:
    r = RegisterSchema(**good)
    print("RegisterSchema OK:", r)
except ValidationError as e:
    print("RegisterSchema error:", e)

try:
    l = LoginSchema(**bad)
    print("LoginSchema OK:", l)
except ValidationError as e:
    print("LoginSchema error:", e)

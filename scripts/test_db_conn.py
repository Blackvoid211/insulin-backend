import sys, os
# ensure project root is on path (helps if you run script from anywhere)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db import engine
from app.models import Base

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✔ Tables created (users, food_items) if your DB supports it.")

if __name__ == "__main__":
    create_tables()

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db import SessionLocal
from app.models import FoodItem

SEEDS = [
    {"name": "Plain Roti (atta)", "carbs_per_100g": 49.0, "source":"seed"},
    {"name": "Cooked Rice (white)", "carbs_per_100g": 28.0, "source":"seed"},
    {"name": "Idli", "carbs_per_100g": 30.0, "source":"seed"},
    {"name": "Dosa (plain)", "carbs_per_100g": 38.0, "source":"seed"},
    {"name": "Poha", "carbs_per_100g": 26.0, "source":"seed"},
]

def run():
    db = SessionLocal()
    for row in SEEDS:
        exists = db.query(FoodItem).filter(FoodItem.name==row["name"]).first()
        if not exists:
            db.add(FoodItem(**row))
    db.commit()
    db.close()
    print("Seed complete.")

if __name__ == "__main__":
    run()

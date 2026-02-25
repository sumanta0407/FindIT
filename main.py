from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, College
from recommender import score_college

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def seed_data():
    db = SessionLocal()
    if db.query(College).count() == 0:
        colleges = [
            College(
                name="Indian Institute of Science",
                location="Bangalore",
                country="India",
                ranking=1,
                specialization="Astrophysics",
                tuition=30000,
                entrance_exam="JAM/GATE",
                scholarship=True,
                website="https://iisc.ac.in"
            )
        ]
        db.add_all(colleges)
        db.commit()
    db.close()

@app.get("/")
def root():
    return {"message": "Backend Running"}

@app.post("/api/recommend")
def recommend(user_input: dict, db: Session = Depends(get_db)):
    colleges = db.query(College).all()
    scored = []

    for college in colleges:
        s = score_college(college, user_input)
        scored.append((college, s))

    ranked = sorted(scored, key=lambda x: x[1], reverse=True)

    return {
        "recommendations": [
            {
                "name": c.name,
                "location": c.location,
                "country": c.country,
                "ranking": c.ranking
            }
            for c, _ in ranked
        ]
    }

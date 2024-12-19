from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal, engine
import crud, models

models.Base.metadata.create_all(bind=engine)# la fonction create_all est définie dans models.py

app = FastAPI()

def get_db():# la fonction get_db permet de créer une session de base de données pour chaque requête
    db = SessionLocal()
    try:
        yield db# le mot-clé yield permet de retourner une valeur sans arrêter la fonction
    finally:
        db.close()

@app.get("/")
def show_users(db: Session = Depends(get_db)):
    users = crud.show_users(db)# la fonction show_users est définie dans crud.py
    if users is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users

@app.get("/{user_id}")
def get_user(*,db: Session = Depends(get_db), user_id: int):
    user = crud.get_user(db, user_id)# la fonction get_user est définie dans crud.py
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.api_route("/adduser/{name}/{email}", methods=["GET", "POST"])
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    return crud.create_user(db, name=name, email=email)# la fonction create_user est définie dans crud.py

"""
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Vérifier si l'email existe déjà (optionnel)
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Ajouter le nouvel utilisateur
    return crud.create_user(db=db, name=user.name, email=user.email)
    """

from sqlalchemy.orm import Session
import models

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def show_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, name: str, email: str):
    db_user = models.User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
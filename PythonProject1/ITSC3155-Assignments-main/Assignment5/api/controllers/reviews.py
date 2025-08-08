from idlelib.macosx import setupApp

from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, review):
    db_review = models.Review(
        review_name=review.review_name,
        description=review.description
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def read_all(db: Session):
    return db.query(models.Review).all()


def read_one(db: Session, review_id):
    return db.query(models.Review).filter(models.Review.id == review_id).first()


def update(db: Session, review_id, review):
    db_review = db.query(models.Review).filter(models.Review.id == review_id)
    update_data = review.model_dump(exclude_unset=True)
    db_review.update(update_data, synchronize_session=False)
    db.commit()
    return db_review.first()


def delete(db: Session, review_id):
    db_review = db.query(models.Review).filter(models.Review.id == review_id)
    db_review.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create_order_details(db: Session, order_detail):
    db_order_detail = models.OrderDetails(
        order_detail_name=order_detail.order_detail_name,
        order_detail_description=order_detail.order_detail_description
    )
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail


def read_all(db: Session):
    return db.query(models.OrderDetails).all()


def read_one(db: Session, order_detail_id):
    return db.query(models.OrderDetails).filter(models.OrderDetails.order_detail_id == order_detail_id).first()


def update(db: Session, order_detail_id, order_detail):
    db_order_detail = db.query(models.OrderDetails).filter(models.OrderDetails.order_detail_id == order_detail_id)
    update_data = order_detail.model_dump(exclude_unset=True)
    db_order_detail.update(update_data, synchronize_session=False)
    db.commit()
    return db_order_detail.first()


def delete(db: Session, order_detail_id):
    db_order_detail = db.query(models.OrderDetails).filter(models.OrderDetails.order_detail_id == order_detail_id)
    db_order_detail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
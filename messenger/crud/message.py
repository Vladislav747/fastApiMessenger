import datetime
from sqlalchemy.orm import Session
import schemas.message as schema
from core.db.models import Message

messages_database = [
    {
        "id": 1,
        "user_id": 1,
        "chat_id": 1,
        "message": "Hello",
        "created_date": datetime.datetime.now(),
    },
    {
        "id": 2,
        "user_id": 2,
        "chat_id": 1,
        "message": "Hello to you",
        "created_date": datetime.datetime.now(),
    },
    {
        "id": 3,
        "user_id": 2,
        "chat_id": 1,
        "message": "Hello to you",
        "created_date": datetime.datetime(2021, 9, 27, 13, 39, 25, 771446),
    },
    {
        "id": 4,
        "user_id": 2,
        "chat_id": 1,
        "message": "Hello to you",
        "created_date": datetime.datetime(2021, 10, 27, 13, 39, 25, 771446),
    },
    {
        "id": 5,
        "user_id": 2,
        "chat_id": 1,
        "message": "Hello to you",
        "created_date": datetime.datetime(2021, 11, 27, 13, 39, 25, 771446),
    }
]

def create_message(db: Session, message: schema.Message):
    """Создать сообщение"""
    chat_db = Message(message=message.message)
    db.add(chat_db)
    db.commit()

    return chat_db

def get_all_messages(db: Session):
    """Получить все сообщения"""
    return db.query(Message).all()

def get_message_by_id(db: Session, message_id: int):
    """Получить сообщение по id"""
    return db.query(Message).filter(Message.id == message_id).one_or_none()
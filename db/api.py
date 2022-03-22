from sqlalchemy import func, or_
from sqlalchemy.orm import sessionmaker
from db.models import Keys
import sqlalchemy as db
import os
import logging


class DB:
    def __init__(self):
        try:
            uri = os.getenv("DATABASE_URL")
            if uri.startswith("postgres://"):
                uri = uri.replace("postgres://", "postgresql://", 1)
            self.engine = db.create_engine(uri, pool_size=20)
        except Exception as e:
            logging.error(e)

    def __del__(self):
        self.engine.dispose()

    def create_session(self):
        session = sessionmaker(bind=self.engine)
        return session()

    def select_key(self, name):
        session = self.create_session()
        key = session.query(Keys).filter_by(name=name).first()
        session.expunge_all()
        session.close()
        return key

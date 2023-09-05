import asyncio

from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

import sqlalchemy as db
import datetime as dt


DSN = 'postgresql+asyncpg://postgres:postgres@127.0.0.1:5439/avito_aiohttp'
engine = create_async_engine(DSN)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    cards = relationship('Card', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Card(Base):
    __tablename__ = 'cards'

    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, index=True, default=dt.datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Card {}>'.format(self.title)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()


if __name__ == '__main__':
    asyncio.run(create_db())

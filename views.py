from aiohttp import web
from sqlalchemy import select
import sqlalchemy as db

from models import User, Session, Card
from serializers import serialize_user, serialize_card


def cards():
    if request.method == 'POST':
        c = Card(**request.json)
        db.session.add(c)
        db.session.commit()
        return serialize_card(c)

    else:
        qs = Card.query.all()
        list_result = []

        for x in qs:
            list_result.append(serialize_card(x))
        return list_result


async def get_users(request):
    async with Session() as session:
        qs = await session.execute(select(User))
        return web.json_response(data=[serialize_user(x[0]) for x in qs])


async def create_user(request):
    data = await request.json()
    u = User(**data)
    async with Session() as session:
        session.add(u)
        await session.commit()
    return web.json_response(data=serialize_user(u))


















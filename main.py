from aiohttp import web

from views import get_users, create_user


app = web.Application()
app.add_routes([
    web.get('/api/users', get_users),
    web.post('/api/users', create_user),
])


if __name__ == '__main__':
    web.run_app(app)


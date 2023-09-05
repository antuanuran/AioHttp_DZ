from models import Card, User


def serialize_card(card: Card):
    return {
        'id': card.id,
        'title': card.title,
        'description': card.description,
        'user_id': card.user_id,
        'created_at': card.created_at.isoformat(),
    }


def serialize_user(user: User):
    return {'id': user.id, 'username': user.username, 'password_hash': user.password_hash}
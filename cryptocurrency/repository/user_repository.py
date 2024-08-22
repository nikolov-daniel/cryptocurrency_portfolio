from cryptocurrency.model.user import User


def get_all_users() -> User:
    return User.query.all()


def get_user_by_username(username: str) -> User:
    return User.query.filter(User.username == username).first()


def get_user_by_email(email: str) -> User:
    return User.query.filter(User.email == email).first()

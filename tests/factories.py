from nbateam.models import User


def user_factory(i):
    return User(
        email="user{}@mail.com".format(i)
    )

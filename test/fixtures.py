from tcidatabase.models import Token, User


def create_user():
    return User(firstname='fixtures').save()


def create_token(survey):
    return Token(user=create_user(), survey=survey).save()

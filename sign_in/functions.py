from django.core.exceptions import ObjectDoesNotExist
from sign_in import models
from sign_in.models import Users


class Error(Exception):
    pass


class Username_already_exist_Error(Error):
    pass


class Username_dosent_exist_Error(Error):
    pass


class Username_password_missmatch_Error(Error):
    pass


def register(username: str, password: str) ->models.Users:
    if is_username_present(username):
        raise Username_already_exist_Error
    else:
        temp = Users(username=username, password=password)
        temp.save()
        return temp


def does_username_and_password_match(username: str, password: str) -> bool:
        try:
            user = models.Users.objects.get(username=username)
            if user.password == password:
                return True
            else:
                return False
        except ObjectDoesNotExist:
            return False


def login(username: str, password: str) -> bool:
    if is_username_present(username):
        if does_username_and_password_match(username, password):
            return True
        else:
            raise Username_password_missmatch_Error
    else:
        raise Username_dosent_exist_Error


def is_username_present(username: str) -> bool:
    try:
        user = models.Users.objects.get(username=username)
        return True
    except ObjectDoesNotExist:
        return False




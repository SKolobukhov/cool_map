from core.permissions import Permissions
from core.urn import Urn


class SessionState(object):
    def __init__(
            self,
            session_id: str,
            user_id: str,
            auth_mode: str,
            creation_date: str,
            ip_address: str):
        self.session_id = session_id
        self.user_id = user_id
        self.auth_mode = auth_mode
        self.creation_date = creation_date
        self.ip_address = ip_address


class FailResultSimple(object):
    def __init__(
            self,
            status: str = 'UndefinedError',
            message: str = ''):
        self.status = status
        self.message = message

    def __str__(self):
        return self.status + ': ' + self.message


class FailResult(FailResultSimple):
    def __init__(
            self,
            status: str = 'UndefinedError',
            message: str = '',
            code: int = None):
        self.code = code
        super(FailResult, self).__init__(status, message)

    def __str__(self):
        return self.status + '(' + str(self.code) + '): ' + self.message


class ItemsResult(object):
    def __init__(
            self,
            items,
            skip: int,
            take: int,
            count: int):
        self.items = items
        self.skip = skip
        self.take = take
        self.count = count


class Permission(object):
    def __init__(
            self,
            subject: Urn,
            object: Urn,
            value: Permissions):
        self.subject = subject
        self.object = object
        self.value = value if isinstance(value, Permissions) \
            else Permissions(value)


class Form(object):
    def __init__(
            self,
            id: str,
            creator: str,
            title: str,
            description: str,
            content: str):
        self.id = id
        self.creator = creator
        self.title = title
        self.description = description
        self.content = content


class Answer(object):
    def __init__(self, id: str, respondent_id: str, form_id: str, place_id: str, answer: str):
        self.id = id
        self.respondent_id = respondent_id
        self.form_id = form_id
        self.place_id = place_id
        self.answer = answer


class User(object):
    def __init__(self, id: str, login: str, email: str):
        self.id = id
        self.login = login
        self.email = email


class Binding(object):
    def __init__(self, form_id: str, place_id: str):
        self.form_id = form_id
        self.place_id = place_id


class Place(object):
    def __init__(self, id: str, osm_type: str, osm_id: int, title: str, address: str):
        self.id = id
        self.osm_type = osm_type
        self.osm_id = osm_id
        self.title = title
        self.address = address

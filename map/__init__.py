from core.auth_policy import CookieAuthenticationPolicy, AuthorizationPolicy
from core.configuration import ConfigurationWrapper
from core.permissions import Permissions
from core.response import HTTPTemporaryRedirect
from pyramid.config import Configurator


def get_app(global_config, **settings):
    ConfigurationWrapper.init('map', **settings)

    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('map_static', 'map:static', cache_max_age=3600)
    config.add_static_view('core_static', 'core:static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('enter', '/enter')
    config.add_route('exit', '/exit')
    config.add_route('anketa', '/anketa')
    config.add_route('xXx_PRO100anketka228_xXx', '/xXx_PRO100anketka228_xXx')
    config.add_route('choose', '/choose')
    config.add_route('registration', '/registration')
    config.scan()
    config.add_notfound_view(lambda r: HTTPTemporaryRedirect('/'))
    config.set_default_permission(Permissions.Null)
    config.set_authentication_policy(CookieAuthenticationPolicy())
    config.set_authorization_policy(AuthorizationPolicy(ConfigurationWrapper.get_auth('map')))
    return config.make_wsgi_app()

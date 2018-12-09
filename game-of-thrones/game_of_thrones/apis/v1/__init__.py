from arrested import ArrestedAPI
from .users import users_resource
from .characters import characters_resource
from .middleware import get_api_client_from_request, get_client_token

api_v1 = ArrestedAPI(
    url_prefix='/v1',
    before_all_hooks=[
        get_api_client_from_request,
        get_client_token
    ]
)
api_v1.register_resource(users_resource, defer=True)
api_v1.register_resource(characters_resource, defer=True)

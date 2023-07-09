from fastapi_keycloak import FastAPIKeycloak
from api.core.config import settings

idp = FastAPIKeycloak(
    server_url=f"{settings.KEYCLOAK_URL}/auth",
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    admin_client_secret=settings.ADMIN_CLIENT_SECRET,
    realm=settings.KEYCLOAK_REALM,
    callback_uri=f"{settings.KEYCLOAK_URL}/callback"
)

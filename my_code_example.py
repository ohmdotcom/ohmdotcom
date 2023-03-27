import requests
import json
import os

# Настройки Keycloak
KEYCLOAK_URL = "https://keycloak.host.ru"
REALM = "myrealm"
ADMIN_USERNAME = os.environ.get('KEYCLOAK_USERNAME')
ADMIN_PASSWORD = os.environ.get('KEYCLOAK_PASSWORD')

# Настройки client, имя и id
CLIENTS = [
    {"client_id": "name", "client_name": "name"},
    {"client_id": "name2", "client_name": "name2"},
    {"client_id": "name3", "client_name": "name3"},
    {"client_id": "name4", "client_name": "name4"}
]
ACCESS_TYPE = "confidential"
REDIRECT_URL = "/*"
BASE_URL = "/"

# Получаем token
data = {
    "grant_type": "password",
    "username": ADMIN_USERNAME,
    "password": ADMIN_PASSWORD,
    "client_id": "admin-user"
}

r = requests.post(f"{KEYCLOAK_URL}/auth/realms/{REALM}/protocol/openid-connect/token", data=data)
access_token = r.json()["access_token"]

# Создаём clients с условием. Меняется access_type для двух клиентов с определённым именем
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

for client in CLIENTS:
    client_id = client["client_id"]
    client_name = client["client_name"]
    
    if client_id == "name1":
        access_type = "public"
        redirect_url = "/dataflows"
        base_url = "/dataflows"
        root_url = f"{KEYCLOAK_URL}/dataflows"
        admin_url = root_url
        web_origin_url = root_url
    elif client_id == "name2":
        access_type = "public"
        redirect_url = "/api/dataflows"
        base_url = "/api/dataflows"
        root_url = f"{KEYCLOAK_URL}/api/dataflows"
        admin_url = root_url
        web_origin_url = root_url
    else:
        access_type = "confidential"
        redirect_url = "/*"
        base_url = "/"
        root_url = f"{KEYCLOAK_URL}/{client_id}"
        admin_url = root_url
        web_origin_url = root_url
    
    data = {
        "clientId": client_id,
        "name": client_name,
        "enabled": True,
        "redirectUris": [REDIRECT_URL],
        "baseUrl": BASE_URL,
        "rootUrl": root_url,
        "adminUrl": admin_url,
        "webOrigins": [web_origin_url],
        "bearerOnly": False,
        "consentRequired": False,
        "standardFlowEnabled": True,
        "implicitFlowEnabled": False,
        "directAccessGrantsEnabled": False,
        "serviceAccountsEnabled": False,
        "publicClient": False,
        "frontchannelLogout": True,
        "protocol": "openid-connect",
        "attributes": {
            "access.type": ACCESS_TYPE
        }
    }
    r = requests.post(f"{KEYCLOAK_URL}/auth/admin/realms/{REALM}/clients", headers=headers, data=json.dumps(data))
    
    # Проверяем создался ли client
    if r.status_code == 201:
        print("Success")
    else:
        print("Something went wrong")

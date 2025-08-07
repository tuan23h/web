import requests

HASS_URL = "http://localhost:8123/api/services"
HASS_TOKEN = "YOUR_LONG_LIVED_ACCESS_TOKEN"

HEADERS = {
    "Authorization": f"Bearer {HASS_TOKEN}",
    "Content-Type": "application/json",
}

def call_hass_service(intent):
    if intent == "turn_on_light":
        entity = "light.phong_khach"
        domain = "light"
        service = "turn_on"
    elif intent == "turn_off_light":
        entity = "light.phong_khach"
        domain = "light"
        service = "turn_off"
    else:
        return False

    url = f"{HASS_URL}/{domain}/{service}"
    data = {"entity_id": entity}

    response = requests.post(url, headers=HEADERS, json=data)
    return response.status_code == 200

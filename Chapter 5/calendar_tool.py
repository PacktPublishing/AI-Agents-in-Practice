import requests
from datetime import datetime

def get_outlook_calendar_events(access_token: str, date: str = None):
    """
    Fetches Outlook calendar events for a given date using Microsoft Graph API.
    """

    if not date:
        date = datetime.today().date().isoformat()

    start_datetime = f"{date}T00:00:00"
    end_datetime = f"{date}T23:59:59"

    url = f"https://graph.microsoft.com/v1.0/me/calendarview?startDateTime={start_datetime}&endDateTime={end_datetime}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    return response.json()

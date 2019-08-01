import requests
import json


def send_results(results):
    try:
        response = requests.post(
            url="https://jarvis.surfstudio.ru/api/v1/analytics/buildinfo",
            params={
                "authToken": "5f7b7b74-a77b-4f6a-8104-78a71eab8bad",
            },
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "info": results
            })
        )
        return response.status_code
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
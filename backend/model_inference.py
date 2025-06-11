
import requests

API_KEY = "IUKu8wLuIQyql1iesKFkjbgNnsxs3DSKFPnn22YPAE2Q"
DEPLOYMENT_URL = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/8e1850a3-4337-4033-84de-cb72e7148a2c/predictions?version=2021-05-01"

def get_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "apikey": API_KEY,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

def predict_interests(features: dict):
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "input_data": [{
            "fields": list(features.keys()),
            "values": [list(features.values())]
        }]
    }

    response = requests.post(DEPLOYMENT_URL, headers=headers, json=payload)
    try:
        return response.json()["predictions"][0]["values"][0]
    except:
        return ["Data Science", "Design"]

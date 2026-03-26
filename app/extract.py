from config import API_KEY, BASE_URL, REGION_CODE, MAX_RESULTS
import requests
import json
from datetime import datetime
import time

def fetch_trending_videos(pages=2):

    all_videos = []
    next_page_token = None

    params = {
        "part": "snippet, statistics",
        "chart": "mostPopular",
        "regionCode": REGION_CODE,
        "maxResults": MAX_RESULTS,
        "key": API_KEY
    }

    for _ in range(pages):
        if next_page_token:
            params["pageToken"] = next_page_token

        response = requests.get(BASE_URL, params=params)

        if response.status_code != 200:
            raise ValueError(f"Error fetching videos: {response.status_code} - {response.text}")

        data = response.json()
        
        if "items" not in data:
            raise ValueError(f"Unexpected response format: {data}")
        
        all_videos.extend(data["items"])

        next_page_token = data.get("nextPageToken")

        if not next_page_token:
            break

        time.sleep(1) 

        return all_videos



def extract_raw_data(data):
    file_name = f"trending_videos_{datetime.now().date()}.json"

    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data extracted and saved to {file_name}")




        





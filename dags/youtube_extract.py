import requests
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://www.googleapis.com/youtube/v3/videos"

def fetch_trending_videos(region_code="IN", max_results=100):
    logger.info(f"Fetching trending videos for region: {region_code}, max_results: {max_results}")
    params = {
        "part": "snippet,statistics",
        "chart": "mostPopular",
        "regionCode": region_code,
        "maxResults": max_results,
        "key": os.getenv("YOUTUBE_API_KEY")
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        logger.info("Successfully fetched data from YouTube API")
    except requests.RequestException as e:
        logger.error(f"Failed to fetch data from YouTube API: {e}")
        raise

    data = response.json()

    videos = []

    for item in data["items"]:
        video = {
            "video_id": item["id"],
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"],
            "views": item["statistics"].get("viewCount", 0),
            "likes": item["statistics"].get("likeCount", 0),
            "comments": item["statistics"].get("commentCount", 0)
        }
        videos.append(video)

    logger.info(f"Extracted {len(videos)} videos")
    return videos


if __name__ == "__main__":
    logger.info("Starting YouTube extract script")
    try:
        vids = fetch_trending_videos()
        logger.info(f"Extracted {len(vids)} videos successfully")
        print(vids)
    except Exception as e:
        logger.error(f"Error in main: {e}")
        raise
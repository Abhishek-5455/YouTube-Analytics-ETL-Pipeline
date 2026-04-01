from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transform_videos(videos):
    logger.info(f"Starting transformation of {len(videos)} videos")
    cleaned = []

    for v in videos:
        try:
            cleaned.append({
                "video_id": v["video_id"],
                "title": v["title"].strip(),
                "channel": v["channel"].strip(),
                "published_at": datetime.fromisoformat(
                    v["published_at"].replace("Z", "")
                ),
                "views": int(v["views"]),
                "likes": int(v["likes"]),
                "comments": int(v["comments"])
            })
        except Exception as e:
            logger.warning(f"Skipping bad record: {e}")
            continue  # skip bad records

    logger.info(f"Successfully transformed {len(cleaned)} videos")
    return cleaned


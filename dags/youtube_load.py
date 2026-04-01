import psycopg2
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_to_postgres(records):
    logger.info(f"Starting load of {len(records)} records to PostgreSQL")
    try:
        conn = psycopg2.connect(
            host="postgres",   # container name
            database="airflow",
            user="airflow",
            password="airflow"
        )
        logger.info("Connected to PostgreSQL")
    except Exception as e:
        logger.error(f"Failed to connect to PostgreSQL: {e}")
        raise

    cursor = conn.cursor()

    insert_query = """
    INSERT INTO youtube_videos (
        video_id, title, channel, published_at,
        views, likes, comments
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (video_id) DO NOTHING;
    """

    inserted_count = 0
    for r in records:
        try:
            cursor.execute(insert_query, (
                r["video_id"],
                r["title"],
                r["channel"],
                r["published_at"],
                r["views"],
                r["likes"],
                r["comments"]
            ))
            inserted_count += 1
        except Exception as e:
            logger.error(f"Failed to insert record {r['video_id']}: {e}")

    try:
        conn.commit()
        logger.info(f"Committed {inserted_count} records to PostgreSQL")
    except Exception as e:
        logger.error(f"Failed to commit: {e}")
        conn.rollback()
        raise

    print("Data loaded to PostgreSQL successfully.")
    cursor.close()
    conn.close()
    logger.info("Connection closed")
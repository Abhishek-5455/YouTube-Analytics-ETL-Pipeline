import psycopg2
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_connection():
    return psycopg2.connect(
        host="postgres",
        database="youtube_analytics",
        user="airflow",
        password="airflow"
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS youtube_videos (
        video_id TEXT PRIMARY KEY,
        title TEXT,
        channel TEXT,
        published_at TIMESTAMP,
        views BIGINT,
        likes BIGINT,
        comments BIGINT,
        inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    cursor.close()
    conn.close()

def load_to_postgres(records):
    logger.info(f"Starting load of {len(records)} records to PostgreSQL")
    conn = get_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO youtube_videos (
        video_id, title, channel, published_at,
        views, likes, comments
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (video_id) DO NOTHING;
    """

    for r in records:
        cursor.execute(insert_query, (
            r["video_id"],
            r["title"],
            r["channel"],
            r["published_at"],
            r["views"],
            r["likes"],
            r["comments"]
        ))

    
    print("Data loaded to PostgreSQL successfully.")
    conn.commit()
    cursor.close()
    conn.close()
    logger.info("Connection closed")
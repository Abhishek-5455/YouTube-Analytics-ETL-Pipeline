from transform import transform_data
from extract import extract_raw_data, fetch_trending_videos

def extract_and_save_data():
    data = fetch_trending_videos(pages=4)
    extract_raw_data(data)
    print(f"Fetched {len(data)} trending videos.")

def transform_raw_data():
    raw_data = fetch_trending_videos(pages=4)
    transformed_data, category_dim, region_dim = transform_data(raw_data)

    for video in transformed_data:
        print(video)
        print("---"*50)
    
    print(f"category_dim: {category_dim}")
    print(f"region_dim: {region_dim}")


if __name__== "__main__":
    transform_raw_data()


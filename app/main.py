from extract import extract_raw_data, fetch_trending_videos

def main():
    data = fetch_trending_videos(pages=4)
    extract_raw_data(data)
    print(f"Fetched {len(data)} trending videos.")

if __name__== "__main__":
    main()


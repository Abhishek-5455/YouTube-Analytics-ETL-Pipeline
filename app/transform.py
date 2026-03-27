from schema import VideoData, CategoryDim, RegionDim

def transform_data(raw_data, region_code="IN"):
    transformed_data = []
    category = set()
    region = set()

    for item in raw_data:
        snippet = item.get("snippet", {})
        stats = item.get("statistics", {})

        video_id = item.get("id", "")
        title = snippet.get("title", "")
        published_date = snippet.get("publishedAt", "")
        channel_title = snippet.get("channelTitle", "")

        audio_language = snippet.get("defaultAudioLanguage", "")

        region_code = snippet.get("regionCode", "")
        catagory_id = snippet.get("categoryId", "")
        view_count = int(stats.get("viewCount", 0))
        like_count = int(stats.get("likeCount", 0))
        comment_count = int(stats.get("commentCount", 0))

        category.add(catagory_id)
        region.add(region_code)

        transformed_data.append(
            VideoData(
                video_id=video_id,
                title=title,
                channel_title=channel_title,
                view_count=view_count,
                like_count=like_count,
                comment_count=comment_count,
                published_date=published_date,
                catagory_id=catagory_id,
                region_code=region_code,
                audio_language=audio_language
            )
        )

    category_dim = [CategoryDim(category_id=cat) for cat in category]
    region_dim = [RegionDim(region_code=reg) for reg in region]

    return transformed_data, category_dim, region_dim


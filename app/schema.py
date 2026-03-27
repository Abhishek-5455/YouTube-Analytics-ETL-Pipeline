from dataclasses import dataclass

@dataclass
class VideoData:
    video_id: str
    title: str
    channel_title: str
    view_count: int
    like_count: int
    comment_count: int
    published_date: str
    catagory_id: str
    region_code: str
    audio_language: str


@dataclass
class CategoryDim:
    category_id: str

@dataclass
class RegionDim:
    region_code: str

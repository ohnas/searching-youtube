import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build

# load_dotenv()

# API_SERVICE_NAME = "youtube"
# API_VERSION = "v3"
# YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

# youtube = build(
#     serviceName=API_SERVICE_NAME,
#     version=API_VERSION,
#     developerKey=YOUTUBE_API_KEY,
# )

# request = youtube.search().list(
#     part="id,snippet",
#     q="아이폰 15 pro",
#     maxResults=2,
#     order="relevance",
#     regionCode="KR",
#     type="video",
#     videoCaption="closedCaption",
# )
# response = request.execute()

# videos = []
# for item in response["items"]:
#     video = {
#         id :
#     }

keyword = "아이폰"
captions = YouTubeTranscriptApi.get_transcript(video_id="rCqPL63APuc", languages=["ko"])
print(len(captions))

filter_captions = []
for caption in captions:
    if keyword in caption["text"]:
        filter_captions.append(caption)

print(filter_captions)
print(len(filter_captions))

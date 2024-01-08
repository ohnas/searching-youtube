import os
from itertools import zip_longest
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
from sheet import read_value, write_values

load_dotenv()

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")
QUERY = read_value()

youtube = build(
    serviceName=API_SERVICE_NAME,
    version=API_VERSION,
    developerKey=YOUTUBE_API_KEY,
)

request = youtube.search().list(
    part="id,snippet",
    q=QUERY,
    maxResults=5,
    order="relevance",
    regionCode="KR",
    type="video",
    videoCaption="closedCaption",
)
response = request.execute()

values = []
for item in response["items"]:
    inside_values = []
    inside_values.append(item["snippet"]["title"])
    inside_values.append(item["snippet"]["description"])
    inside_values.append(
        f'=IMAGE("{item["snippet"]["thumbnails"]["default"]["url"]}",3)'
    )
    inside_values.append(item["snippet"]["channelTitle"])
    inside_values.append(item["snippet"]["publishTime"])
    captions = YouTubeTranscriptApi.get_transcript(
        video_id=item["id"]["videoId"], languages=["ko"]
    )
    for caption in captions:
        if QUERY in caption["text"]:
            inside_values.append(caption["text"])
            inside_values.append(
                f'https://www.youtube.com/watch?v={item["id"]["videoId"]}&t={int(caption["start"])}'
            )
    values.append(inside_values)

transposed_values = list(zip_longest(*values, fillvalue=""))
write_values(transposed_values)

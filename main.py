from youtube_transcript_api import YouTubeTranscriptApi

captions = YouTubeTranscriptApi.get_transcript("p64_MLw-ios", languages=["ko"])

for caption in captions:
    print(caption)

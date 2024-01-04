from youtube_transcript_api import YouTubeTranscriptApi

captions = YouTubeTranscriptApi.get_transcript("2lAe1cqCOXo", languages=["en", "ko"])

for caption in captions:
    print(caption)

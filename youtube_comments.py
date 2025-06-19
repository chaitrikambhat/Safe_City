from googleapiclient.discovery import build
import requests
import streamlit as st

YOUTUBE_API_KEY = st.secrets["YOUTUBE_API_KEY"]
PERSPECTIVE_KEY = st.secrets["PERSPECTIVE_KEY"]

def fetch_comments(video_id, max_comments=100):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    comments = []
    next_page_token = None
    while len(comments) < max_comments:
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token
        ).execute()
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
    return comments

def score_toxicity(comment):
    url = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"
    headers = {"Content-Type": "application/json"}
    data = {
        "comment": {"text": comment},
        "languages": ["en"],
        "requestedAttributes": {"TOXICITY": {}}
    }
    response = requests.post(
        f"{url}?key={PERSPECTIVE_KEY}",
        json=data,
        headers=headers
    )
    try:
        return response.json()['attributeScores']['TOXICITY']['summaryScore']['value']
    except:
        return 0.0
from fastapi import FastAPI
from app.twitter import fetch_mentions, post_reply
from app.gpt_handler import generate_reply
from app.sentiment import analyze_sentiment

app = FastAPI()

@app.get("/check_mentions")
def check_mentions():
    mentions = fetch_mentions()
    for mention in mentions:
        tweet = mention.full_text
        sentiment, score = analyze_sentiment(tweet)
        reply = generate_reply(tweet)
        post_reply(reply, mention.id)
    return {"status": "done"}
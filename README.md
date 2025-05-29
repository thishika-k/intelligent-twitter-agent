# 🤖 Intelligent Twitter Agent

An open-source, AI-powered assistant that helps *brands and creators* respond to their audience on Twitter/X—automatically, thoughtfully, and in real-time.



# ✨ Overview

In the fast-paced world of social media, creators and brands receive hundreds of mentions, questions, and messages daily. Manual replies aren't scalable—and most bots sound robotic.

This project introduces an **Intelligent Twitter Agent** that:
- Reads mentions/comments from Twitter (or a JSON file)
- Detects sentiment of each tweet
- Crafts replies that match your **brand’s voice**
- Logs all interactions for learning and improvement

> Built 100% using open-source tools. No paid APIs. Just Python magic.


# 🧠 Features

- 🧾 Reads tweet mentions from JSON
- 😃 Sentiment detection (positive, negative, neutral)
- 🗣️ Personalized reply generation using open-source LLMs
- 📁 Interaction log for traceability and learning
- 🖥️ CLI-based demo — fast and simple
- 🔄 Easy to customize brand tone


# 🛠️ Tech Stack

| Tech/Library     | Purpose                          |
|------------------|----------------------------------|
| Python           | Core programming language        |
| TextBlob         | Sentiment analysis               |
| Transformers / GPT | Open-source text generation    |
| JSON             | Input/Output storage             |
| CLI              | Quick demo interaction           |



# 📂 Folder Structure



intelligent-twitter-agent/
├── main.py              # Main entry point
├── sentiment.py         # Sentiment analysis module
├── responder.py         # Reply generator using GPT
├── config.py            # Brand tone & templates
├── utils.py             # Helper functions
├── data/
│   └── sample\_tweets.json # Sample mentions
├── logs/
│   └── replies\_log.json   # Reply outputs
├── requirements.txt     # Python dependencies
└── README.md




# 🚀 Getting Started

1. **Clone the repository**
`bash
git clone https://github.com/your-username/intelligent-twitter-agent.git
cd intelligent-twitter-agent
`

2. **Create a virtual environment**

`bash
python -m venv venv
venv\Scripts\activate  # For Windows
# source venv/bin/activate  # For Mac/Linux
`

3. **Install dependencies**

``bash
pip install -r requirements.txt
``

4. **Run the agent**

``bash
python main.py
``



# 🧪 Sample Run

* The agent reads tweets from `data/sample_tweets.json`
* Analyzes each tweet’s sentiment
* Generates and logs personalized replies to `logs/replies_log.json`


# 📌 Customization

To change the tone of replies:

* Open `config.py`
* Modify the `BRAND_TONE_PROMPT` template
* You can also adjust keywords or predefined tone templates



# 🔮 Future Enhancements

[ ] Twitter API Integration for live mentions
[ ] Web dashboard to track replies
[ ] Brand tone selector UI
[ ] Fine-tuned sentiment model
[ ] Feedback loop to improve reply accuracy



# 🙌 Author

*Thishika K*
Built as part of a hackathon challenge
Made with 💡, ☕, and Open Source


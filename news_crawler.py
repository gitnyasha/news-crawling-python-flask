from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from scrapingbee import ScrapingBeeClient
from datetime import datetime
from pytz import utc

app = Flask(__name__)
scheduler = BackgroundScheduler(timezone=utc)

client = ScrapingBeeClient(api_key='YOUR_API_KEY')

cnn_url = 'https://edition.cnn.com/business'
cnn_extract_rules = {
    "headlines": {
            "selector": ".container_lead-plus-headlines__headline span",
            "type": "list",
            "output": "text"
        }
}

yahoo_url = 'https://sports.yahoo.com/'
yahoo_extract_rules = {
    "headlines": {
        "selector": "h3 a",
        "type": "list",
        "output": "text"
    }
}

nbc_url = 'https://www.nbcnews.com/tech-media'
nbc_extract_rules = {
    "headlines": {
        "selector": ".styles_headline__ice3t a",
        "type": "list",
        "output": "text"
    }
}

cnn_headlines = []
nbc_headlines = []
yahoo_headlines = []

def get_headlines(url, extract_rules):
    response = client.get(url, params={"extract_rules": extract_rules})
    data = response.json()
    headlines = data["headlines"]
    return headlines

def run_crawling():
    global cnn_headlines, nbc_headlines, yahoo_headlines

    with app.app_context():
        cnn_headlines = get_headlines(cnn_url, cnn_extract_rules)
        nbc_headlines = get_headlines(nbc_url, nbc_extract_rules)
        yahoo_headlines = get_headlines(yahoo_url, yahoo_extract_rules)

has_run_crawling_onstartup = False

@app.before_request
def crawling_onstartup():
    global has_run_crawling_onstartup
    if not has_run_crawling_onstartup:
        run_crawling()
        has_run_crawling_onstartup = True

@app.route('/')
def display_news():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('news.html', cnn_headlines=cnn_headlines, nbc_headlines=nbc_headlines, yahoo_headlines=yahoo_headlines, timestamp=timestamp)


if __name__ == "__main__":
    scheduler.add_job(run_crawling, 'interval', minutes=1)
    scheduler.start()

    app.run()


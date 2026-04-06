from collector import fetch_news
from analytics import summarize_articles, analyze_war_trends, forecast_war_end
from reporter import generate_report
from telegram_sender import send_to_telegram

def run():
    war = fetch_news("війна Україна", 30)
    oil = fetch_news("ціни на нафту", 20)
    all_news = war + oil

    top_news = summarize_articles(all_news)
    trend = analyze_war_trends(all_news)
    forecast = forecast_war_end(all_news)

    report = generate_report(top_news, trend, forecast)
    send_to_telegram(report)

if __name__ == "__main__":
    run()

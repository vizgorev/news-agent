from gnews import GNews

def fetch_news(query, max_results=20):
    google_news = GNews(language='uk', country='UA', max_results=max_results)
    return google_news.get_news(query)

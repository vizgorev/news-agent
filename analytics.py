def summarize_articles(articles, top_n=10):
    lines = []
    for a in articles[:top_n]:
        lines.append(f"- {a.get('title')} ({a.get('source')})")
    return "\n".join(lines)


def analyze_war_trends(articles):
    pos = 0
    neg = 0

    for a in articles:
        t = a.get("title", "").lower()
        if any(x in t for x in ["успіх", "санкції", "допомога", "контрнаступ"]):
            pos += 1
        if any(x in t for x in ["атака", "удар", "ескалація", "ракета"]):
            neg += 1

    if pos > neg:
        return "Новини сьогодні більше позитивні для України."
    elif neg > pos:
        return "Новини сьогодні вказують на ускладнення ситуації."
    else:
        return "Баланс позитивних і негативних новин нейтральний."


def forecast_war_end(articles):
    pos = 0
    neg = 0

    for a in articles:
        t = a.get("title", "").lower()
        if any(x in t for x in ["допомога", "санкції", "успіх"]):
            pos += 1
        if any(x in t for x in ["ескалація", "мобілізація", "удар"]):
            neg += 1

    base12 = 0.30
    base24 = 0.60
    delta = (pos - neg) * 0.01

    return {
        "12m": round((base12 + delta) * 100, 1),
        "24m": round((base24 + delta) * 100, 1)
    }

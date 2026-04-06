def generate_report(top_news, trend, forecast):
    return f"""
# 📰 Дайджест новин

## 🔟 Топ-10 новин
{top_news}

## 📊 Аналітика
{trend}

## 🔮 Прогноз завершення війни
- 12 місяців: {forecast['12m']}%
- 24 місяці: {forecast['24m']}%

Звіт згенеровано автоматично GitHub Actions.
"""

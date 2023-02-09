from datetime import datetime
from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    list = []

    for element in news:
        list.append((element["title"], element["url"]))
    return list


# Requisito 8
def search_by_date(date):
    try:
        news_info = []
        format_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")

        for e in search_news({"timestamp": format_date}):
            news_info.append((e["title"], e["url"]))
        return news_info
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

import requests
import time
import parsel
import re


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if res.status_code == 200:
            return res.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = parsel.Selector(html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    next_url = selector.css("a.next::attr(href)").get()
    if next_url:
        return next_url
    return None


# Requisito 4
def scrape_news(html_content):
    selector = parsel.Selector(html_content)
    return {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "reading_time": int(re.findall(
            r"\d+", selector.css("li.meta-reading-time::text").get()
        )[0]),
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip(),
        "category": selector.css(".category-style span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

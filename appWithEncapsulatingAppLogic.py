from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from milestone_4_Quote_scraper_with_Selenium.pages.quotes_page import QuotesPage, InvalidAuthorError, \
    InvalidTagForAuthorError

chrome = ""


def tear_down():
    if chrome:
        chrome.quit()


try:
    required_author = input("Please enter an author: ")
    required_tag = input("Please enter a tag: ")

    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome.get("https://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)

    for quote in page.search_for_quotes(required_author, required_tag):
        print(quote)
    tear_down()
except InvalidTagForAuthorError as e:
    tear_down()
    print(e)
except InvalidAuthorError as e:
    tear_down()
    print(e)
except Exception as e:
    tear_down()
    print(e)
    print("An unknown error occurred. Please try again.")

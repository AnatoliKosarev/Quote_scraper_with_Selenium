from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from milestone_4_Quote_scraper_with_Selenium.pages.quotes_page import QuotesPage, InvalidTagForAuthorError, \
    InvalidAuthorError

MENU_MESSAGE = "Enter the author you'd like to get the quotes of or enter 'q' to exit: "
chrome = webdriver.Chrome(ChromeDriverManager().install())
# chrome = webdriver.Chrome(executable_path=r"C:\Users\kosarau\Documents\Drivers\chromedriver.exe")
chrome.get("https://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)


def tear_down():
    if chrome:
        chrome.quit()


def menu():
    required_author = input(MENU_MESSAGE)
    while required_author != "q":
        try:
            page.select_author(required_author)
            available_tags = page.get_available_tags()
            print(f"Select one of these tags: {' | '.join(available_tags)}.")
            selected_tag = input("Choose your tag: ")
            page.select_tag(selected_tag)
            page.search_button.click()
            for quote in page.quotes:
                print(quote)
            break
        except InvalidAuthorError as e:
            print(e)
            required_author = input(MENU_MESSAGE)
        except InvalidTagForAuthorError as e:
            tear_down()
            print(e)
            break
        except Exception as e:
            tear_down()
            print(e)
            print("An unknown error occurred. Please try again.")
            break
    tear_down()


menu()

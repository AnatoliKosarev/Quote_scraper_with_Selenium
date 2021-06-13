from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from milestone_4_Quote_scraper_with_Selenium.pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(ChromeDriverManager().install())
# chrome = webdriver.Chrome(executable_path=r"C:\Users\kosarau\Documents\Drivers\chromedriver.exe")
chrome.get("https://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)

required_author = input("Enter the author you'd like to get the quotes of: ")
page.select_author(required_author)

available_tags = page.get_available_tags()
print(f"Select one of these tags: {' | '.join(available_tags)}.")
selected_tag = input("Choose your tag: ")
page.select_tag(selected_tag)
page.press_search_button()

for quote in page.quotes:
    print(quote)

chrome.quit()
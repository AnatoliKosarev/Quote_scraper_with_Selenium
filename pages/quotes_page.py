from typing import List

from selenium.webdriver.support.ui import Select

from milestone_4_Quote_scraper_with_Selenium.locators.quote_page_locators import QuotePageLocators
from milestone_4_Quote_scraper_with_Selenium.parsers.quote_parser import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def author_dropdown(self) -> Select:
        locator = QuotePageLocators.AUTHOR_SELECTOR
        element = self.browser.find_element_by_css_selector(locator)
        return Select(element)  # gives element methods for interacting with dropdowns

    @property
    def tags_dropdown(self) -> Select:
        locator = QuotePageLocators.TAG_SELECTOR
        element = self.browser.find_element_by_css_selector(locator)
        return Select(element)

    @property
    def quotes(self) -> List[QuoteParser]:
        locator = QuotePageLocators.QUOTE
        quotes = self.browser.find_elements_by_css_selector(locator)
        return [QuoteParser(quote) for quote in quotes]

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def select_tag(self, tag_name: str):
        self.tags_dropdown.select_by_visible_text(tag_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]

    def press_search_button(self):
        locator = QuotePageLocators.SEARCH_BUTTON
        self.browser.find_element_by_css_selector(locator).click()

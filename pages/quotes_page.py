from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from milestone_4_Quote_scraper_with_Selenium.locators.quote_page_locators import QuotePageLocators
from milestone_4_Quote_scraper_with_Selenium.parsers.quote_parser import QuoteParser
from milestone_4_Quote_scraper_with_Selenium.waits.wait import Wait


class InvalidTagForAuthorError(ValueError):
    pass


class InvalidAuthorError(ValueError):
    pass


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = Wait(browser)

    @property
    def author_dropdown(self) -> Select:
        locator = QuotePageLocators.AUTHOR_SELECTOR
        self.wait.until_element_is_present(locator)
        element = self.browser.find_element_by_css_selector(locator)
        return Select(element)  # gives element methods for interacting with dropdowns

    @property
    def tags_dropdown(self) -> Select:
        locator = QuotePageLocators.TAG_SELECTOR
        self.wait.until_element_is_present(locator)
        element = self.browser.find_element_by_css_selector(locator)
        return Select(element)

    @property
    def search_button(self):
        locator = QuotePageLocators.SEARCH_BUTTON
        self.wait.until_element_is_present(locator)
        return self.browser.find_element_by_css_selector(locator)

    @property
    def quotes(self) -> List[QuoteParser]:
        locator = QuotePageLocators.QUOTE
        self.wait.until_element_is_present(locator)
        quotes = self.browser.find_elements_by_css_selector(locator)
        return [QuoteParser(quote) for quote in quotes]

    def select_author(self, author_name: str):
        try:
            self.author_dropdown.select_by_visible_text(author_name)
        except NoSuchElementException:
            raise InvalidAuthorError(f"Author '{author_name}' is not found.")

    def select_tag(self, tag_name: str):
        try:
            self.wait.until_element_is_present(QuotePageLocators.TAG_SELECTOR_VALUE_OPTION)
            self.tags_dropdown.select_by_visible_text(tag_name)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(f"Selected author does not have quotes tagged with '{tag_name}'.")

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]

    def search_for_quotes(self, author: str, tag: str) -> List[QuoteParser]:
        self.select_author(author)
        self.select_tag(tag)
        self.search_button.click()
        return self.quotes

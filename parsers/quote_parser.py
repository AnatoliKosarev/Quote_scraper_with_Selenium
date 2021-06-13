from milestone_4_Quote_scraper_with_Selenium.locators.quote_locators import QuoteLocators


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        tag = "tags" if len(self.tags) > 1 else "tag"
        return f"""
        Quote: {self.quote_text},
        by {self.author},
        with {tag}: {str(self.tags).strip('[]')}."""  # with {tag}: '{"', '".join(self.tags)}'."""

    @property
    def quote_text(self):
        locator = QuoteLocators.QUOTE_TEXT
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [q.text for q in self.parent.find_elements_by_css_selector(locator)]

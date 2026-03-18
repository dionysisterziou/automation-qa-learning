from playwright.sync_api import Page


def test_homepage_has_expected_title(page: Page):
    page.goto("https://example.com")

    assert page.title() == "Example Domain"
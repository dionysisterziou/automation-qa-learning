from playwright.sync_api import Page, expect
from config import BASE_URL


def test_homepage_has_expected_title(page: Page):
    page.goto(BASE_URL)

    assert page.title() == "Example Domain"
    expect(page.get_by_role("heading", name="Example Domain")).to_be_visible()


def test_homepage_link_redirects(page: Page):
    page.goto(BASE_URL)
    page.get_by_text("Learn more").click()
    page.wait_for_url("**iana.org**")

    assert "iana.org" in page.url
from playwright.sync_api import Page, expect
from test_data import LEARN_MORE_TEXT, IANA_HEADING, HOMEPAGE_HEADING


def test_homepage_has_expected_title(homepage: Page):
    expect(homepage.get_by_role("heading", name=HOMEPAGE_HEADING)).to_be_visible()


def test_homepage_link_redirects_to_iana(homepage: Page):
    homepage.get_by_text(LEARN_MORE_TEXT).click()
    homepage.wait_for_url("**iana.org**")
    expect(homepage.get_by_role("heading", name=IANA_HEADING)).to_be_visible()

    assert "iana.org" in homepage.url
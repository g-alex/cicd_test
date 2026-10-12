from playwright.sync_api import Page, expect
import re

def test_open_page(page: Page):
    page.goto('https://www.selenium.dev/selenium/web/web-form.html')
    submit_button = page.get_by_role("button", name='submit')
    submit_button.click()
    expect(page).to_have_url(re.compile('submitted-form.html'))


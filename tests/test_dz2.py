from playwright.sync_api import Page, expect

def test_input_value(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    text_field = page.locator('#id_text_string')
    text_field.fill('123')
    text_field.press('Enter')

    text_title = page.locator('[id="result-text"]')
    expect(text_title).to_have_text('123')



# Открой https://the-internet.herokuapp.com/inputs, введи в поле число и проверь,
# что поле его действительно приняло. Заведи проект на GitLab, положи тест и .gitlab-ci.yml.
# Сдача: ссылка на зелёный pipeline + текст .gitlab-ci.yml + скажи,
# чем процесс отличался от GitHub.
from playwright.sync_api import Page, expect
import re

def test_open_page(page: Page):
    page.goto('https://the-internet.herokuapp.com/status_codes')
    title_200 = page.locator('[href="status_codes/200"]')
    title_200.click()
    expect(page).to_have_url(re.compile('status_codes/200'))

# Открой https://the-internet.herokuapp.com/status_codes, кликни ссылку 200, проверь,
# что браузер оказался там, где ожидалось. Один и тот же репозиторий подключи к обоим
# сервисам (GitHub + GitLab). Настрой ручной запуск на каждой платформе и чтобы
# после прогона сохранялся артефакт с результатами. Сдача: ссылка на ручной прогон
# на GitHub + ссылка на ручной pipeline на GitLab + список того, что пришлось сделать
# по-разному на двух платформах (это самая важная часть!).
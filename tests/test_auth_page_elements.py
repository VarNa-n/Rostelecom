# Тесты группы "Форма ввода логина и пароля" - проверка наличия требуемых элементов на странице авторизации https://b2c.passport.rt.ru/
import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from pages.setting import ad_slogan
from pages.setting import *


def test_tab_phone(web_browser):
    """ Тест-кейс FT-001: проверка наличия таба Телефон на странице авторизации """

    page = AuthPage(web_browser)

    # Переходим на таб Телефон
    page.swich_tab(page.tab_phone)
    print(page.title_username.text)
    assert page.title_username.text == u"Мобильный телефон", "Таб Телефон не найден"


def test_tab_email(web_browser):
    """ Тест-кейс FT-002: проверка наличия таба Почта на странице авторизации """

    page = AuthPage(web_browser)

    # Переходим на таб Почта
    page.swich_tab(page.tab_email)
    print(page.title_username.text)
    assert page.title_username.text == u"Электронная почта", "Таб Почта не найден"


def test_tab_login(web_browser):
    """ Тест-кейс FT-003: проверка наличия таба Логин на странице авторизации """

    page = AuthPage(web_browser)

    # Переходим на таб Логин
    page.swich_tab(page.tab_login)
    print(page.title_username.text)
    assert page.title_username.text == u"Логин", "Таб Логин не найден"


def test_tab_ls(web_browser):
    """ Тест-кейс FT-004: проверка наличия таба Лицевой счет на странице авторизации """

    page = AuthPage(web_browser)

    # Переходим на таб Лицевой счет
    page.swich_tab(page.tab_ls)
    print(page.title_username.text)
    assert page.title_username.text == u"Лицевой счёт", "Таб Лицевой счет не найден"


def test_input_field(web_browser):
    """ Тест-кейс FT-005: проверка наличия полей ввода username и пароля на странице авторизации """

    page = AuthPage(web_browser)

    # Есть поле ввода логина
    assert page.username, "Нет поля ввода username"
    # Есть поле ввода пароля
    assert page.password, "Нет поля ввода пароля"
    # Есть кнопка "Войти"
    assert page.btn, "Нет кнопки 'Войти'"


def test_ad_slogan(web_browser):
    """ Тест-кейс FT-006: проверка наличия слогана на странице авторизации """

    page = AuthPage(web_browser)

    assert ad_slogan in page.ad_slogan.text, f"Нет слогана {ad_slogan}"


@pytest.mark.parametrize(("username, tab_title"),
                            [
                                (valid_email, u"Почта"),
                                #(valid_login, u"Логин"),
                                #(valid_ls, u"Лицевой счёт"),
                                (valid_phone, u"Телефон")
                            ],
                            ids= [
                                'By email',
                                #'By login',
                                #"By LS",
                                "By phone"]
                         )
def test_auto_switch_tab(username, tab_title, web_browser):
    """ Тест-кейс FT-007: авторизация по любому username без смены таба """

    page = AuthPage(web_browser)

    # Табы
    #tabs = (u"Телефон", u"Почта", u"Логин", u"Лицевой счёт")
    tabs = ("tab_phone", "tab_email", "tab_login", "tab_ls")
    # Флаги переключения таба
    tab_flag = []

    # Переходим на каждый таб
    for tab in tabs:
        get_tab = getattr(page, tab)
        page.swich_tab(get_tab)
        # Очистим логин
        page.enter_username('')
        # Вводим логин
        page.enter_username(username)
        # Кликаем на пароль
        page.password.click()

        time.sleep(5)

        # Если таб не переключился
        active_tab = web_browser.find_element(By.CSS_SELECTOR, "div.rt-tab--active").text
        print(f"\n{tab} -> {active_tab} == {tab_title}")

        if active_tab != tab_title:
            tab_flag.append(0)
        else:
            tab_flag.append(1)

    for i in range(len(tab_flag)-1):
        print(f"{i}) {tabs[i]} = {tab_flag[i]}\n")
        # Проверка, что таб переключился
        assert tab_flag[i] == 1, f"{username} error on {tabs[i]} \n"

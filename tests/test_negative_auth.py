# Тесты группы "Авторизация. Негативные тесты" - вход в ЛК

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from pages.setting import *
import time


@pytest.mark.parametrize("phone", ['', ' '], ids= ["Empty phone", "Space phone"])
def test_auth_by_empty_phone(phone, web_browser):
    """ Тест-кейс AT-006: попытка авторизации с пустым номером телефона """

    page = AuthPage(web_browser)

    # Переходим на таб Мобильный телефон
    page.swich_tab(page.tab_phone)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(phone)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Введите номер телефона"
    assert web_browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error").text == 'Введите номер телефона'


@pytest.mark.parametrize("username, passwd", [
                            (valid_phone, ''),
                            (valid_phone, ' '),
                            (valid_email, ''),
                            (valid_email, ' '),
                            (valid_login, ''),
                            (valid_login, ' '),
                            (valid_ls, ''),
                            (valid_ls, ' ')
                        ], ids= [
                            "Phone: Empty password",
                            "Phone: Space password",
                            "Email: Empty password",
                            "Email: Space password",
                            "Login: Empty password",
                            "Login: Space password",
                            "LS: Empty password",
                            "LS: Space password"
                        ])
@pytest.mark.xfail(reason="Нереализовано")
def test_auth_by_phone_and_empty_password(username, passwd, web_browser):
    """ Тест-кейс AT-007 и AT-012: попытка авторизации с пустым паролем """

    page = AuthPage(web_browser)

    # Вводим логин/пароль
    page.enter_username(username)
    page.enter_pass(passwd)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Введите пароль"
    assert web_browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error").text == 'Введите пароль', "Нет вывода сообщения 'Введите пароль'"


@pytest.mark.parametrize("username", [
                                '+7(999)9999999',
                                "romashka2003@gmail.com"
                            ], ids= [
                                "Wrong phone number",
                                "Wrong email"
                            ]
                         )
def test_auth_by_wrong_phone(username, web_browser):
    """ Тест-кейс AT-008 и AT-014: попытка авторизации неверным username и верным паролем"""

    page = AuthPage(web_browser)

    # Вводим логин/пароль
    page.enter_username(username)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        print("Captcha!!!")
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Неверный логин или пароль"
    assert web_browser.find_element(By.ID, "form-error-message").text == 'Неверный логин или пароль'


@pytest.mark.parametrize("username, passwd", [
                            (valid_phone, 'hjvfirf2003'),
                            (valid_email, 'hjvfirf2003'),
                        ], ids= [
                            "Phone: Wrong password",
                            "Email: Wrong password",
                        ])
def test_auth_by_wrong_password(username, passwd, web_browser):
    """ Тест-кейс AT-009 и AT-013: попытка авторизации верным username и неверным паролем"""

    page = AuthPage(web_browser)

    # Вводим логин/пароль
    page.enter_username(username)
    page.enter_pass(passwd)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        print("Captcha!!!")
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Неверный логин или пароль"
    assert web_browser.find_element(By.ID, "form-error-message").text == 'Неверный логин или пароль'

@pytest.mark.parametrize("phone", ['+7(977)561260'], ids= ["Not correct numb"])
def test_auth_by_bad_format_phone(phone, web_browser):
    """ Тест-кейс AT-010: попытка авторизации по номеру телефона в неверном формате"""

    page = AuthPage(web_browser)

    # Переходим на таб Мобильный телефон
    page.swich_tab(page.tab_phone)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(phone)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Введите номер телефона"
    assert web_browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error").text == 'Неверный формат телефона'


@pytest.mark.parametrize("email", ['', ' '], ids= ["Empty email", "Space email"])
def test_auth_by_empty_email(email, web_browser):
    """ Тест-кейс AT-011: попытка авторизации с пустым адресом электронной почты """

    page = AuthPage(web_browser)

    # Переходим на таб Почта
    page.swich_tab(page.tab_email)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(email)
    page.enter_pass(valid_password)

    # Если есть капча, делаем задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Введите адрес, указанный при регистрации"
    assert web_browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error").text == 'Введите адрес, указанный при регистрации'


@pytest.mark.parametrize("email", ['romashkacool2003@gmail'], ids= ["Not correct email"])
def test_auth_by_bad_format_phone(email, web_browser):
    """ Тест-кейс AT-015: попытка авторизации по емейлу в неверном формате"""

    page = AuthPage(web_browser)

    # Переходим на таб Почта
    page.swich_tab(page.tab_email)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(email)
    page.enter_pass(valid_password)

    # Проверка перехода на таб "Логин"
    assert web_browser.find_element(By.CSS_SELECTOR, "div.rt-tab.rt-tab--small.rt-tab--active").text == 'Логин'


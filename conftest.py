#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is example shows how we can manage failed tests
# and make screenshots after any failed test case.

import pytest
from selenium import webdriver
from pages.setting import drv_path


@pytest.fixture()
def web_browser(request):

    browser = webdriver.Chrome(drv_path)
    browser.set_window_size(1400, 1000)

    # Return browser instance to test case:
    yield browser

    browser.quit()

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

# from selenium.webdriver.firefox.service import Service

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        print("firefox browser")
    elif browser_name == "safari":
        print("Safari browser")

    request.cls.driver = driver
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    # URL : https://rahulshettyacademy.com/angularpractice/
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    # browser invocation command : pytest --browser_name chrome


# @pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extras.append(pytest_html.extras.html(html))
        report.extras = extras


# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)
def _capture_screenshot(name):
    screenshot_folder = "../screenshots"
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)
    screenshot_path = os.path.join(screenshot_folder, name)
    driver.get_screenshot_as_file(screenshot_path)

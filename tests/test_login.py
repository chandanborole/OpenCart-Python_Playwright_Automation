from playwright.sync_api import Page
from OpenCart.pageobject.login import Login
from OpenCart.config import Config

# To verify new user registration

def test_valid_login(page:Page):

    page.goto("https://tutorialsninja.com/demo/")

    # Create Page Object
    login_page = Login(page)
    config_data = Config

    # Navigate to login page
    login_page.click_myaccount()
    login_page.click_login_link()

    # Fill User ID / Password
    login_page.user_email_address(config_data.email)
    login_page.user_password(config_data.password)
    login_page.click_login_button()

def test_invalid_login(page:Page):

    page.goto("https://tutorialsninja.com/demo/")

    # Create Page Object
    login_page = Login(page)
    config_data = Config

    # Navigate to login page
    login_page.click_myaccount()
    login_page.click_login_link()

    # Fill User ID / Password
    login_page.user_email_address(config_data.invalid_email)
    login_page.user_password(config_data.invalid_password)
    login_page.click_login_button()

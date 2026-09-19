from playwright.sync_api import Page
from OpenCart.pageobject.login import Login
from OpenCart.config import Config

# To verify new user registration

def test_login(page:Page):

    page.goto("https://tutorialsninja.com/demo/")

    # Create Page Object
    login_page = Login(page)
    config_data = Config

    # Navigate to login page
    login_page.click_myaccount()
    login_page.click_login_link()

    # Fill User ID / Password
    login_page.set_email_address(config_data.email)
    login_page.set_password(config_data.password)
    login_page.click_login_button()
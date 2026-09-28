from playwright.sync_api import Page , expect
from OpenCart.pageobject.logout import (Logout)
from OpenCart.config import Config

def test_0016_validate_user_logout(page:Page):

    """
    To validate - User logout
    """

    # Browse URL
    page.goto(Config.base_url)

    # Create Page Object
    logout_page = Logout(page)
    config_data = Config

    # Navigate to login page
    logout_page.click_myaccount()
    logout_page.click_login_link()

    # Fill User ID / Password
    logout_page.user_email_address(config_data.valid_register_email)
    logout_page.user_password(config_data.valid_register_password)
    logout_page.click_login_button()

    # Verify title after login
    title_after_valid_login = logout_page.verify_title_after_logout()
    expect(title_after_valid_login).to_have_title("My Account")

    # Navigate to My Account and click Logout
    logout_page.click_my_account_after_login()
    logout_page.click_logout_link()

    # Click continue button
    logout_page.click_continue_after_logout()

    # Verify title after logout
    title_after_logout = logout_page.verify_title_after_logout()
    expect(title_after_logout).to_have_title("My Account")
from playwright.sync_api import Page , expect
from OpenCart.pageobject.logout import (Logout)
from OpenCart.config import Config

def test_0016_validate_user_logout(page:Page):

    """
    To validate - User logout
    """

    # Browse URL
    page.goto(Config.valid_base_url)

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


def test_0017_validate_user_logout_from_right_column_options(page:Page):

    """
    To validate - User logout from Right Column options
    """

    # Browse URL
    page.goto(Config.valid_base_url)

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

    # Navigate to click Logout from Right Column
    logout_page.click_logout_from_right_column()

    # Click continue button
    logout_page.click_continue_after_logout()

    # Verify title after logout
    title_after_logout_from_right_column_options = logout_page.verify_title_after_logout_from_right_column_options()
    expect(title_after_logout_from_right_column_options).to_have_title("Your Store")
from playwright.sync_api import Page , expect
from OpenCart.pageobject.login import Login
from OpenCart.config import Config

def test_0009_validate_user_login_with_valid_input(page:Page):

    """
    To validate - User login with valid input
    """

    # Browse URL
    page.goto(Config.valid_base_url)

    # Create Page Object
    login_page = Login(page)
    config_data = Config

    # Navigate to login page
    login_page.click_myaccount()
    login_page.click_login_link()

    # Fill User ID / Password
    login_page.user_email_address(config_data.valid_register_email)
    login_page.user_password(config_data.valid_register_password)
    login_page.click_login_button()

    # Verify title after login
    title_after_valid_login = login_page.verify_title_after_valid_login()
    expect(title_after_valid_login).to_have_title("My Account")


def test_0010_validate_user_login_with_invalid_input(page:Page):

    """
    To validate - User login with invalid input
    Provide Invalid - email & password
    """

    # Browse URL
    page.goto(Config.valid_base_url)

    # Create Page Object
    login_page = Login(page)
    config_data = Config

    # Navigate to login page
    login_page.click_myaccount()
    login_page.click_login_link()

    # Fill User ID / Password
    login_page.user_email_address(config_data.invalid_login_username)
    login_page.user_password(config_data.invalid_login_password)
    login_page.click_login_button()

    # Verify warning message
    invalid_login_warning_message = login_page.invalid_login_warning_message()
    expect(invalid_login_warning_message).to_have_text("Warning: No match for E-Mail Address and/or Password.")


def test_0011_validate_warning_for_exceeded_login_attempts(page:Page):

    """
    To Validate - Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.
    """

    # Browse URL
    page.goto(Config.valid_base_url)

    # Create Page Object
    login_page = Login(page)
    config_data = Config

    # Navigate to login page
    login_page.click_myaccount()
    login_page.click_login_link()

    # Fill User ID / Password
    login_page.user_email_address(config_data.valid_register_email)
    login_page.user_password(config_data.valid_register_password)
    login_page.click_login_button()

    # Verify title after login
    exceeded_login_attempts_warning_message = login_page.exceeded_login_attempts_warning_message()
    expect(exceeded_login_attempts_warning_message).to_have_title("My Account")


def test_0012_validate_user_login_with_invalid_email_valid_password(page:Page):

    """
    To validate - User login with invalid input (Invalid email address and valid Password)
    """

    # Browse URL
    page.goto(Config.valid_base_url)

    # Create Page Object
    login_page = Login(page)
    config_data = Config

    # Navigate to login page
    login_page.click_myaccount()
    login_page.click_login_link()

    # Fill User ID / Password
    login_page.user_email_address(config_data.invalid_login_username)
    login_page.user_password(config_data.invalid_login_password)
    login_page.click_login_button()

    # Verify warning message
    validate_user_login_with_invalid_email_valid_password = login_page.invalid_login_warning_message()
    expect(validate_user_login_with_invalid_email_valid_password).to_have_text("Warning: No match for E-Mail Address and/or Password.")


def test_0013_validate_user_login_with_valid_email_invalid_password(page:Page):

    """
    To validate - User login with invalid input (Valid email address and Invalid Password)
    """

    # Browse URL
    page.goto(Config.valid_base_url)

    # Create Page Object
    login_page = Login(page)
    config_data = Config

    # Navigate to login page
    login_page.click_myaccount()
    login_page.click_login_link()

    # Fill User ID / Password
    login_page.user_email_address(config_data.valid_register_email)
    login_page.user_password(config_data.invalid_login_password)
    login_page.click_login_button()

    # Verify warning message
    validate_user_login_with_invalid_email_valid_password = login_page.invalid_login_warning_message()
    expect(validate_user_login_with_invalid_email_valid_password).to_have_text("Warning: No match for E-Mail Address and/or Password.")


def test_0014_validate_user_login_without_any_credentials(page:Page):

    """
    To validate - User login without providing any credentials
    """

    # Browse URL
    page.goto(Config.valid_base_url)

    # Create Page Object
    login_page = Login(page)
    config_data = Config

    # Navigate to login page
    login_page.click_myaccount()
    login_page.click_login_link()

    # Fill User ID / Password
    login_page.user_email_address(config_data.invalid_blank_email_address)
    login_page.user_password(config_data.invalid_blank_password)
    login_page.click_login_button()

    # Verify warning message
    validate_user_login_with_invalid_email_valid_password = login_page.invalid_login_warning_message()
    expect(validate_user_login_with_invalid_email_valid_password).to_have_text("Warning: No match for E-Mail Address and/or Password.")


def test_0015_forgotten_password_hyperlink_should_clickable(page:Page):

    """
    To validate - Forgotten Password hyperlink should be clickable
    """

    # Browse URL
    page.goto(Config.valid_base_url)

    # Create Page Object
    login_page = Login(page)

    # Navigate to login page
    login_page.click_myaccount()
    login_page.click_login_link()

    # Click on Forgotten Password hyperlink
    login_page.click_forgotten_password_hyperlink()

    # Verify title after clicking on Forgotten Password hyperlink
    title_forgot_your_password = login_page.verify_title_forgot_your_password()
    expect(title_forgot_your_password).to_have_title("Forgot Your Password")
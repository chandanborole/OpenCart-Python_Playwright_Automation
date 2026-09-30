from playwright.sync_api import Page , expect
from OpenCart.pageobject.forgot_password import ForgotPassword
from OpenCart.config import Config

def test_forgot_password(page:Page):

    page.goto("https://tutorialsninja.com/demo/")

    # Create page object
    forgot_password = ForgotPassword(page)
    config_data = Config()

    # Navigate to login page and perform process for forgot password
    forgot_password.click_myaccount()
    forgot_password.click_login_link()
    forgot_password.click_forgotten_password()
    forgot_password.provide_email_address(config_data.email_get_by_label)
    forgot_password.click_continue_button()

    # Verify Edit Confirmation and Validation
    success_message = forgot_password.confirmation_message()
    expect(success_message).to_have_text("An email with a confirmation link has been sent your email address.")
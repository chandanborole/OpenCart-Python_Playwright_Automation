from playwright.sync_api import Page , expect
from OpenCart.pageobject.edit_your_account_information import EditYourAccountInformation
from OpenCart.config import Config

def test_edit_your_account_information(page:Page):

    page.goto("https://tutorialsninja.com/demo/")

    # Create Page Object
    edit_account_info = EditYourAccountInformation(page)
    config_data = Config()

    # Navigate to login page
    edit_account_info.click_myaccount()
    edit_account_info.click_login_link()
    edit_account_info.user_email_address(config_data.email)
    edit_account_info.user_password(config_data.password)
    edit_account_info.click_login_button()

    # Click Edit
    edit_account_info.click_edit()

    # Update Details
    edit_account_info.set_firstname(config_data.edit_firstname)
    edit_account_info.set_lastname(config_data.edit_lastname)
    edit_account_info.set_telephone(config_data.edit_telephone)
    edit_account_info.click_continue_button()

    # Verify Edit Confirmation and Validation
    edit_success_message = edit_account_info.edit_confirmation_success_message()
    expect(edit_success_message).to_have_text("Success: Your account has been successfully updated.")
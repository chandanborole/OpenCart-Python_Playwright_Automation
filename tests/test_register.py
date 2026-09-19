from playwright.sync_api import Page , expect
from OpenCart.pageobject.register import Register
from OpenCart.pageobject.homepage import HomePage
from OpenCart.utilities.random_data_util import RandomDataGenerator
from OpenCart.config import Config

# To verify new user registration

def test_new_user_registration(page:Page):

    page.goto("https://tutorialsninja.com/demo/")

    # Create Page Object
    home_page = HomePage(page)
    register_page = Register(page)
    random_data = RandomDataGenerator()

    # Navigate to registration page
    home_page.click_myaccount()
    home_page.click_register()

    # Fill Registration Form
    register_page.set_firstname(random_data.get_first_name())
    register_page.set_lastname(random_data.get_last_name())
    register_page.set_email(random_data.get_email())
    register_page.set_telephone(random_data.get_phone_number())
    password = random_data.get_password()
    register_page.set_password(password)
    register_page.set_confirm_password(password)

    # Accept Privacy Policy and Submit
    register_page.click_privacy_policy_checkbox()
    register_page.click_continue_button()

    # Verify Account Creation Confirmation and Validation
    registration_success_message = register_page.registration_confirmation_success_message()
    expect(registration_success_message).to_have_text("Your Account Has Been Created!")
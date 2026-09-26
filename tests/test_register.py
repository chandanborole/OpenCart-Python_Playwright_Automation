import pytest
from playwright.sync_api import Page , expect
from OpenCart.pageobject.register import Register
from OpenCart.pageobject.homepage import HomePage
from OpenCart.utilities.random_data_util import RandomDataGenerator
from OpenCart.config import Config

def test_0001_to_validate_application_url(page:Page):

    """
    To validate - Application URL
    """

    # Browse URL
    page.goto(Config.base_url)


def test_0002_new_user_registration_valid_inputs(page:Page):

    """
    To validate - New user registration with valid input
    """

    # Browse URL
    page.goto(Config.base_url)

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

    # Accept Privacy Policy and Click Continue Button
    register_page.click_privacy_policy_checkbox()
    register_page.click_continue_button()

    # Verify Account Creation Confirmation and Validation
    registration_success_message = register_page.registration_confirmation_success_message()
    expect(registration_success_message).to_have_text("Your Account Has Been Created!")
    page.wait_for_timeout(5000)


@pytest.mark.skip(reason="Currently there is no validation on UI page - SKIP")
def test_0003_new_user_registration_invalid_inputs(page:Page):

    """
    To validate - New user registration with invalid input
    IMP - Currently there is no validation on UI page - SKIP
    """

    # Browse URL
    page.goto(Config.base_url)

    # Create Page Object
    home_page = HomePage(page)
    register_page = Register(page)

    # Navigate to registration page
    home_page.click_myaccount()
    home_page.click_register()

    # Fill Registration Form
    register_page.set_firstname(Config.invalid_register_first_name)
    register_page.set_lastname(Config.invalid_register_last_name)
    register_page.set_email(Config.invalid_register_email)
    register_page.set_telephone(Config.invalid_register_telephone)
    register_page.set_password(Config.invalid_register_password)
    register_page.set_confirm_password(Config.invalid_register_confirm_password)

    # Accept Privacy Policy and Submit
    register_page.click_privacy_policy_checkbox()
    register_page.click_continue_button()

    # Verify Account Creation Confirmation and Validation
    registration_success_message = register_page.registration_confirmation_success_message()
    expect(registration_success_message).to_have_text("Currently there is no validation on UI page - SKIP")


def test_0004_new_user_registration_subscribe_newsletter_yes(page:Page):

    """
    To Validate - Register an Account when 'YES' option is selected for Subscribe Newsletter field
    """

    # Browse URL
    page.goto(Config.base_url)

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

    # Select Newsletter Subscription as 'YES'
    register_page.click_subscribe_yes()

    # Accept Privacy Policy and Submit
    register_page.click_privacy_policy_checkbox()
    register_page.click_continue_button()

    # Verify Account Creation Confirmation and Validation
    registration_success_message = register_page.registration_confirmation_success_message()
    expect(registration_success_message).to_have_text("Your Account Has Been Created!")


def test_0005_new_user_registration_subscribe_newsletter_no(page:Page):

    """
    To Validate - Register an Account when 'NO' option is selected for Subscribe Newsletter field
    """

    # Browse URL
    page.goto(Config.base_url)

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

    # Select Newsletter Subscription as 'NO'
    register_page.click_subscribe_no()

    # Accept Privacy Policy and Submit
    register_page.click_privacy_policy_checkbox()
    register_page.click_continue_button()

    # Verify Account Creation Confirmation and Validation
    registration_success_message = register_page.registration_confirmation_success_message()
    expect(registration_success_message).to_have_text("Your Account Has Been Created!")


def test_0006_new_user_registration_register_with_different_confirm_password(page:Page):

    """
    To Validate - Register account by entering different passwords into 'Password' and 'Password Confirm' fields
    """

    # Browse URL
    page.goto(Config.base_url)

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
    register_page.set_confirm_password(Config.different_register_confirm_password)

    # Select Newsletter Subscription as 'YES'
    register_page.click_subscribe_yes()

    # Accept Privacy Policy and Submit
    register_page.click_privacy_policy_checkbox()
    register_page.click_continue_button()

    # Verify warning message for confirm password mismatch
    different_confirm_password_warning_message = register_page.different_confirm_password_warning_message()
    expect(different_confirm_password_warning_message).to_have_text("Password confirmation does not match password!")
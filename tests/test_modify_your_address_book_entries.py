from playwright.sync_api import Page , expect
from OpenCart.pageobject.modify_your_address_book_entries import ModifyYourAddressBookEntries
from OpenCart.config import Config

# To verify modify address book entries

def test_modify_address_book_entries(page:Page):

    page.goto("https://tutorialsninja.com/demo/")

    # Create Page Object
    modify_address_book_entries = ModifyYourAddressBookEntries(page)
    config_data = Config()

    # Navigate to login - modify - edit
    modify_address_book_entries.click_myaccount()
    modify_address_book_entries.click_login_link()
    modify_address_book_entries.user_email_address(config_data.email)
    modify_address_book_entries.user_password(config_data.password)
    modify_address_book_entries.click_login_button()
    modify_address_book_entries.click_modify()
    modify_address_book_entries.click_edit()
    modify_address_book_entries.provide_firstname(config_data.modify_firstname)
    modify_address_book_entries.provide_lastname(config_data.modify_lastname)
    modify_address_book_entries.provide_address(config_data.modify_address)
    modify_address_book_entries.provide_city(config_data.modify_city)
    page.wait_for_timeout(10000)
    modify_address_book_entries.select_country(config_data.modify_country)
    modify_address_book_entries.select_region(config_data.modify_region)
    modify_address_book_entries.click_continue()

    # Verify Account Creation Confirmation and Validation
    page.wait_for_timeout(10000)
    success_message = modify_address_book_entries.verify_message_success()
    expect(success_message).to_be_visible()
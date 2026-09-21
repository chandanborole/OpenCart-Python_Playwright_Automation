from playwright.sync_api import Page

# Pageobject model class for Modify Your Address Book Entries page

class ModifyYourAddressBookEntries:

    # Constructor
    def __init__(self , page:Page):
        self.page = page

        # Locators declaration for Modify Your Address Book Entries page
        self.modify_your_address_book_entries_link_my_account = self.page.locator("span:has-text('My Account')")
        self.modify_your_address_book_entries_link_login = self.page.locator("a:has-text('Login')")
        self.modify_your_address_book_entries_textbox_email_address = self.page.locator("#input-email")
        self.modify_your_address_book_entries_textbox_password = self.page.locator("#input-password")
        self.modify_your_address_book_entries_button_click_login = self.page.locator("input[type='submit']")
        self.modify_your_address_book_entries_link_click_modify = self.page.locator("a:has-text('Modify your address book entries')")
        self.modify_your_address_book_entries_button_click_edit = self.page.locator("tbody tr td .btn.btn-info")
        self.modify_your_address_book_entries_textbox_first_name = self.page.locator("#input-firstname")
        self.modify_your_address_book_entries_textbox_last_name = self.page.locator("#input-lastname")
        self.modify_your_address_book_entries_textbox_address1 = self.page.locator("#input-address-1")
        self.modify_your_address_book_entries_textbox_city = self.page.locator("#input-city")
        self.modify_your_address_book_entries_dropdown_country = self.page.locator("#input-country")
        self.modify_your_address_book_entries_dropdown_region = self.page.locator("#input-zone")
        self.modify_your_address_book_entries_button_click_continue = self.page.locator("input[type='submit']")
        self.modify_your_address_book_entries_message_success = self.page.locator(".fa-check-circle")

    # Action methods

    def click_myaccount(self):
        self.modify_your_address_book_entries_link_my_account.click()

    def click_login_link(self):
        self.modify_your_address_book_entries_link_login.click()

    def user_email_address(self, email_address):
        self.modify_your_address_book_entries_textbox_email_address.fill(email_address)

    def user_password(self, password):
        self.modify_your_address_book_entries_textbox_password.fill(password)

    def click_login_button(self):
        self.modify_your_address_book_entries_button_click_login.click()

    def click_modify(self):
        self.modify_your_address_book_entries_link_click_modify.click()

    def click_edit(self):
        self.modify_your_address_book_entries_button_click_edit.click()

    def provide_firstname(self, firstname):
        self.modify_your_address_book_entries_textbox_first_name.fill(firstname)

    def provide_lastname(self, lastname):
        self.modify_your_address_book_entries_textbox_last_name.fill(lastname)

    def provide_address(self, address):
        self.modify_your_address_book_entries_textbox_address1.fill(address)

    def provide_city(self, city):
        self.modify_your_address_book_entries_textbox_city.fill(city)

    def select_country(self, country):
        self.modify_your_address_book_entries_dropdown_country.select_option(country)

    def select_region(self, region):
        self.modify_your_address_book_entries_dropdown_region.select_option(region)

    def click_continue(self):
        self.modify_your_address_book_entries_button_click_continue.click()

    def verify_message_success(self):
        return self.modify_your_address_book_entries_message_success
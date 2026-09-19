from playwright.sync_api import Page

# Pageobject model class for Login page

class Login:

    # Constructor
    def __init__(self , page:Page):
        self.page = page

        # Locators declaration for Login page
        self.login_link_my_account = self.page.locator("span:has-text('My Account')")
        self.login_link_login = self.page.locator("a:has-text('Login')")
        self.login_textbox_email_address = self.page.locator("#input-email")
        self.login_textbox_password = self.page.locator("#input-password")
        self.login_button_click_login = self.page.locator("input[type='submit']")

    #Action methods

    def click_myaccount(self):
        self.login_link_my_account.click()

    def click_login_link(self):
        self.login_link_login.click()

    def set_email_address(self , email_address):
        self.login_textbox_email_address.fill(email_address)

    def set_password(self , password):
        self.login_textbox_password.fill(password)

    def click_login_button(self):
        self.login_button_click_login.click()
from playwright.sync_api import Page

# Pageobject model class for Homepage

class HomePage:

    # Constructor
    def __init__(self , page:Page):
        self.page = page

        # Locators declaration for Register page
        self.homepage_link_my_account = self.page.locator("span:has-text('My Account')")
        self.homepage_link_register = self.page.locator("a:has-text('Register')")
        self.homepage_link_click_login= self.page.locator("a:has-text('Login')")
        self.homepage_textbox_email_address = self.page.locator("#input-email")
        self.homepage_textbox_password = self.page.locator("#input-password")
        self.homepage_button_click_continue = self.page.locator("input[type='submit'][value='Login']")

    # Action methods
    def click_myaccount(self):
        self.homepage_link_my_account.click()

    def click_register(self):
        self.homepage_link_register.click()

    def click_login(self):
        self.homepage_link_click_login.click()

    def set_email_address(self , email_address):
        self.homepage_textbox_email_address.fill(email_address)

    def set_password(self , password):
        self.homepage_textbox_password.fill(password)

    def homepage_button_click_continue(self):
        self.homepage_button_click_continue.click()
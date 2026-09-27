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
        self.login_title_after_valid_login = self.page.locator("title:has-text('My Account')")
        self.login_warning_message_invalid_login = self.page.locator(".alert:has-text('Warning: No match for E-Mail Address and/or Password.')")
        self.login_warning_for_exceeded_login_attempts = self.page.locator(".alert:has-text('Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.')")
        self.login_hyperlink_forgotten_password = self.page.locator(".form-group:has-text('Forgotten Password')")
        self.login_title_forgot_your_password = self.page.locator("h1")


    #Action methods

    def click_myaccount(self):
        self.login_link_my_account.click()

    def click_login_link(self):
        self.login_link_login.click()

    def user_email_address(self , email_address):
        self.login_textbox_email_address.fill(email_address)

    def user_password(self , password):
        self.login_textbox_password.fill(password)

    def click_login_button(self):
        self.login_button_click_login.click()

    def verify_title_after_valid_login(self):
        return self.login_title_after_valid_login

    def invalid_login_warning_message(self):
        return self.login_warning_message_invalid_login

    def exceeded_login_attempts_warning_message(self):
        return self.login_warning_for_exceeded_login_attempts

    def click_forgotten_password_hyperlink(self):
        return self.login_hyperlink_forgotten_password.click()

    def verify_title_forgot_your_password(self):
        return self.login_title_forgot_your_password

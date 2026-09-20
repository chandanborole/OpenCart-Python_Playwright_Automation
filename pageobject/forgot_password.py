from playwright.sync_api import Page

# Pageobject model class for forgot password

class ForgotPassword:

    # Constructor
    def __init__(self , page:Page):
        self.page = page

        # Locators declaration for forgot password page
        self.forgotpassword_link_my_account = self.page.locator("span:has-text('My Account')")
        self.forgotpassword_link_login = self.page.locator("a:has-text('Login')")
        self.forgotpassword_link_forgot_password = self.page.locator("form[action*='account/login'] a:has-text('Forgotten Password')")
        self.forgotpassword_textbox_email_address = self.page.get_by_label("E-Mail Address")
        self.forgotpassword_button_click_continue = self.page.locator("input[value='Continue']")
        self.forgotpassword_success_message = self.page.locator(".alert:has-text('An email with a confirmation link has been sent your email address.')")

    # Action methods
    def click_myaccount(self):
        self.forgotpassword_link_my_account.click()

    def click_login_link(self):
        self.forgotpassword_link_login.click()

    def click_forgotten_password(self):
        self.forgotpassword_link_forgot_password.click()

    def provide_email_address(self , emailid):
        self.forgotpassword_textbox_email_address.fill(emailid)

    def click_continue_button(self):
        self.forgotpassword_button_click_continue.click()

    def confirmation_message(self):
        return self.forgotpassword_success_message
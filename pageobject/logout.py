from playwright.sync_api import Page

# Pageobject model class for Logout page

class Logout:

    # Constructor
    def __init__(self , page:Page):
        self.page = page

        # Locators declaration for Logout page
        self.logout_link_my_account = self.page.locator("span:has-text('My Account')")
        self.logout_link_login = self.page.locator("a:has-text('Login')")
        self.logout_textbox_email_address = self.page.locator("#input-email")
        self.logout_textbox_password = self.page.locator("#input-password")
        self.logout_button_click_login = self.page.locator("input[type='submit']")
        self.logout_link_my_account_after_login = self.page.locator(".hidden-sm:has-text('My Account')")
        self.logout_link_logout = self.page.locator(".dropdown-menu:has-text('Logout')")
        self.logout_button_continue_after_logout = self.page.locator(".pull-right:has-text('Continue')")
        self.logout_verify_title_after_logout = self.page.locator("title:has-text('My Account')")
        self.logout_from_right_column = self.page.locator(".list-group-item:has-text('Logout')")
        self.logout_button_continue_after_logout_from_right_column_options = self.page.locator(".btn-primary:has-text('Continue')")
        self.logout_verify_title_after_logout_from_right_column_options = self.page.locator("title:has-text('Your Store')")

    #Action methods

    def click_myaccount(self):
        self.logout_link_my_account.click()

    def click_login_link(self):
        self.logout_link_login.click()

    def user_email_address(self, email_address):
        self.logout_textbox_email_address.fill(email_address)

    def user_password(self, password):
        self.logout_textbox_password.fill(password)

    def click_login_button(self):
        self.logout_button_click_login.click()

    def click_my_account_after_login(self):
        self.logout_link_my_account_after_login.click()

    def click_logout_link(self):
        self.logout_link_logout.click()

    def click_continue_after_logout(self):
        self.logout_button_continue_after_logout.click()

    def verify_title_after_logout(self):
        return self.page

    def click_logout_from_right_column(self):
        self.logout_from_right_column.click()

    def click_continue_after_logout_from_right_column_options(self):
        self.logout_button_continue_after_logout_from_right_column_options.click()

    def verify_title_after_logout_from_right_column_options(self):
        return self.page
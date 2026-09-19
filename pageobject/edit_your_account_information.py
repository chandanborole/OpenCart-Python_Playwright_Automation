from playwright.sync_api import Page

# Pageobject model class for Edit your account information page

class EditYourAccountInformation:

    # Constructor
    def __init__(self , page:Page):
        self.page = page

        # Locators declaration for Edit your account information page
        self.edityouraccountinformation_link_my_account = self.page.locator("span:has-text('My Account')")
        self.edityouraccountinformation_link_login = self.page.locator("a:has-text('Login')")
        self.edityouraccountinformation_textbox_email_address = self.page.locator("#input-email")
        self.edityouraccountinformation_textbox_password = self.page.locator("#input-password")
        self.edityouraccountinformation_button_click_login = self.page.locator("input[type='submit']")
        self.edityouraccountinformation_link_edit_your_account_information = self.page.locator("a:has-text('Edit your account information')")
        self.edityouraccountinformation_textbox_firstname = self.page.locator("#input-firstname")
        self.edityouraccountinformation_textbox_lastname = self.page.locator("#input-lastname")
        self.edityouraccountinformation_textbox_telephone = self.page.locator("#input-telephone")
        self.edityouraccountinformation_button_click = page.locator("input[type='submit']")
        self.edityouraccountinformation_message_success_message = page.locator(".alert")

    # Action methods
    def click_myaccount(self):
        self.edityouraccountinformation_link_my_account.click()

    def click_login_link(self):
        self.edityouraccountinformation_link_login.click()

    def user_email_address(self , email_address):
        self.edityouraccountinformation_textbox_email_address.fill(email_address)

    def user_password(self , password):
        self.edityouraccountinformation_textbox_password.fill(password)

    def click_login_button(self):
        self.edityouraccountinformation_button_click_login.click()

    def click_edit(self):
        self.edityouraccountinformation_link_edit_your_account_information.click()

    def set_firstname(self, firstname):
        self.edityouraccountinformation_textbox_firstname.fill(firstname)

    def set_lastname(self, lastname):
        self.edityouraccountinformation_textbox_lastname.fill(lastname)

    def set_telephone(self, telephone):
        self.edityouraccountinformation_textbox_telephone.fill(telephone)

    def click_continue_button(self):
        self.edityouraccountinformation_button_click.click()

    def edit_confirmation_success_message(self):
        return self.edityouraccountinformation_message_success_message
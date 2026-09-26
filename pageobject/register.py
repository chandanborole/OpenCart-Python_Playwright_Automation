from playwright.sync_api import Page

# Pageobject model class for Register page

class Register:

    # Constructor
    def __init__(self , page:Page):
        self.page = page

        # Locators declaration for Register page
        self.register_link_my_account = self.page.locator("span:has-text('My Account')")
        self.register_link_register = self.page.locator("a:has-text('Register')")
        self.register_textbox_firstname = self.page.locator("#input-firstname")
        self.register_textbox_lastname = self.page.locator("#input-lastname")
        self.register_textbox_email = self.page.locator("#input-email")
        self.register_textbox_telephone = self.page.locator("#input-telephone")
        self.register_textbox_password = self.page.locator("#input-password")
        self.register_textbox_confirm_password = self.page.locator("#input-confirm")
        self.register_radio_click_subscribe_yes = self.page.locator("input[name='newsletter'][value='1']")
        self.register_radio_click_subscribe_no = self.page.locator("input[name='newsletter'][value='0']")
        self.register_checkbox_click_privacy_policy = self.page.locator("input[name='agree']")
        self.register_button_click_continue_button = self.page.locator("input[type='submit']")
        self.register_message_registration_success_message = self.page.locator("h1:has-text('Your Account Has Been Created!')")
        self.register_message_password_warning_message = self.page.locator(".text-danger:has-text('Password must be between 4 and 20 characters!')")
        self.register_message_different_confirm_password_warning_message = self.page.locator(".text-danger:has-text('Password confirmation does not match password!')")
        self.register_message_register_with_existing_details_warning_message = self.page.locator(".alert:has-text('Warning: E-Mail Address is already registered!')")

    # Action methods

    def set_firstname(self , firstname):
        self.register_textbox_firstname.fill(firstname)

    def set_lastname(self , lastname):
        self.register_textbox_lastname.fill(lastname)

    def set_email(self , email):
        self.register_textbox_email.fill(email)

    def set_telephone(self , telephone):
        self.register_textbox_telephone.fill(telephone)

    def set_password(self , password):
        self.register_textbox_password.fill(password)

    def set_confirm_password(self , confirm_password):
        self.register_textbox_confirm_password.fill(confirm_password)

    def click_subscribe_yes(self):
        self.register_radio_click_subscribe_yes.click()

    def click_subscribe_no(self):
        self.register_radio_click_subscribe_no.click()

    def click_privacy_policy_checkbox(self):
        self.register_checkbox_click_privacy_policy.click()

    def click_continue_button(self):
        self.register_button_click_continue_button.click()

    def registration_confirmation_success_message(self):
        return self.register_message_registration_success_message

    def blank_password_warning_message(self):
        return self.register_message_password_warning_message

    def different_confirm_password_warning_message(self):
        return self.register_message_different_confirm_password_warning_message

    def register_with_existing_details_warning_message(self):
        return self.register_message_register_with_existing_details_warning_message
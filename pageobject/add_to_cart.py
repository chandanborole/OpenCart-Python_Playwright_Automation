from playwright.sync_api import Page

# Pageobject model class for add to cart

class AddToCart:

    # Constructor
    def __init__(self , page:Page):
        self.page = page

        # Locators declaration for add to cart page
        self.addtocart_link_my_account = self.page.locator("span:has-text('My Account')")
        self.addtocart_link_login = self.page.locator("a:has-text('Login')")
        self.addtocart_textbox_email_address = self.page.locator("#input-email")
        self.addtocart_textbox_password = self.page.locator("#input-password")
        self.addtocart_button_click_login = self.page.locator("input[type='submit']")
        self.addtocart_title_after_valid_login = self.page.locator("title:has-text('My Account')")
        self.addtocart_searchbox_search_product = self.page.locator("input[type='text'][placeholder='Search']")
        self.addtocart_title_after_search_product = self.page.locator("title:has-text('Search - iMac')")
        self.addtocart_button_click_serach_product = self.page.locator("button[type='button'][class='btn btn-default btn-lg']")
        self.addtocart_button_click_add_to_cart = self.page.locator("span:has-text('ADD TO CART')")
        self.addtocart_message_addtocart_success_message = self.page.locator(".alert-success:has-text('Success: You have added iMac to your shopping cart!')")

    # Action methods

    def click_myaccount(self):
        self.addtocart_link_my_account.click()

    def click_login_link(self):
        self.addtocart_link_login.click()

    def user_email_address(self, email_address):
        self.addtocart_textbox_email_address.fill(email_address)

    def user_password(self, password):
        self.addtocart_textbox_password.fill(password)

    def click_login_button(self):
        self.addtocart_button_click_login.click()

    def verify_title_after_valid_login(self):
        return self.page

    def search_product(self, product_name):
        self.addtocart_searchbox_search_product.fill(product_name)

    def click_search_product_button(self):
        self.addtocart_button_click_serach_product.click()

    def verify_title_after_search_product(self):
        return self.page

    def click_add_to_cart_button(self):
        self.addtocart_button_click_add_to_cart.click()

    def add_to_cart_success_message(self):
        return self.addtocart_message_addtocart_success_message
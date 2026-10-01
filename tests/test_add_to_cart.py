from playwright.sync_api import Page , expect
from OpenCart.pageobject.login import Login
from OpenCart.pageobject.add_to_cart import AddToCart
from OpenCart.config import Config

def test_0020_validate_adding_the_product_to_cart_from_product_display_page(page:Page):

    """
    To validate - adding the product to Cart from 'Product Display' Page
    """

    # Browse URL
    page.goto(Config.valid_base_url)

    # Create Page Object
    login_page = Login(page)
    add_to_cart_page = AddToCart(page)
    config_data = Config

    # Navigate to login page
    login_page.click_myaccount()
    login_page.click_login_link()

    # Fill User ID / Password
    login_page.user_email_address(config_data.valid_register_email)
    login_page.user_password(config_data.valid_register_password)
    login_page.click_login_button()

    # Verify title after login
    title_after_valid_login = login_page.verify_title_after_valid_login()
    expect(title_after_valid_login).to_have_title("My Account")

    # Search for a product
    add_to_cart_page.search_product(config_data.search_product)

    # Click on search button
    add_to_cart_page.click_search_product_button()

    # Verify title after searching for the product
    title_after_search_product = add_to_cart_page.verify_title_after_search_product()
    expect(title_after_search_product).to_have_title(f"Search - {config_data.search_product}")

    # Click on add to cart button to add in cart
    add_to_cart_page.click_add_to_cart_button()

    # Verify success message after adding the product to cart
    add_to_cart_success_message = add_to_cart_page.add_to_cart_success_message()
    expect(add_to_cart_success_message).to_be_visible()
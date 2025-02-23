import pytest
from playwright.sync_api import Page, expect
from faker import Faker
from pages.login import LoginPage
from pages.home import HomePage
from pages.details import DetailsPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage

@pytest.fixture(scope="session", autouse=True)
def configure_playwright(playwright):
    """Set the test ID attribute globally before running tests"""
    playwright.selectors.set_test_id_attribute("data-test")


def test_buy_item(page: Page):
    faker = Faker()

    page.goto('https://www.saucedemo.com/v1/')
    loginPage = LoginPage(page)
    loginPage.login('standard_user', 'secret_sauce')

    homePage = HomePage(page)
    homePage.clickItem("Sauce Labs Backpack")
    page.get_by_text("Sauce Labs Backpack").is_visible()

    detailsPage = DetailsPage(page)
    detailsPage.cartBtn.click()
    detailsPage.shoppingCart.click()
    page.get_by_role("link", name="Sauce Labs Backpack").is_visible()

    firstName = faker.first_name()
    lastName = faker.last_name()
    zipCode = faker.zipcode()

    cartPage = CartPage(page)
    cartPage.checkoutBtn.click()
    cartPage.inputPaymentInfo(firstName, lastName, zipCode)
    page.get_by_role("link", name="Sauce Labs Backpack").is_visible()

    checkoutPage = CheckoutPage(page)
    checkoutPage.finishBtn.click()
    
    page.get_by_role("heading", name="THANK YOU FOR YOUR ORDER").is_visible()
    page.pause()

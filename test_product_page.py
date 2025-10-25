import pytest
import time

from .pages.product_page import ProductPage



@pytest.mark.parametrize(
    "link",
    [
        f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}"
        for i in range(10)
    ],
)
def test_guest_can_add_product_to_basket(browser, link):
    if "offer7" in link:
        pytest.xfail("Known issue with promo offer7")

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

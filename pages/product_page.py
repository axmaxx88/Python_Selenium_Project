from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        # нажимаем кнопку добавить товар в корзину
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_to_basket_button.click()

    def should_be_message_about_adding(self):
        # проверяем, что сообщение о добавлении товара присутствует на странице
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_MESSAGE), "Message about adding is not presented"
        # проверяем, что название добавленной книги соответствует выбранной
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_text = book_name.text
        book_name_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MESSAGE)
        book_name_message_text = book_name_message.text
        assert book_name_text == book_name_message_text, "Added book does not match selected one"

    def should_be_message_about_price(self):
        # проверяем, что сообщение с суммой товара присутствует на странице
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_MESSAGE), "Message about price is not presented"
        # проверяем, что цена добавленного товара соответствует выбранному
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price_text = book_price.text
        book_price_message = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_MESSAGE)
        book_price_message_text = book_price_message.text
        assert book_price_text == book_price_message_text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but have to"

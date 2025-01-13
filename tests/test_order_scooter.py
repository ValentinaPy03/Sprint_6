from conftest import driver
from pages.order_scooter_page import OrderScooter
import allure
from helper import generate_order_data
from data import *
from curl import *

class TestOrder:
    @allure.title('Проверка заказа через кнопку в хэдере страницы')
    def test_order_by_button_in_header(self, driver):
        name, last_name, address, phone = generate_order_data()

        order_scooter = OrderScooter(driver)

        order_scooter.click_order_button_on_header()
        order_scooter.wait_page_order()
        order_scooter.fill_order_form(name,last_name,address, phone)
        order_scooter.fill_field_metro()
        order_scooter.assept_cockies()
        order_scooter.click_button_below()
        order_scooter.wait_page_order_about_rent()
        order_scooter.fill_order_form_about_fent()
        order_scooter.wait_page_confirmation()
        order_scooter.click_button_yes()

        assert order_scooter.check_button_check_status()

    @allure.title('Проверка заказа через кнопку внизу страницы')
    def test_order_by_button_on_page(self,driver):
        name, last_name, address, phone = generate_order_data()

        order_scooter = OrderScooter(driver)

        order_scooter.scroll_to_button_order()
        order_scooter.click_order_button_on_page()
        order_scooter.wait_page_order()
        order_scooter.fill_order_form(name, last_name, address, phone)
        order_scooter.fill_field_metro()
        order_scooter.assept_cockies()
        order_scooter.click_button_below()
        order_scooter.wait_page_order_about_rent()
        order_scooter.fill_order_form_about_fent()
        order_scooter.wait_page_confirmation()
        order_scooter.click_button_yes()

        assert order_scooter.check_button_check_status()

    @allure.title('Проверка перехода на главную страницу через клик по логотипу Самокат')
    def test_going_by_logo_scooter(self, driver):
        order_scooter = OrderScooter(driver)
        order_scooter.click_order_button_on_header()
        order_scooter.wait_page_order()
        order_scooter.click_on_logo_scooter()
        text = order_scooter.get_text_of_title()

        assert text == Data.title_on_main_page

    @allure.title('Проверка перехода на Я.Дзен через клик по лого Яндекс')
    def test_going_by_logo_yandex(self, driver):
        order_scooter = OrderScooter(driver)
        order_scooter.click_order_button_on_header()
        order_scooter.wait_page_order()
        order_scooter.click_on_logo_yandex()

        order_scooter.switch_window()
        order_scooter.wait_loading_dzen()

        current_url = order_scooter.get_url_of_page()

        assert current_url == main_page_dzen











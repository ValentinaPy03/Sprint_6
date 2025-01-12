from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from pages.order_scooter_page import OrderScooter
import random
import allure

class TestOrder:
    faker = Faker('ru_RU')
    @allure.title('Проверка заказа через кнопку в хэдере страницы')
    def test_order_by_button_in_header(self, driver):
        faker = Faker('ru_RU')
        name = faker.first_name()
        last_name = faker.last_name()
        address = f'{faker.street_name()}, {faker.building_number()}'
        phone = f'89{random.randint(111111111, 999999999)}'

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

        assert order_scooter.check_button_check_status() == True

    @allure.title('Проверка заказа через кнопку внизу страницы')
    def test_order_by_button_on_page(self,driver):
        faker = Faker('ru_RU')
        name = faker.first_name()
        last_name = faker.last_name()
        address = f'{faker.street_name()}, {faker.building_number()}'
        phone = f'89{random.randint(111111111, 999999999)}'

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

        assert order_scooter.check_button_check_status() == True

    @allure.title('Проверка перехода на главную страницу через клик по логотипу Самокат')
    def test_going_by_logo_scooter(self, driver):
        order_scooter = OrderScooter(driver)
        order_scooter.click_order_button_on_header()
        order_scooter.wait_page_order()
        order_scooter.click_on_logo_scooter()
        text = order_scooter.get_text_of_title()

        assert text == 'Самокат\n''на пару дней\n''Привезём его прямо к вашей двери,\n''а когда накатаетесь — заберём'

    @allure.title('Проверка перехода на Я.Дзен через клик по лого Яндекс')
    def test_going_by_logo_yandex(self, driver):
        order_scooter = OrderScooter(driver)
        order_scooter.click_order_button_on_header()
        order_scooter.wait_page_order()
        order_scooter.click_on_logo_yandex()

        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        WebDriverWait(driver, 10).until(EC.title_contains("Дзен"))

        current_url = driver.current_url

        assert current_url == 'https://dzen.ru/?yredirect=true'











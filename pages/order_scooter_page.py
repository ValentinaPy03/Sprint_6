import allure
from locators.order_scooter_page_locator import OrderScooterPageLocators
from pages.base_page import BasePage

class OrderScooter(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Кликнуть по кнопке Заказать')
    def click_order_button_on_header(self):
        self.click_on_element(OrderScooterPageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Кликнуть по кнопке заказать внизу страницы')
    def click_order_button_on_page(self):
        self.wait_for_element(OrderScooterPageLocators.BUTTON_ORDER)
        self.click_on_element(OrderScooterPageLocators.BUTTON_ORDER)

    @allure.step('Дождаться закрузки страницы заказа')
    def wait_page_order(self):
        self.wait_for_element(OrderScooterPageLocators.TEXT_FOR_WHOM_SCOOTER)

    @allure.step('Заполнить форму заказа')
    def fill_order_form(self, name, last_name, address, phone):
        self.send_keys_to_input(OrderScooterPageLocators.FIELD_NAME, name)
        self.send_keys_to_input(OrderScooterPageLocators.FIELD_LAST_NAME, last_name)
        self.send_keys_to_input(OrderScooterPageLocators.FIELD_ADRESS, address)
        self.send_keys_to_input(OrderScooterPageLocators.FIELD_PHONE, phone)

    def fill_field_metro(self):
        self.click_on_element(OrderScooterPageLocators.FIELD_METRO)
        self.click_on_element(OrderScooterPageLocators.METRO_STATION_DROPDOWN)

    @allure.step('Нажать кнопку Далее')
    def click_button_below(self):
        self.click_on_element(OrderScooterPageLocators.BUTTON_BELOW)

    @allure.step('Дождаться закрузки второй страницы заказа')
    def wait_page_order_about_rent(self):
        self.wait_for_element(OrderScooterPageLocators.TEXT_ABOUT_RENT)

    @allure.step('Заполнить вторю форму заказа')
    def fill_order_form_about_fent(self):
        self.click_on_element(OrderScooterPageLocators.FIELD_DATE)
        self.click_on_element(OrderScooterPageLocators.DATE_13_01)
        self.click_on_element(OrderScooterPageLocators.FIELD_PERIOD_RENT)
        self.click_on_element(OrderScooterPageLocators.TWO_DAYS_PERIOD)
        self.click_on_element(OrderScooterPageLocators.CHECKBOX_BLACK_PEARL)
        self.click_on_element(OrderScooterPageLocators.BUT_ORDER)

    @allure.step('Дождаться окна подстверждения заказа')
    def wait_page_confirmation(self):
        self.wait_for_element(OrderScooterPageLocators.ORDER_CONFIRMATION)

    @allure.step('Подтвердить заказ')
    def click_button_yes(self):
        self.click_on_element(OrderScooterPageLocators.BUTTON_YES)

    @allure.step('Проверить, что кнопка Проверить заказ на экране')
    def check_button_check_status(self):
        return self.check_element_is_displayed(OrderScooterPageLocators.BUTTON_CHECK_STATUS)

    @allure.step('Скролл до кнопки Заказть внизу страницы')
    def scroll_to_button_order(self):
        self.scroll_to_element(OrderScooterPageLocators.BUTTON_ORDER)

    @allure.step('Клик на лого Самокат')
    def click_on_logo_scooter(self):
        self.click_on_element(OrderScooterPageLocators.LOGO_SCOOTER)

    @allure.step('Клик на лого Яндекс')
    def click_on_logo_yandex(self):
        self.click_on_element(OrderScooterPageLocators.LOGO_YANDEX)

    @allure.step('Получить текст Самокат на пару дней')
    def get_text_of_title(self):
        self.wait_for_element(OrderScooterPageLocators.TITLE_ON_MAIN_PAGE)
        return self.get_text_on_element(OrderScooterPageLocators.TITLE_ON_MAIN_PAGE)

    @allure.step('Дождаться загрузки Дзена')
    def wait_for_loading_page(self):
        self.wait_for_element(OrderScooterPageLocators.LOGO_DZEN)

    @allure.step('Принять куки')
    def assept_cockies(self):
        self.click_on_element(OrderScooterPageLocators.BUTTON_ASEPT_COOCKIES)

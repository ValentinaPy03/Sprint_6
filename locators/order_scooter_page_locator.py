from selenium.webdriver.common.by import By

class OrderScooterPageLocators:
    BUTTON_ORDER_HEADER = [By.XPATH, "//button[@class='Button_Button__ra12g']"]
    BUTTON_ORDER = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    TEXT_FOR_WHOM_SCOOTER = [By.XPATH, '//div[text()="Для кого самокат"]']
    FIELD_NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    FIELD_LAST_NAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    FIELD_ADRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    FIELD_METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    METRO_STATION_DROPDOWN = (By.XPATH, "//ul[@class='select-search__options']/li[1]")
    # METRO_STATION_SOKOLNIKI = [By.XPATH, "//div[@class='select-search__select']/ul/li[text()='Сокольники']"]
    FIELD_PHONE = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    BUTTON_BELOW = [By.XPATH, "//button[text()='Далее']"]
    TEXT_ABOUT_RENT = [By.XPATH,'//div[text()="Про аренду"]']
    FIELD_DATE = [By.XPATH, '// input[@placeholder = "* Когда привезти самокат"]']
    DATE_13_01 = [By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[1]']
    DATE_30_01 = [By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[4]']
    FIELD_PERIOD_RENT = [By.XPATH, "//div[@class='Dropdown-control']"]
    TWO_DAYS_PERIOD = [By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[2]']
    FIVE_DAYS_PERIOD = [By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[5]']
    CHECKBOX_BLACK_PEARL = [By.XPATH, '//input[@id="black"]']
    CHECKBOX_GREY_HOPELESSNESS = [By.XPATH, '//input[@id="grey"]']
    BUT_ORDER = [By.XPATH, "//*[@id='root']/div/div[2]/div[3]/button[2]"]

    ORDER_CONFIRMATION = [By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]']
    BUTTON_YES = [By.XPATH, '//button[text()="Да"]']
    BUTTON_CHECK_STATUS = [By.XPATH, '//button[text()="Посмотреть статус"]']

    LOGO_SCOOTER = [By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]']
    LOGO_YANDEX = [By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]']

    TITLE_ON_MAIN_PAGE = [By.XPATH, '//div[@class="Home_Header__iJKdX"]']
    LOGO_DZEN = [By.XPATH, '//input[@class="arrow__input mini-suggest__input"]']

    BUTTON_ASEPT_COOCKIES = [By.XPATH, "//button[@id='rcc-confirm-button']"]


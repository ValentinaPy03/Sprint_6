from selenium.webdriver.common.by import By

class ImportantQuestionsLocators:
    QUESTION_LIST = [By.XPATH, "//div[@class='Home_FAQ__3uVm4']"]

    @staticmethod
    def question_number(question):
        return By.ID, f'accordion__heading-{question}'

    @staticmethod
    def answer(answer_number):
        return By.XPATH, f"//div[@id='accordion__panel-{answer_number}']/p"



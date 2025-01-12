import allure

from locators.important_question_page_locators import ImportantQuestionsLocators
from pages.base_page import BasePage


class ImportantQuestions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def wait_for_question_list(self):
        self.wait_for_element(ImportantQuestionsLocators.QUESTION_LIST)

    @allure.step("Нажать на вопрос из списка")
    def click_question(self, question):
        self.wait_for_clickable_element(ImportantQuestionsLocators.question_number(question))
        self.click_on_element(ImportantQuestionsLocators.question_number(question))

    @allure.step('Скролл до вопросов')
    def scroll_to_question(self, question):
        self.scroll_to_element(ImportantQuestionsLocators.question_number(question))

    @allure.step("Сравнить ответ на вопрос из списка")
    def check_answer(self, expected_text, answer_number):
        answer_locator = ImportantQuestionsLocators.answer(answer_number)
        actual_text = self.get_text_on_element(answer_locator)
        return actual_text == expected_text


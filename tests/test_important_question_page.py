import pytest
import data
from conftest import driver
from pages.important_question_page import ImportantQuestions
import allure


class TestImportantQuestions:
    @allure.title('Проверка корректных ответов на вопросы из секции Вопросы о важном')
    @pytest.mark.parametrize('question, expected_text', data.Data.question_number)
    def test_question_number(self, driver, question, expected_text):
        important_question_page = ImportantQuestions(driver)
        important_question_page.scroll_to_question(question)
        important_question_page.click_question(question)
        assert important_question_page.check_answer(expected_text, question)


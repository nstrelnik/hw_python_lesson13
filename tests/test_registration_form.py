import allure
from pages.registration_page import RegistrationFormPage


@allure.title("Корректность заполнения формы")
def test_student_registration_form():
    with allure.step("Поиск полей для заполнения формы"):
        registration_page = RegistrationFormPage()
    with allure.step("Заполнение формы регистрации"):
        registration_page.open()
        (
            registration_page
            .fill_first_name('Anastasiia')
            .fill_last_name('Strelnik')
            .fill_user_email('test@gmail.com')
            .fill_user_gender('Female')
            .fill_user_number('9216666666')
            .fill_day_of_birth('2001', 'March', '29')
            .fill_user_subject('Maths')
            .fill_user_hobby('Sports')
            .fill_user_picture('picture.jpg')
            .fill_user_current_address('Kaliningrad')
            .fill_user_state('NCR')
            .fill_user_city('Delhi')
            .click_submit()
        )
    with allure.step("Проверка заполнения формы регистрации"):
        registration_page.registered_user_with('Anastasiia Strelnik', 'test@gmail.com', 'Female', '9216666666',
                                               '29 March,2001',
                                               'Maths', 'Sports', 'picture.jpg',
                                               'Kaliningrad', 'NCR Delhi')
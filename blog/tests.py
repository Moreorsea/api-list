from django.test import TestCase
from .models import Author

# Create your tests here.


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_det_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/')


class AuthorTestClass(TestCase):
    # setUpTestData() вызывается каждый раз перед запуском теста на уровне настройки всего класса.
    # Вы должны использовать данный метод для создания объектов, которые не будут модифицироваться/изменяться
    # в каком-либо из тестовых методов
    @classmethod
    def setUpTestData(cls):
        # print("setUpTestData: Выполните один раз, чтобы настроить неизмененные данные для всех методов класса.")
        pass

    # setUp() вызывается перед каждой тестовой функцией для настройки объектов, которые могут изменяться во
    # время тестов (каждая функция тестирования будет получать "свежую" версию данных объектов).
    def setUp(self):
        # print("setUp: Выполните один раз для каждого метода тестирования, чтобы настроить чистые данные.")
        pass

    # def test_false_is_false(self):
    #     print("Method: test_false_is_false")
    #     pass

    # def test_false_is_true(self):
    #     print("Method: test_false_is_true")
    #     self.assertTrue(False)

    # def test_one_plus_one_equal_two(self):
    #     print("Method: test_one_plus_one_equal_two")
    #     self.assertEqual(1 + 1, 2)

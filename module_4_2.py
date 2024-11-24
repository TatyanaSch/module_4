# Домашнее задание по уроку "Пространство имен"
#
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новую функцию test_function
# Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы


a = 6


def test_function(x):
    a = x ** 2

    def inner_function():
        a = x * 2
        print("Я в области видимости функции test_function")

    inner_function()
    return a


print(test_function(40))

inner_function()

# вызов inner_function вне функции test_function выдает ошибку
#NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# Поскольку вызываем функцию из объемлющей области видимости, а не из локальной
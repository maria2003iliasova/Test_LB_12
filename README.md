# Автоматизированное тестирование.Selenium WebDriver

## Файл test1.py
Название: Авторизация с некорректными учетными данными (сайт ИСПИ)
Предусловие: Пользователь не авторизирован в системе
Шаги:
    1. Переходим на сайт кафедры ИСПИ на страницу авторизации;
    2. В поле «Логин» вводим 'k1179e6jt';
    3. В поле «Пароль» вводим 'NA498bli';
    4. Нажимаем на кнопку «Вход».
Ожидаемый результат: Пользователь находится на странице авторизации. На странице отображается сообщение «Неверный логин или пароль, попробуйте заново.».
Примечание: Логин и пароль надо указать в коде.

## Файл test2.py
Название: Авторизация с корректными учетными данными (сайт ИСПИ)
Предусловие: Пользователь не авторизирован в системе
Шаги:
    1. Переходим на сайт кафедры ИСПИ на страницу авторизации;
    2. В поле «Логин» вводим <ваш логиин>;
    3. В поле «Пароль» вводим <ваш пароль>;
    4. Нажимаем на кнопку «Вход».
Ожидаемый результат: Пользователь успешно авторизовался в системе. На странице отображается имя текущего пользователя.
Примечание: В коде нужно указать ФИО пользователя, логин и пароль.

## Файл test3.py
Название: Поиск книги (сайт Читай-город)
Предусловие: Открыть сайт
Последовательность действий:
    1. Перейти на главную страницу сайта «Читай город»;
    2. В поле поиска ввести «Дни нашей жизни»;
    3. Нажать на кнопку «Найти».
Ожидаемый результат: Поиск книги выполнен успешно. На странице присутствует название того, что искал пользователь.

## Файл test4.py
Название: Добавление товара в корзину (сайт Читай-город)
Предусловие: Открыть сайт
Последовательность действий:
    1. Перейти на страницу «Книги»;
    2. Нажать на кнопку «Купить»;
    3. Перейти в корзину.
Ожидаемый результат: Книга находится в корзине.

## Файл test5.py
Название: Авторизация с корректными учетными данными (сайт Читай-город)
Предусловие: Пользователь не авторизирован в системе
Последовательность действий:
    1. Перейти на главную страницу сайта «Читай город»;
    2. Нажать на кнопку «Войти»
    3. В поле «Логин» ввести <логин>;
    4. В поле «Пароль» ввести <пароль>;
    5. Нажимать на кнопку «Вход»;
    6. Перейти на страницу «Мой профиль».
Ожидаемый результат: Пользователь успешно авторизовался в системе. В профиле написано имя пользователя.
Примечание: В коде нужно указать имя пользователя, логин и пароль.
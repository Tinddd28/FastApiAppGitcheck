# FastApiAppGitcheck
распаковать/склонить репу с проектом
перейти в директорию с проектом и командой
- python -m venv venv
активировать виртуальное окружение: 
- Linux: source venv/bin/activate
- Windows: venv\bin\activate.bat

после чего установить зависимости из файла requeirements.txt командой
- pip install -r requirements.txt

дальше запустить main.py 
- python main.py 
и зайти по url: localhost:8080/docs для отображения swagger

## Получение гитхаб токена
- Зайти на сайт
- Перейти в настройки
-  Пролистать левую панель до конца вниз и перейти в раздел "Developer settings"
- Перейти в "Personal access tokens (classic)"
-  Нажать "Generate new token"
-  Выбрать все нужные параметры для данного токена
-  После чего скопировать токен в файл gitToken.py в директории config (необходимо создать переменную token и поместить туда скопированное значение)

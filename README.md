# DevOpsLab_11 CICD

Проверяем, что публичный ключ ssh добавлен на профиль в гите.
<img width="1280" height="417" alt="image" src="https://github.com/user-attachments/assets/21a9c4fb-9ee0-4046-933f-8a9523df9213" />

Создаём новый репозиторий.
<img width="1038" height="869" alt="image" src="https://github.com/user-attachments/assets/dbbe873c-3159-4272-a1ca-097f9891041a" />

И клонируем репозиторий.
<img width="847" height="219" alt="image" src="https://github.com/user-attachments/assets/668a3768-6b28-4d10-b529-cf354ef55e5d" />

Организуем структуру каталогов.
<img width="615" height="233" alt="image" src="https://github.com/user-attachments/assets/663bb07d-ac4f-40b2-ad7f-6e7cc026c20c" />

Создаем приложение server/application.py, в котором есть класс для демонстрации работы тестов и веб-сервер, отвечающий на любой запрос.
<img width="850" height="541" alt="image" src="https://github.com/user-attachments/assets/4f3443c4-d0e5-4d64-b20c-004c63f3c3c2" />

Юнит-тесты server/test-application.py, в которых используется библиотека pytest, импортируется приложение, проверяются наши функции из server/application.py.

<img width="661" height="436" alt="image" src="https://github.com/user-attachments/assets/1c6b0c1c-c3b2-436b-b93c-c9f81a7168cd" />

Создаем файл с зависимостями для самих тестов requirements.txt.

<img width="661" height="280" alt="image" src="https://github.com/user-attachments/assets/d40dc6c3-6cfb-4c6a-ba87-476de2e2aeea" />

Создаем файл для сборки образа dockerfile.
<img width="662" height="346" alt="image" src="https://github.com/user-attachments/assets/108f75cd-9ab0-40e7-9971-745b4c58fa4c" />

Пушим в гитхаб в ветку main.
<img width="845" height="553" alt="image" src="https://github.com/user-attachments/assets/4dff8cb7-b917-4560-8dda-b5ef7310c341" />
<img width="843" height="268" alt="image" src="https://github.com/user-attachments/assets/df0b36ea-4f5f-4a0d-949d-0c4e8ef5fa6d" />

Переходим в ветку dev.
<img width="848" height="308" alt="image" src="https://github.com/user-attachments/assets/7951147c-9973-464c-bc10-b3cccd855dea" />

Защищаем ветку main от прямых изменений, только merge-requests.
<img width="1280" height="813" alt="image" src="https://github.com/user-attachments/assets/e12a3491-f7bb-4166-ad4e-203e535b9b67" />

Добавляем сценарии
<img width="1280" height="808" alt="image" src="https://github.com/user-attachments/assets/3bb30cbc-02f0-4f3f-9ce8-393c61a26c01" />

Создаем базовый сценарий и пушим изменения в ветку dev.
<img width="719" height="454" alt="image" src="https://github.com/user-attachments/assets/367a14b6-caa1-4b44-9733-161018ea70f9" />
<img width="831" height="387" alt="image" src="https://github.com/user-attachments/assets/0605eeb0-76c8-4c91-aa07-da1ae1111993" />

Проверяем, как отработал.
<img width="1280" height="936" alt="image" src="https://github.com/user-attachments/assets/8c1067c5-d8c5-4e00-a03a-e9aed7e833ba" />

Создаем боевой сценарий и пушим его.
<img width="815" height="688" alt="image" src="https://github.com/user-attachments/assets/90653d59-5089-428f-a98f-ab9d12452548" />
<img width="779" height="683" alt="image" src="https://github.com/user-attachments/assets/568fb2ed-1f20-4440-b767-6eab6efb446d" />

Проверяем успешность работы сценария.
<img width="1280" height="424" alt="image" src="https://github.com/user-attachments/assets/9e1aa56f-8ded-4b69-a364-adf0b26abb0f" />
<img width="1280" height="586" alt="image" src="https://github.com/user-attachments/assets/394096bf-d6e3-4c06-917e-7031a0de30c0" />

Создаём k8s-манифест devops-psu для куберизирования нашего приложения.
<img width="797" height="700" alt="image" src="https://github.com/user-attachments/assets/3fe68962-6ad5-459e-be5a-ca1c52a024d9" />

Запускаем minikubе, применяем манифесты и проверяем поды, если с ними все отлично, пушим в гит.
<img width="811" height="462" alt="image" src="https://github.com/user-attachments/assets/80cf6773-e5a9-42c5-8392-56bd51710c71" />

Регистрируемся через гит, добавляем публикацию докер-образа приложения в хранилище, создаем токены для доступа.
<img width="1280" height="770" alt="image" src="https://github.com/user-attachments/assets/7611b265-bdad-4d61-8368-e049077f8108" />
<img width="1280" height="324" alt="image" src="https://github.com/user-attachments/assets/2890b64e-74e3-4d16-9496-c6f9196d8863" />

Создаем пайплайн .github/workflows/release.yml для сборки и публикации образа в докер.
<img width="637" height="571" alt="image" src="https://github.com/user-attachments/assets/991a2c8f-2ad4-413c-b161-d0d747bb9c51" />

Делаем коммит новых файлов в репозиторий, создаем pull-request и выполняем merge в main
<img width="1280" height="513" alt="image" src="https://github.com/user-attachments/assets/3aed926e-c0ae-4483-8975-68c8b4ab47c5" />

Прокидываем пайплайн и смотрим отображение в тегах докерхаб.
<img width="1280" height="588" alt="image" src="https://github.com/user-attachments/assets/5f3c8e99-4474-4991-82be-cd12aa5da481" />

# ArgoCD
Создаем отдельное пространство имен и скачиваем, устанавливаем все из манифеста.
<img width="801" height="387" alt="image" src="https://github.com/user-attachments/assets/450a0c1d-df83-4e39-b8ff-7a45a4673a2d" />

Ожидаем готовность модулей.
<img width="811" height="212" alt="image" src="https://github.com/user-attachments/assets/03fc969a-b089-479e-acd0-58ad9bcea21b" />

Достаём админский пароль.
<img width="818" height="88" alt="image" src="https://github.com/user-attachments/assets/07caecdf-8b41-41fc-9fab-5f6b3a49b794" />

Пробрасываем api-сервис.
<img width="831" height="149" alt="image" src="https://github.com/user-attachments/assets/bd362574-d83c-41a5-b458-2969481fce7f" />

<img width="838" height="523" alt="image" src="https://github.com/user-attachments/assets/5d618a14-1741-4b1c-aa5a-3880eb0ea9b1" />

Попадаем в Argo с помощью логина и пароля админа, ранее добытого.
<img width="1134" height="572" alt="image" src="https://github.com/user-attachments/assets/d9b11ca0-11da-4606-8de7-391ba1ef90f3" />

Подключаем к ArgoCD наш гит с использованием приватного ключа.
<img width="789" height="669" alt="image" src="https://github.com/user-attachments/assets/1ecb3853-1eb7-4f7e-8aea-1d79abde4e6f" />
<img width="1182" height="418" alt="image" src="https://github.com/user-attachments/assets/b5e8a031-f1b5-4066-a75a-cd874d68671f" />

Выбираем репозиторий, указываем ветку для отслеживания и путь к манифестам.
<img width="1096" height="699" alt="image" src="https://github.com/user-attachments/assets/072be709-857b-4771-ab3f-d5e1d88f481c" />
<img width="930" height="428" alt="image" src="https://github.com/user-attachments/assets/a843b5a7-1db4-492a-825e-e1e6e605a418" />

Указываем реквизиты кластера k8s и пространство имен.
<img width="927" height="331" alt="image" src="https://github.com/user-attachments/assets/45e68358-8604-45e0-90b3-2c790ced33e2" />

Подключение произошло.
<img width="1193" height="603" alt="image" src="https://github.com/user-attachments/assets/463a49a0-895f-4f3e-ab4b-8e47f9f8ae2b" />

Создаем индексный файл и правим докерфайл, пушим в ветку dev.
<img width="742" height="114" alt="image" src="https://github.com/user-attachments/assets/ecfea6ad-aedd-4876-b0d4-c4f77ede3c5d" />
<img width="728" height="397" alt="image" src="https://github.com/user-attachments/assets/5352d471-ea92-4138-9671-e93fd2ddb436" />

Делаем pull-request и merge после успешных тестов.
<img width="1280" height="573" alt="image" src="https://github.com/user-attachments/assets/48153a4b-da78-4707-bdc3-93b77ca7068e" />
<img width="1280" height="502" alt="image" src="https://github.com/user-attachments/assets/634f3dcc-db8d-4754-bd48-bcdb81bdfb5e" />
<img width="1211" height="479" alt="image" src="https://github.com/user-attachments/assets/3e096647-9dab-4a14-ba72-57d8cbd62aed" />

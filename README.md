# Описание проекта

Yatube - это социальная сеть для публикации постов и общения. С помощью Yatube вы можете зарегистрироваться, создать свой профиль, публиковать посты с текстом и изображениями, а также комментировать и подписываться на посты других пользователей.

Проект Yatube решает задачу предоставления пользователю возможности обмениваться информацией, мнениями и идеями в удобном формате, а также находить интересных авторов и следить за их творчеством.

Польза проекта заключается в том, что он предоставляет удобный и простой способ для общения и публикации контента. С помощью Yatube вы можете быстро и легко поделиться своими мыслями, идеями и изображениями, а также узнать мнения и комментарии других пользователей.

# Установка

Чтобы развернуть проект на локальной машине, выполните следующие шаги:

```bash
git clone https://github.com/<your_username>/yatube.git
```
```bash
cd yatube
```
```bash
python -m venv venv
source venv/bin/activate
```
```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py runserver
```
http://localhost:8000/

# Примеры

Для работы с API проекта Yatube вы можете использовать следующие примеры запросов:

 
```bash
1. GET /api/v1/posts/
```

```bash
2. POST /api/v1/posts/
{
    "text": "Текст нового поста",
    "image": "image.jpg"
}
```

```bash
3. PUT /api/v1/posts/<post_id>/
{
    "text": "Новый текст поста",
    "image": "new_image.jpg"
}
```

```bash
4. DELETE /api/v1/posts/<post_id>/
```

Это лишь некоторые из возможностей API проекта Yatube, для более подробной информации и примеров запросов смотрите документацию к API.
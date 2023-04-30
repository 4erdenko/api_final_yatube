# Project Description

Yatube is a social network for posting content and communication. With Yatube, you can register, create a profile, publish posts with text and images, and comment and follow other users' posts.

The Yatube project aims to provide users with the ability to exchange information, opinions, and ideas in a convenient format, as well as find interesting authors and follow their creative work.

The benefit of the project is that it provides a simple and convenient way for communication and content sharing. With Yatube, you can quickly and easily share your thoughts, ideas, and images while discovering opinions and comments from other users.

# Installation

To deploy the project on a local machine, follow these steps:

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

# Examples

To interact with Yatube's API, you can use the following example requests:

```bash 
1. GET /api/v1/posts/
{
    "text" : "Post text",
    "image" : "image.jpg",
}
```

```bash
2. POST /api/v1/posts/
{
    "text": "New post text",
    "image": "image.jpg"
}
```

```bash
3. PUT /api/v1/posts/<post_id>/
{
    "text": "Updated post text",
    "image": "new_image.jpg"
}
```

```bash
4. DELETE /api/v1/posts/<post_id>/
200 OK
```

These are just some of the capabilities of Yatube's API. For more detailed information and request examples, see the API documentation.

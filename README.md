# Project Description

YatubeAPI is an integral part of a broader social networking project, serving as its API for content posting and communication. By registering and creating a profile, users can publish text and image posts, as well as comment and follow posts from other users.


The primary objective of the Yatube API is to facilitate the exchange of information, views, and ideas in a streamlined format. It enables users to find interesting authors and stay updated on their creative work.


This API enhances the main project by providing a straightforward and convenient platform for communication and content sharing. With Yatube, users can swiftly share their thoughts, ideas, and images, and engage with feedback from the community. It's an essential component, contributing to the dynamic interaction of the overall project.

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

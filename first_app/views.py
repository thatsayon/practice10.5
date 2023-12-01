from django.shortcuts import render
from datetime import datetime
def blog(request):
    data = {
        "blog": [
            {
                "title": "How to install linux",
                "content": "Installing linux is a easy step but many beginners think it's a hard job to do. But it's not. All you need is an iso file and pendrive.",
                "img_url": "https://pakhotin.org/wp-content/uploads/2023/07/53113-106400-Linux-xl-1024x576.jpg",
                "keyword": ["linux", "install", "how"],
                "date": datetime.now()
            },
            {
                "title": "What is python?",
                "content": "Python is high level, object oriented programming language. And it's also one of the most famous programming language",
                "img_url": "https://onlinedegrees.sandiego.edu/wp-content/uploads/2023/05/6-careers-you-can-get-with-python.jpg",
                "keyword": ["python", "language", "programming"],
                "date": datetime.now()
            }
        ]
    }
    return render(request, 'blog.html', data)
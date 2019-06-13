from django.shortcuts import render

posts = [
    {
        'author': 'Michael Le',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 15, 2019'
    },
    {
        'author': 'Phucanese Le',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 16, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

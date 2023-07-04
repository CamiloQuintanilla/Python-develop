from django.shortcuts import render, HttpResponse

# Create your views here.
layout = """
    <ul>
        <li><a href="/index">Home</a></li>
        <li><a href="/hola_mundo">Content</a></li>
        <li><a href="/about_me">About Me</a></li>
    </ul>
"""
def index(request):

    header = """
        <ul>
            <li><a href="/index">Home</a></li>
            <li><a href="/hola_mundo">Content</a></li>
            <li><a href="/about_me">About Me</a></li>
        </ul>
    """
    return HttpResponse(header)

def hello_word(request):
    return HttpResponse(layout+"""
        <h1>Hola Django !!</h1>
        <h3>Soy Camilo :)</h3>
        <p>Back Developer</p>
    """)

def page(resques):
    return HttpResponse(layout+"""
        <h1>El mejor en lo que hago</h1>
    """)
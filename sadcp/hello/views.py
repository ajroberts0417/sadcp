from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Views for basic hello world


def hello_view(request: HttpRequest) -> HttpResponse:

    return render(request, "hello/hello.html")

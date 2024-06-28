from django.shortcuts import render

# Create your views here.
def lending_page(request):
    render(request, 'lending_page.html')

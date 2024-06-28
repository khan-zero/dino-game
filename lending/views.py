from django.shortcuts import render

def lending_page(request):
    return render(request, 'lending/lending_page.html')

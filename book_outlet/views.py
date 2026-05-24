from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Book 
# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request,"book_outlets/index.html", {
        "books":books
    })

def book_detail(request, slug):
    
    # try:
    #     book =Book.objects.get(id=id)
    # except:
    #     raise Http404()

    book = get_object_or_404(Book, slug=slug) # can use pk = id as well, pk is primary key
    return render(request, "book_outlets/book_detail.html", {
        "title": book.title, 
        "author":book.author, 
        "rating":book.rating, 
        "is_bestseller":book.is_bestselling
    })
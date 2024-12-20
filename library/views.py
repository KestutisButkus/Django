from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Book, Author, BookInstance, Genre


def index(request):
    # Suskaičiuokime keletą pagrindinių objektų
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Laisvos knygos (tos, kurios turi statusą 'g')
    num_instances_available = BookInstance.objects.filter(status__exact='g').count()

    # Kiek yra autorių
    num_authors = Author.objects.count()

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    # return render(request, 'library/index.html', context=context)
    return render(request, 'index.html', context=context)


def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    # print(authors)
    return render(request, 'authors.html', context=context)

def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author.html', {'author': single_author})

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'

# class BookListView(generic.ListView):
#     model = Book
#     # patys galite nustatyti šablonui kintamojo vardą
#     context_object_name = 'my_book_list'
#     # gauti sąrašą 3 knygų su žodžiu pavadinime 'ir'
#     queryset = Book.objects.filter(title__icontains='ir')[:3]
#     # šitą jau panaudojome. Neįsivaizduojate, kokį default kelią sukuria :)
#     template_name = 'books/my_arbitrary_template_name_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
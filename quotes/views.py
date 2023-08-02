from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuoteForm, AuthorForm, TagForm
from .models import Author, Quote
from .utils import get_mongodb
from bson.objectid import ObjectId


def main(request, page=1):
    # db = get_mongodb()
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)

    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author_detail(request, id):
    author = get_object_or_404(Author, pk=id)
    return render(request, 'quotes/author_detail.html', {'author': author})


# def author_about(request, _id):
#     print(_id)
#     author = Author.objects.get(pk=_id)
#
#     return render(request, 'quotes:author_detail.html', context={'author': author})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_quote.html', context={'form': QuoteForm(), 'message': 'Form not valid'})

    return render(request, 'quotes/add_quote.html', context={'form': QuoteForm()})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to='quotes:root')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})


def first_page(request):
    return redirect('quotes:root_paginate', page=1)

def last_page(request):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    last_page_number = paginator.num_pages
    return redirect('quotes:root_paginate', page=last_page_number)
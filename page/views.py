from django.shortcuts import render, redirect
from accaunts.utils import check_login, admin_required
from page.forms import AddBook
from page.models import Books


@admin_required
def add_book(request):
    if request.method == 'POST':
        form=AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objects')
    else:
        form=AddBook()
    return render(request, 'visual/main.html', {'form':form})

def get_info(request):
    info=Books.objects.all()
    return render(request, 'visual/info.html', {'info': info})


def detail_book(request, pk):
    book = Books.objects.get(pk=pk)
    return render(request, 'visual/details.html', {'p':book})

@admin_required
def delete(request, pk):
    book = Books.objects.get(pk=pk)
    book.delete()
    return redirect('objects')


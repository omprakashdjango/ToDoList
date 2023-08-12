from django.shortcuts import render
from .models import Entry

# Create your views here.

def entry_list(request):
    context = {'entry_data': Entry.objects.all()}
    return render(request, 'entry/entry_list.html', context)

def single_entry(request, pk):
    single_entry_data = {"Id": None, "Subject": "Error 404", "Description": "This Page Does not exist"}
    if Entry.objects.get(id=pk):
        single_entry_data = Entry.objects.get(id=pk)

    context = {'single_entry': single_entry_data}
    return render(request, 'entry/single_entry.html', context)

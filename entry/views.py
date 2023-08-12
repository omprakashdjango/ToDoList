from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

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

# Create Entry To the To Do List
def create_entry(request):
    form = EntryForm()

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
        
    context = {'form': form}
    return render(request, 'entry/create_entry.html', context)

# Update Entry To the To Do List
def update_entry(request, pk):
    entry_data = Entry.objects.get(id=pk)
    form = EntryForm(instance=entry_data)

    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry_data)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    
    context = {'form': form}
    return render(request, 'entry/create_entry.html', context)

# Delete Entry To the To Do List
def delete_entry(request, pk):
    entry_data = Entry.objects.get(id=pk)
    if request.method == 'POST':
        entry_data.delete()
        return redirect('entry_list')
    context = {'entry': entry_data}
    return render(request, 'entry/delete_template.html', context)

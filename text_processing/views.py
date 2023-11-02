import tempfile
import os
from .models import _delete_file

from django.shortcuts import render, redirect, get_object_or_404
from .forms import TextUploadForm
from .models import Text
import random
import shutil


def handle_uploaded_file(f):
    with open('files/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def file_upload(request):
    if request.method == 'POST':
        form = TextUploadForm(request.POST, request.FILES)
        if form.is_valid():

            handle_uploaded_file(request.FILES['file'])
            name = request.FILES['file'].name
            form.save()



        return redirect('files:display', name)
    else:
        form = TextUploadForm()
    return render(request, 'texts/upload.html', {'form': form})


# def _delete_file(path):
#    """ Deletes file from filesystem. """
#    if os.path.isfile(path):
#        os.remove(path)


def display(request, name):
    data_file = open('files/' + name, 'r', encoding='utf-8-sig')
    data = data_file.read()
    shuffle_list = []
    split_data = data.split()
    for word in split_data:
        if len(word) > 1:
            new_word = ''
            new_word += word[0]
            random_sample = random.sample(word[1:-1], len(word[1:-1]))

            for char_random_sample in random_sample:
                new_word += char_random_sample
            new_word += word[-1]
            shuffle_list.append(new_word)
        else:
            shuffle_list.append(word)

    _delete_file('files/' + name,)

    return render(request, 'texts/display.html', {'name': shuffle_list})

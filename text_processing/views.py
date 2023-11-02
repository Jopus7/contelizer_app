from django.shortcuts import render
from .forms import TextUploadForm
import random


def file_upload(request):
    if request.method == 'POST':
        form = TextUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES.get('file')
            data = uploaded_file.read().decode('utf-8-sig')
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
            return render(request, 'texts/display.html', {'name': shuffle_list})
    else:
        form = TextUploadForm()
    return render(request, 'texts/upload.html', {'form': form})



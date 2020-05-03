from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'counterword/home.html')

def about(request):
    return render(request, 'counterword/about.html')

def count(request):
    text = request.GET['fulltext']
    words =text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1


    return render(request, 'counterword/count.html', {'fulltext': text, 'total': len(words), 'dictionary':word_dictionary.items()})


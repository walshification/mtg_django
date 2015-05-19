from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {
        'new_deck_text': request.POST.get('deck_text', ''),
    })

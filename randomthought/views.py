from django.shortcuts import render


def random(request):
    return render(
        request,
        'randomthought/thought.html'

    )

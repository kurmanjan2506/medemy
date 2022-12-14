from .utils import get_turn_info
from django.shortcuts import render, redirect


def peer1(request):
    context = get_turn_info()
    return render(request, 'chat/peer1.html', context=context)


def peer2(request):
    context = get_turn_info()
    return render(request, 'chat/peer2.html', context=context)


def peer(request):
    context = get_turn_info()
    print('context: ', context)
    return render(request, 'chat/peer.html', context=context)
import requests as re
from django.shortcuts import render, redirect

from apps.teachers.models.comments import CommentsModel
from dashboard.comment.forms import CommentForm


def comment(requests):
    root = CommentsModel.objects.all()
    ctx = {
        'root': root
    }
    return render(requests, 'dashboard/commend/commend.html', ctx)


def commend_add(requests):
    forms = CommentForm()
    if requests.POST:
        form = CommentForm(requests.POST, requests.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('dash_comment')
    ctx = {
        "forms": forms
    }
    return render(requests, f"dashboard/commend/form.html", ctx)


def commend_edit(requests, pk):
    if pk:
        root = CommentsModel.objects.get(pk=pk)
        forms = CommentForm(instance=root)
    else:
        raise ValueError('topilmadi 404')
    if requests.POST:
        form = CommentForm(requests.POST, requests.FILES or None, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_comment_edit')
        else:
            print(form.errors)

    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/commend/form.html', ctx)

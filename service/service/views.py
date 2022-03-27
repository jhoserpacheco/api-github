from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.expressions import Subquery
from django.http import HttpResponse
from django.http.response import FileResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from .api import get_repos, info_repo, info_user

class GithubView(View):
    def get(self, request, user, *args, **kwargs):
        return HttpResponse(info_user(user), content_type='application/json')

class Repository(View):
    def get(self, request, user, repository, *args, **kwargs):
        return HttpResponse(info_repo(user, repository), content_type='application/json')
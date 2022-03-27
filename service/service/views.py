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
        lista = get_repos(user)
        context={'user': user,
                'get_user': info_user(user).json(), 
                'repos': lista,
                'size': len(lista)
                }
        return HttpResponse(request, 'index.html', context)

class Repository(View):
    def get(self, request, user, repository, *args, **kwargs):
        context={'user': user,
                'repository': repository,
                'info_repository': info_repo(user, repository)
                }
        return render(request, 'repository.html', context)
import os

from github import Github

token = os.getenv('GITHUB_TOKEN')

g = Github(token)

def info_user(user):
    usuario = g.get_user(user)
    user_dict = {}
    user_dict['IMG_URL'] = usuario.avatar_url
    user_dict['ID'] = usuario.id
    user_dict['BIO'] = usuario.bio
    user_dict['CREATED_AT'] = usuario.created_at
    user_dict['# FOLLOWERS'] = usuario.followers
    user_dict['# FOLLOWING'] = usuario.following
    
    return user_dict

def get_repos(user):
    repo = [x for x in g.get_user(user).get_repos()]
    return repo

def info_repo(user, repository):
    
    repo = g.get_repo(user+'/'+repository)
    stars = repo.stargazers_count
    contents =  [x.path for x in repo.get_contents("")]
    clone_url = repo.clone_url
    
    repository_dict = {}
    repository_dict['# STARS'] = stars
    repository_dict['CONTENTS'] = contents
    repository_dict['URL'] = clone_url
    repository_dict['CREATED_AT'] = repo.created_at
    repository_dict['# FORKS'] = repo.forks_count
    repository_dict['SIZE KB'] = repo.size
    
    return repository_dict
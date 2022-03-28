# Microservice with Django

### Description & Context

This project is developing in the Python language using Django and Docker container. It is a microservice that consumes the Github API to obtain user information and user repositories.

<hr>

### GET

##### Info User 
```
curl 127.0.0.1:8000/jhoserpacheco
```

```yaml
{
    "# FOLLOWERS": 17,
    "# FOLLOWING": 31,
    "# REPOS": [
        "jhoserpacheco/2048.cpp",
        "jhoserpacheco/api-github",
        "jhoserpacheco/Biblioteca",
        "jhoserpacheco/Curso-html-css",
        "jhoserpacheco/Data-Science--Cheat-Sheet",
        "jhoserpacheco/DS-Algo-Point",
        "jhoserpacheco/Email_master",
        "jhoserpacheco/github-readme-stats",
        "jhoserpacheco/GitHubGraduation-2021",
        "jhoserpacheco/Hack-CP-DSA",
        "jhoserpacheco/Hacktoberfest-21",
        "jhoserpacheco/hacktoberfest2K",
        "jhoserpacheco/idle_master_extended",
        "jhoserpacheco/jhoserpacheco",
        "jhoserpacheco/json",
        "jhoserpacheco/json-studiantes",
        "jhoserpacheco/learn-go-with-tests",
        "jhoserpacheco/mvc-php",
        "jhoserpacheco/nerfies",
        "jhoserpacheco/notebook",
        "jhoserpacheco/Solutions-Competitve-Programming",
        "jhoserpacheco/StringMatchingAlgorithms"
    ],
    "BIO": "Systems engineering student, Colombia, UFPS.\r\nSILUX - Competitive Programming ",
    "CREATED_AT": "01/11/2018",
    "ID": 44657472,
    "IMG_URL": "https://avatars.githubusercontent.com/u/44657472?v=4"
}
```

##### Info Repo 
```
curl -x 127.0.0.1:8000/jhoserpacheco/api-github
```

```yaml
{
    "# FORKS": 1,
    "# STARS": 1,
    "CONTENTS": [
        ".gitignore",
        "service"
    ],
    "CREATED_AT": "2022-03-18 02:30:29",
    "SIZE KB": 8,
    "URL": "https://github.com/jhoserpacheco/api-github.git"
}
```

<hr>

### Run project

Git clone this repository into your local machine.
```
git clone https://github.com/jhoserpacheco/api-github

cd api-github/service 
```

Execute container
```
docker-compose up
```

from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    title = ' Home'
    projects = Project.get_all()

    return render(request, 'index.html',{
        'title': title,
        'projects':projects,
    })
def all_repos(request):
    title = 'Repos'

    all_repos = requests.get('https://api.github.com/user/repos?sort=asc&access_token={}'.format(settings.GITHUB_API))
    repos = json.loads(all_repos.content)
    # print(repos)

    return render(request, 'repos.html', {
        'title':title,
        'repos':repos
    })
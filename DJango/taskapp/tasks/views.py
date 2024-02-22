from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nec neque venenatis, tristique ipsum nec, feugiat erat. Cras auctor vel arcu rhoncus mollis. Vivamus nec erat ac lorem blandit sollicitudin. Ut ac iaculis odio. Aenean ut sodales augue. Maecenas a dignissim risus. Cras et arcu suscipit, viverra nunc sit amet, ornare odio. Fusce vitae turpis felis.")

def task_list(request):
    ctx={
        "tasks": [
            'Task 1',
            'Task 2',
            'Task 3',
            'Task 4'
        ]
    }
    return render(request, 'task_list.html', ctx)
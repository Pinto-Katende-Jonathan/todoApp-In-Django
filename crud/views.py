from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render

from crud.models import Todo

# Create your views here.
def create_todo(request):
    # on récupère une todo title et on supprime les espces de début et fin
    todo = str(request.POST['todo-title']).strip()

    if todo:
        create_task = Todo(title=todo)
        create_task.save()
        return redirect('all_todos')
    else:
        return redirect('all_todos')

def all_todos(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos':todos})


def update_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
        return render(request, 'edit.html', {'todo': todo})
    except:
        raise Http404('Todo does not exist')

def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.title = request.POST['todo-title']
    todo.save()
    return redirect('all_todos')

def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return redirect('all_todos')    
    except:
        raise Http404('Todo does not exist')
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from todo_app.models import Todo
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'index.html', {
      "todo_items": todo_items
    })

@csrf_exempt # This decorator marks a view as being exempt from the protection ensured by the middleware
def add_todo(request):
  current_date = timezone.now()
  content = request.POST["content"]
  created_obj = Todo.objects.create(added_date=current_date, text=content)
  return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
  Todo.objects.get(id=todo_id).delete()
  return HttpResponseRedirect("/")
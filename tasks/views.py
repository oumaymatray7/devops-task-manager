from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def dashboard(request):
    if request.user.is_staff:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=request.user)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='Completed').count()
    pending_tasks = tasks.filter(status='Pending').count()
    in_progress_tasks = tasks.filter(status='In Progress').count()

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
    }

    return render(request, 'tasks/dashboard.html', context)


@login_required
def task_list(request):
    if request.user.is_staff:
        tasks = Task.objects.all().order_by('-created_at')
    else:
        tasks = Task.objects.filter(assigned_to=request.user).order_by('-created_at')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})
@login_required
def task_create(request):

    if not request.user.is_staff:
        messages.error(request, "Accès refusé : réservé à l'admin.")
        return redirect('task_list')

    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_update(request, id):

    if not request.user.is_staff:
        messages.error(request, "Accès refusé : réservé à l'admin.")
        return redirect('task_list')

    task = get_object_or_404(Task, id=id)

    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_delete(request, id):

    if not request.user.is_staff:
        messages.error(request, "Accès refusé : réservé à l'admin.")
        return redirect('task_list')

    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/task_delete.html', {'task': task})
@login_required
def update_status(request, id):

    task = get_object_or_404(Task, id=id)

    if not request.user.is_staff and task.assigned_to != request.user:
        messages.error(request, "Accès refusé.")
        return redirect('task_list')

    if request.method == 'POST':
        new_status = request.POST.get('status')
        task.status = new_status
        task.save()

    return redirect('task_list')
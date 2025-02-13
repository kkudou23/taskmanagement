from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from django.http import Http404
from .models import Task
# from .forms import CreateTaskForm

class ListTaskView(LoginRequiredMixin, generic.ListView):
    template_name = 'task/task_list.html'
    model = Task
    context_object_name = 'task_context'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = self.request.GET.get('status', None)           # GETパラメータstatusの値を取得
        priority = self.request.GET.get('priority', None)       # GETパラメータpriorityの値を取得

        task_context = Task.objects.filter(author=self.request.user)    # ①:今ログインしているユーザーが作成したタスクを取得

        if status == 'completed':                                       # ②:GETパラメータstatusの値によって絞り込み
            task_context = task_context.filter(status=True)                 # 完了したタスク
        elif status == 'incomplete':
            task_context = task_context.filter(status=False)                # 未完のタスク

        if priority == 'high':                                          # ③:GETパラメータpriorityの値によって絞り込み
            task_context = task_context.filter(priority=1)                  # 優先度 : 高
        elif priority == 'medium':
            task_context = task_context.filter(priority=2)                  # 優先度 : 中
        elif priority == 'low':
            task_context = task_context.filter(priority=3)                  # 優先度 : 低

        task_context = task_context.order_by('priority', 'deadline')    # ④:③を「優先度が高い順(1:高→3:低)」と「締切順(1/1→12/31)」でソート

        paginator = Paginator(task_context, 5)                  # ページネーション(1ページに5件表示)
        page_number = self.request.GET.get('page')
        context['task_context'] = paginator.get_page(page_number)

        return context

class DetailTaskView(LoginRequiredMixin, generic.DetailView):
    template_name = 'task/task_detail.html'
    model = Task
    context_object_name = 'Task'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('閲覧権限がありません。')
        elif not obj:
            raise Http404('アクセスできないURLか、ページが削除されています。')
        return super(DetailTaskView, self).dispatch(request, *args, **kwargs)
    

class CreateTaskView(LoginRequiredMixin, generic.edit.CreateView):
    template_name = 'task/task_create.html'
    model = Task
    context_object_name = 'Task'
    success_url = reverse_lazy('list-task')
    fields = ('title', 'status', 'priority', 'deadline', 'text')
    # form_class = CreateTaskForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateTaskView, self).form_valid(form)

class DeleteTaskView(LoginRequiredMixin, generic.edit.DeleteView):
    template_name = 'task/task_confirm_delete.html'
    model = Task
    context_object_name = 'Task'
    success_url = reverse_lazy('list-task')

class UpdateTaskView(LoginRequiredMixin, generic.edit.UpdateView):
    template_name = 'task/task_update.html'
    model = Task
    context_object_name = 'Task'
    success_url = reverse_lazy('list-task')
    fields = ('title', 'status', 'priority', 'deadline', 'text')

def custom_permission_denied_view(request, exception):
    return render(request, '403.html', {'error_message': str(exception)}, status=403)

def custom_page_not_found_view(request, exception):
    return render(request, '404.html', {'error_message': str(exception)}, status=404)
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Manager, StaffManager


class ManagerListView(ListView):
    model = Manager
    fields = '__all__'
    template_name = 'managers/manager_list.html'

    def get_context_data(self, **kwargs):
        context = super(ManagerListView, self).get_context_data(**kwargs)
        context['manager'] = Manager.objects.all().order_by('created')
        return context


class ManagerCreateView(CreateView):
    model = Manager
    fields = '__all__'
    queryset = Manager.objects.all()


class ManagerDetailView(DetailView):
    model = Manager
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ManagerDetailView, self).get_context_data(**kwargs)
        context['manager'] = Manager.objects.get(name=self.object)
        return context


class ManagerUpdateView(UpdateView):
    model = Manager
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ManagerUpdateView, self).get_context_data(**kwargs)
        context['manager'] = Manager.objects.get(name=self.object)
        return context


class ManagerDeleteView(DeleteView):
    model = Manager
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ManagerDeleteView, self).get_context_data(**kwargs)
        context['manager'] = Manager.objects.get(name=self.object)
        return context

    def get_success_url(self):
        return reverse('list')


class StaffManagerListView(ListView):
    model = StaffManager
    fields = '__all__'
    template_name = 'managers/staffmanager_list.html'

    def get_context_data(self, **kwargs):
        context = super(StaffManagerListView, self).get_context_data(**kwargs)
        context['staff_manager'] = StaffManager.objects.all().order_by('manager_name_id')
        return context


class StaffManagerCreateView(CreateView):
    model = StaffManager
    fields = '__all__'
    queryset = StaffManager.objects.all()


class StaffManagerDetailView(DetailView):
    model = StaffManager
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(StaffManagerDetailView, self).get_context_data(**kwargs)
        context['manager'] = StaffManager.objects.get(id=self.object.id)
        return context


class StaffManagerUpdateView(UpdateView):
    model = StaffManager
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(StaffManagerUpdateView, self).get_context_data(**kwargs)
        context['manager'] = StaffManager.objects.get(id=self.object.id)
        return context


class StaffManagerDeleteView(DeleteView):
    model = Manager
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(StaffManagerDeleteView, self).get_context_data(**kwargs)
        context['manager'] = StaffManager.objects.get(manager_name_id=self.object.pk)
        return context

    def get_success_url(self):
        return reverse('staff_list')


from django.shortcuts import render, redirect
from .forms import EBordForm
from .models import EBordModel, CategoryModel
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from django.contrib.auth.decorators import user_passes_test
from django.contrib.messages.views import SuccessMessageMixin


class CategoryView(ListView):
    model = CategoryModel
    template_name = 'eBord/home.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryAddView(UserPassesTestMixin, CreateView):
    model = CategoryModel
    success_url = reverse_lazy('home')
    fields = ('name', 'image')
    template_name = 'eBord/add_cat.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class ByCategoryView(ListView):
    template_name = 'eBord/by_category.html'
    context_object_name = 'items'
    paginate_by = 6

    def get_queryset(self):
        return EBordModel.objects.filter(category=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = CategoryModel.objects.get(pk=self.kwargs['pk'])
        return context


class ByUserView(ListView):
    template_name = 'eBord/by_user.html'
    context_object_name = 'items'
    paginate_by = 6

    def get_queryset(self):
        return EBordModel.objects.filter(author=self.kwargs['pk'])


class EBordView(ListView):
    model = EBordModel
    template_name = 'eBord/all_ads.html'
    context_object_name = 'items'
    paginate_by = 6


class EBordAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'eBord/add.html'
    form_class = EBordForm
    initial = {'price': 0.00}
    success_message = f'Объявление успешно создано'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание объявления'
        return context

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})


class EBordDetailView(DetailView):
    template_name = 'eBord/detail.html'
    context_object_name = 'item'

    def get_queryset(self):
        return EBordModel.objects.filter(pk=self.kwargs['pk'])


class EBordUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    template_name = 'eBord/add.html'
    form_class = EBordForm
    success_message = 'Объявление успешно отредактировано'

    def get_queryset(self):
        return EBordModel.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование объявления'
        return context

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.kwargs['pk']})

    def test_func(self):
        ads = self.get_object()
        if self.request.user == ads.author or self.request.user.is_staff:
            return True
        else:
            return False


class EBordDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    template_name = 'eBord/delete.html'
    model = EBordModel
    success_url = reverse_lazy('all_ads')
    success_message = 'Объявление успешно удалено'

    def get_queryset(self):
        return EBordModel.objects.filter(pk=self.kwargs['pk'])

    def test_func(self):
        ads = self.get_object()
        if self.request.user == ads.author or self.request.user.is_staff:
            return True
        else:
            return False


@user_passes_test(lambda user: user.is_staff)
def category_change(request):
    CategoryFormSet = forms.modelformset_factory(
        model=CategoryModel,
        fields='__all__',
        labels={'name': 'Название категории', 'image': 'Изображении'},
        can_delete=True
    )
    if request.method == 'POST':
        formset = CategoryFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    else:
        formset = CategoryFormSet()
    context = {'formset': formset}
    return render(request, 'eBord/change-cat.html', context)

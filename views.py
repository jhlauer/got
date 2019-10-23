from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from django.http import HttpResponse
# from django.template.loader import render_to_string
from APPNAME.models import Model_1, Model_2
from APPNAME.forms import Model_1Form

# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        m1c = Model_1.objects.all().count();
        m2l = Model_2.objects.all();

        ctx = { 'model_1_count': tc, 'model2_list': sl };
        return render(request, 'APPNAME/model2_list.html', ctx)

class Model_1View(LoginRequiredMixin,View) :
    def get(self, request):
        tl = Model_1.objects.all();
        ctx = { 'model_1_list': tl };
        return render(request, 'APPNAME/model_1_list.html', ctx)

# We use reverse_lazy() because we are in "constructor code"
# that is run before urls.py is cmopletely loaded
class Model_1Create(LoginRequiredMixin, View):
    model = Model_1
    template = 'APPNAME/model_1_form.html'
    success_url = reverse_lazy('APPNAME:all')
    def get(self, request) :
        form = TypeForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = Model_1Form(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        model_1 = form.save()
        return redirect(self.success_url)

class Model_1Update(LoginRequiredMixin, View):
    model = Model_1
    success_url = reverse_lazy('APPNAME:all')
    template = 'APPNAME/model_1_form.html'
    def get(self, request, pk) :
        model_1 = get_object_or_404(self.model, pk=pk)
        form = Model_1Form(instance=model_1)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        model_1 = get_object_or_404(self.model, pk=pk)
        form = Model_1Form(request.POST, instance = model_1)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class Model_1Delete(LoginRequiredMixin, DeleteView):
    model = model_1
    success_url = reverse_lazy('APPNAME:all')
    template = 'APPNAME/model_1_confirm_delete.html'

    def get(self, request, pk) :
        model_1 = get_object_or_404(self.model, pk=pk)
        form = Model_1Form(instance=model_1)
        ctx = { 'model_1': model_1 }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        model_1 = get_object_or_404(self.model, pk=pk)
        model_1.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
class Model_2Create(LoginRequiredMixin,CreateView):
    model = model_2
    fields = '__all__'
    success_url = reverse_lazy('APPNAME:all')

class Model_2Update(LoginRequiredMixin, UpdateView):
    model = model_2
    fields = '__all__'
    success_url = reverse_lazy('APPNAME:all')

class Model_2Delete(LoginRequiredMixin, DeleteView):
    model = model_2
    fields = '__all__'
    success_url = reverse_lazy('APPNAME:all')

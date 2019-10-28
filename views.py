from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string
from got.models import House, Character, Culture, Title
from got.forms import HouseForm, CultureForm, TitleForm

# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        hc = House.objects.all().count()
        cc = Culture.objects.all().count()
        tc = Title.objects.all().count()
        cl = Character.objects.all()

        ctx = { 'house_count': hc, 'title_count': tc, 'culture_count': cc, 'character_list': cl }
        return render(request, 'got/character_list.html', ctx)

class HouseView(LoginRequiredMixin,View) :
    def get(self, request):
        hl = House.objects.all()
        ctx = { 'house_list': hl }
        return render(request, 'got/house_list.html', ctx)

class CultureView(LoginRequiredMixin,View) :
    def get(self, request):
        cl = Culture.objects.all()
        ctx = { 'culture_list': cl }
        return render(request, 'got/culture_list.html', ctx)

class TitleView(LoginRequiredMixin,View) :
    def get(self, request):
        tl = Title.objects.all()
        ctx = { 'title_list': tl }
        return render(request, 'got/title_list.html', ctx)

# House 
class HouseCreate(LoginRequiredMixin, View):
    model = House
    template = 'got/house_form.html'
    success_url = reverse_lazy('got:all')
    def get(self, request) :
        form = HouseForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = HouseForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        house = form.save()
        return redirect(self.success_url)

class HouseUpdate(LoginRequiredMixin, View):
    model = House
    success_url = reverse_lazy('got:all')
    template = 'got/house_form.html'
    def get(self, request, pk) :
        house = get_object_or_404(self.model, pk=pk)
        form = HouseForm(instance=house)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        house = get_object_or_404(self.model, pk=pk)
        form = HouseForm(request.POST, instance = house)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class HouseDelete(LoginRequiredMixin, DeleteView):
    model = House
    success_url = reverse_lazy('got:all')
    template = 'got/house_confirm_delete.html'

    def get(self, request, pk) :
        house = get_object_or_404(self.model, pk=pk)
        form = HouseForm(instance=house)
        ctx = { 'house': house }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        house = get_object_or_404(self.model, pk=pk)
        house.delete()
        return redirect(self.success_url)

# Title
class TitleCreate(LoginRequiredMixin, View):
    model = Title
    template = 'got/title_form.html'
    success_url = reverse_lazy('got:all')
    def get(self, request) :
        form = TitleForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = TitleForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        title = form.save()
        return redirect(self.success_url)

class TitleUpdate(LoginRequiredMixin, View):
    model = Title
    success_url = reverse_lazy('got:all')
    template = 'got/title_form.html'
    def get(self, request, pk) :
        title = get_object_or_404(self.model, pk=pk)
        form = TitleForm(instance=title)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        title = get_object_or_404(self.model, pk=pk)
        form = TitleForm(request.POST, instance = title)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class TitleDelete(LoginRequiredMixin, DeleteView):
    model = Title
    success_url = reverse_lazy('got:all')
    template = 'got/title_confirm_delete.html'

    def get(self, request, pk) :
        title = get_object_or_404(self.model, pk=pk)
        form = TitleForm(instance=title)
        ctx = { 'title': title }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        title = get_object_or_404(self.model, pk=pk)
        title.delete()
        return redirect(self.success_url)

# Culture 
class CultureCreate(LoginRequiredMixin, View):
    model = Culture
    template = 'got/culture_form.html'
    success_url = reverse_lazy('got:all')
    def get(self, request) :
        form = CultureForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = CultureForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        culture = form.save()
        return redirect(self.success_url)

class CultureUpdate(LoginRequiredMixin, View):
    model = Culture
    success_url = reverse_lazy('got:all')
    template = 'got/culture_form.html'
    def get(self, request, pk) :
        culture = get_object_or_404(self.model, pk=pk)
        form = CultureForm(instance=culture)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        culture = get_object_or_404(self.model, pk=pk)
        form = CultureForm(request.POST, instance = culture)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class CultureDelete(LoginRequiredMixin, DeleteView):
    model = Culture
    success_url = reverse_lazy('got:all')
    template = 'got/culture_confirm_delete.html'

    def get(self, request, pk) :
        culture = get_object_or_404(self.model, pk=pk)
        form = CultureForm(instance=culture)
        ctx = { 'culture': culture }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        culture = get_object_or_404(self.model, pk=pk)
        culture.delete()
        return redirect(self.success_url)

# Character
class CharacterCreate(LoginRequiredMixin,CreateView):
    model = Character
    fields = '__all__'
    success_url = reverse_lazy('got:all')

class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    fields = '__all__'
    success_url = reverse_lazy('got:all')

class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Character
    fields = '__all__'
    success_url = reverse_lazy('got:all')

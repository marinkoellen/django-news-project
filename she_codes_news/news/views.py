from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import NewsStory
from .forms import StoryForm,StoryFormChangeForm,UserDeleteForm
from django.contrib.auth import get_user_model
from users.models import CustomUser, Cuisine_CHOICES
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
User = CustomUser

def LikeView(request, pk):
    newsstory = get_object_or_404(NewsStory,pk=pk)
    newsstory.likes.add(request.user)
    return HttpResponseRedirect(reverse('news:story',args=[str(pk)]))


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        context['categories'] = NewsStory.cuisine_type.field.choices
        return context

class ALLIndexView(generic.ListView):
    template_name = 'news/category_page.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        context['categories'] = NewsStory.cuisine_type.field.choices
        return context

class CategoryFilterView(generic.ListView):
    template_name = 'news/category_page.html'
    context_object_name = 'all_stories'
    slug_field = "cuisine_type"
    slug_url_kwarg = "cuisine_type"

    def get_queryset(self):
        '''Return all news stories.'''
        qs = NewsStory.objects.all()
        q = self.request.GET.get("cuisine_type")
        if q:
            qs =qs.filter(cuisine_type = q)
        return qs

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['form'] = StoryForm
            context['categories'] = Cuisine_CHOICES
            return context




class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            stuff = get_object_or_404(NewsStory, id=self.kwargs['pk'])
            total_likes = stuff.total_likes()
            context['total_likes'] = total_likes
            context['categories'] = NewsStory.cuisine_type.field.choices
            return context

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = StoryForm.Cuisine_CHOICES
        return context
 


class EditStoryView(generic.edit.UpdateView):
    model = NewsStory
    form_class =  StoryFormChangeForm
    context_object_name = 'storyForm'
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = NewsStory.cuisine_type.field.choices
        return context



class OneAuthorView(generic.DetailView):
    model = User
    template_name = 'news/one_author.html'
    slug_field = "username"
    slug_url_kwarg = "username"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = User.Cuisine_CHOICES
        return context    

class DeleteStoryView(generic.edit.DeleteView):
    model = NewsStory
    form_class =  UserDeleteForm
    context_object_name = 'storyForm'
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = NewsStory.cuisine_type.field.choices
        return context
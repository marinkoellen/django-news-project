from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm,StoryFormChangeForm,UserDeleteForm
from django.contrib.auth import get_user_model
from users.models import CustomUser

User = CustomUser

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditStoryView(generic.edit.UpdateView):
    model = NewsStory
    form_class =  StoryFormChangeForm
    context_object_name = 'storyForm'
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')



class OneAuthorView(generic.DetailView):
    model = User
    template_name = 'news/one_author.html'
    slug_field = "username"
    slug_url_kwarg = "username"
    


class DeleteStoryView(generic.edit.DeleteView):
    model = NewsStory
    form_class =  UserDeleteForm
    context_object_name = 'storyForm'
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')
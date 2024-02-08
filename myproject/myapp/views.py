from django.shortcuts import render
from django.views.generic import ListView, DetailView   
from .models import Post, summary

class HomeView(ListView):
    model = Post  # Define the model for the queryset
    template_name = 'home.html' 
    context_object_name = 'posts'  # Set a context object name to use in the template
    
    def get_queryset(self):
        return Post.objects.all()  # Define the queryset explicitly
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summaries'] = summary.objects.all()  # Add summaries to the context
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

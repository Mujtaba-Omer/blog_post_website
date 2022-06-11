

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
	context = {
		'posts' : post.objects.all()
	}
	return render(request, 'blog/home.html', context )


class ProfileListView(ListView):
	model = post
	template_name = 'blog/home.html' #<app>/<model>_<view type>.html
	context_object_name =  'posts'
	ordering = ['-date_posted']
	paginate_by = 5


class UserListView(ListView):
	model = post
	template_name = 'blog/user_post.html' #<app>/<model>_<view type>.html
	context_object_name =  'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username = self.kwargs.get('username'))
		return post.objects.filter(author=user).order_by('-date_posted')


class ProfileDetailView(DetailView):
	model = post


class ProfileCreateView(LoginRequiredMixin, CreateView):
	model = post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html', {'title' : 'about'})
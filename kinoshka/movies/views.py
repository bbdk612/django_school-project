from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from django.db.models import Q

from .models import Movies, Category, Actors
from .forms import RevieweForm

def index(request):
	"""Контроллер для нчатльной страницы"""
	template = 'index.html'
	movies = Movies.objects.filter(draft=False)[:10][::-1]
	category = Category.objects.all()[:5]
	context = {'movies': movies, 'categories': category}
	return render(request, template, context)

class MovieDetail(DetailView):
	"""Контроллер для детального представления модели Movie"""
	model = Movies
	slug_field = 'url'

class ActorsDetail(DetailView):
	"""Контроллер для детального представления модели Actors"""
	model = Actors
	slug_field = 'name'

class AddReview(View):
	"""Контроллер для добавления комментариев на сайт"""
	def post(self, request, pk):
		form = RevieweForm(request.POST)
		movie = Movies.objects.get(id=pk)
		if form.is_valid():
			post = form.save(commit=False)
			if request.POST.get("parent", None):
				post.parent_id = int(request.POST.get('parent'))
			post.movie = movie
			post.save()
		return redirect(movie.get_absolute_url())

class SearchView(ListView):
	"""Контроллер для пиоска фильмов на сайте"""


	def get_queryset(self):
		
		return Movies.objects.filter(
			Q(title__icontains=self.request.GET.get('q').title())|
			Q(title__icontains=self.request.GET.get('q').lower())|
			Q(actor__name__icontains=self.request.GET.get('q').title())|
            Q(actor__name__icontains=self.request.GET.get('q').lower())|
			Q(directors__name__icontains=self.request.GET.get('q').title())|
            Q(directors__name__icontains=self.request.GET.get('q').lower())).distinct()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['q'] = f'q={self.request.GET.get("q")}&'
		context['q_show'] = self.request.GET.get("q")
		return context

from django.urls import path

from .views import index, MovieDetail, AddReview, SearchView, ActorsDetail

urlpatterns = [
	path('', index, name='index'),
	path('search/', SearchView.as_view(), name="search" ),
	path('<slug:slug>/', MovieDetail.as_view(), name="movie__detail"),
	path('review/<int:pk>', AddReview.as_view(), name="add__review"),
	path('actor/<str:slug>/', ActorsDetail.as_view(), name='actors__detail'),
	
]
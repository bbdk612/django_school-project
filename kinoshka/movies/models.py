from django.db import models
from datetime import date
from django.urls import reverse

class Category(models.Model):
	""" Категории """
	
	name = models.CharField("Категория", max_length=50)
	description = models.TextField('Описание')
	url = models.SlugField(max_length=160, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

class Actors(models.Model):
	""" Актеры и режисеры """
	name = models.CharField('Имя', max_length=100)
	age = models.PositiveSmallIntegerField("Возраст", default=0)
	description = models.TextField('Описание')
	image = models.ImageField("Изображение", upload_to='static/actors/')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Актер'
		verbose_name_plural='Актеры'


class Genre(models.Model):
	""" Жанры """

	name = models.CharField("Название", max_length=50)
	description = models.TextField('Описание')
	url = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Жанр'
		verbose_name_plural='Жанры'

class Movies(models.Model):
	""" Кинчик """

	title = models.CharField('Название', max_length=250)
	tagline = models.CharField('Слоган', max_length=200, default='')
	description = models.TextField('Описание')
	poster = models.ImageField('Постер', upload_to='static/movies/')
	year = models.PositiveSmallIntegerField('Год выхода', default=1896)
	country = models.CharField('Страна', max_length=50)

	directors = models.ManyToManyField(Actors, verbose_name='Режисер', related_name='director')
	actor = models.ManyToManyField(Actors, verbose_name='Актер', related_name='actor')
	genre = models.ManyToManyField(Genre, verbose_name='Жанр')

	world_premiere = models.DateField("Премьера в мире", default=date.today)

	budget = models.PositiveIntegerField('Бюджет', default=0, help_text='в долларах США')

	fees_in_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='в долларах США')
	fees_in_world = models.PositiveIntegerField('Сборы в мире', default=0, help_text='в долларах США')

	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)

	url = models.SlugField(max_length=160, unique=True)

	draft = models.BooleanField("Редактировать",default=False)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Фильм'
		verbose_name_plural='Фильмы'

	def get_absolute_url(self):
		return reverse("movie__detail", kwargs={"slug": self.url})

	def get_reviews(self):
		return self.reviewe_set.filter(parent__isnull=True)


class Reviewe(models.Model):
	"""Отзывы/Рецензии"""
	name = models.CharField('Имя пользователя', max_length=50)
	email = models.EmailField()
	message = models.TextField('Рецензия', max_length=50000)
	parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, null=True, blank=True)
	movie = models.ForeignKey(Movies, verbose_name='Фильм', on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} - {self.movie}"

	class Meta:
		verbose_name='Рецензия'
		verbose_name_plural='Рецензии'

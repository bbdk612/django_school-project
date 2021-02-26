from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Actors, Genre, Category, Movies, Reviewe


@admin.register(Actors)
class ActorAdmin(admin.ModelAdmin):
	list_display = ('name', 'get_image', 'age')
	readonly_fields = ('get_image',)

	def get_image(self, obj):
		return mark_safe(f'<img src="{obj.image.url}" width="60" height="90">')

	get_image.short_description = 'Изображение'


@admin.register(Genre)
class GenreAmin(admin.ModelAdmin):
	list_display = ('name', 'url')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
	list_display = ('title', 'get_poster', 'url')

	def get_poster(self, obj):
		return mark_safe(f'<img src="{obj.poster.url}" width="60" height="90">')

	get_poster.short_description = 'Изображение'

admin.site.register(Reviewe)

# Register your models here.

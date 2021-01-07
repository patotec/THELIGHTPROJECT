from django.db import models
from django.utils.text import slugify


class PopularDestination(models.Model):
	title_place = models.CharField(max_length=200)
	discription = models.TextField()
	image = models.FileField(default='')
	slug = models.SlugField(default='' ,blank=True)
	date = models.DateTimeField(default='')


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title_place)
		super(PopularDestination, self).save(*args, **kwargs)


	def __str__ (self):
		return self.title_place




class PopularPlace(models.Model):
	title_place = models.CharField(max_length=200)
	discription = models.TextField()
	country = models.CharField(max_length=200)
	image = models.FileField(default='')
	amount = models.DecimalField(decimal_places=2, max_digits=20)
	slug = models.SlugField(default='' ,blank=True)
	date = models.DateTimeField(default='')


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title_place)
		super(PopularPlace, self).save(*args, **kwargs)


	def __str__ (self):
		return self.title_place


class RecentTrip(models.Model):
	title_place = models.CharField(max_length=200)
	image = models.FileField(default='')
	slug = models.SlugField(default='' ,blank=True)
	date = models.DateTimeField(default='')


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title_place)
		super(RecentTrip, self).save(*args, **kwargs)


	def __str__ (self):
		return self.title_place


class Question(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	phone = models.CharField(max_length=200)
	message = models.TextField()

	def __str__ (self):
		return self.name









# Create your models here.

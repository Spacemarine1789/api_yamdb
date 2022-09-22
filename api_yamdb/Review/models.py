from django.db import models

# Create your models here.

# class Review(models.Model):
#     title_id = models.ForeignKey(
#         Title, 
#         on_delete=models.CASCADE,
#         related_name='reviews',
#     )
#     text = models.TextField()
#     author = models.ForeignKey(
#         User, 
#         on_delete=models.CASCADE,
#         related_name='reviews'
#     )
#     score = models.IntegerField(
#         MaxValueValidator=10,
#         MinValueValidator=1,
#     )
#     pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

#     def __str__(self):
#         return self.text


# class Comment(models.Model):
#     review_id = models.ForeignKey(
#         Review, 
#         on_delete=models.CASCADE,
#         related_name='сomments',
#     )
#     text = models.TextField()
#     author = models.ForeignKey(
#         User, 
#         on_delete=models.CASCADE,
#         related_name='сomments'
#     )
#     pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

#     def __str__(self):
#         return self.text

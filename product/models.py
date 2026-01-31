from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='название категории:')
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    title = models.CharField(max_length=150,verbose_name='Продукт:')
    description = models.TextField(max_length=1000,verbose_name='описание товара:')
    price = models.IntegerField(verbose_name='цена:')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Категория',related_name='product_category')
    def __str__(self):
        return f'{self.title} - {self.price}'
    
    @property
    def medium_review(self):
        medium = [i.star for i in self.reviews.all()]
        return round(sum(medium) / len(medium),1)
    
class Review(models.Model):
    text = models.TextField(max_length=1000,verbose_name='отзыв')
    product = models.ForeignKey(Product,verbose_name='отзыв к продукту ',on_delete=models.CASCADE,related_name='reviews')
    STARS = (
        (i,'⭐'*i)for i in range(1,6)
    )
    star = models.IntegerField(choices=STARS,default=5)
    def __str__(self):
        return f'отзыв товара: {self.product}'
    
    
    
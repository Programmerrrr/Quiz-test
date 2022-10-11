from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default='994442465')
    email = models.EmailField(default='user@gmail.com')


    def __str__(self):
        return self.user


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    count = models.IntegerField()
    time = models.IntegerField()
    passing_score = models.IntegerField()

    def __str__(self):
        return self.category_name


class Product(models.Model):
    test = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productcategory')
    question_name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return str(self.test)


# questiontest -----------------

class Answer(models.Model):
    question = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='answerquestion')
    answer = models.CharField(max_length=200, blank=True, null=True)
    image_answer = models.ImageField(upload_to='answer_images', blank=True, null=True)
    is_correct = models.BooleanField(default=False)


    def __str__(self):
        return f'{str(self.question)} -> {self.answer} -> {self.is_correct}'


# answerquestion ----------

class Result(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='resultprofile')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='resulttest')    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='resultquestion')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='resultanswer')

# resultprofile ---------------------------
# resulttest ---------------------------
# resultquestion ---------------------------
# resultanswer ---------------------------
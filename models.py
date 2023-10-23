
from django.db import models
from django.urls import reverse

class food (models.Model):
    fname=models.CharField(max_length=400, )
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    FOOD_CHOICES = (
        ('JUICE', 'JUICE SPLASH'),
        ('LIME', 'LIME REFRESHER'),
        ('SCOOPS', 'SCOOPS'),
        ('ICE', 'ICE CREAM CHAT'),
        ('AVIL', 'AVIL MILK'),
        ('SHAKES', 'SHAKES'),
        ('BURGER', 'BURGER'),
        ('SANDWICH', 'SANDWICH'),
        ('FRENCH', 'FRENCH FRIES & NUGGETS'),
        ('HOT', 'HOT SPOT'),
        ('MANDHI', 'MANDHI'),
        ('ALFAHAM', 'AL FAHAM'),
        ('CURRYFRY', 'CURRY & FRY'),
        ('VEG', 'VEG'),
        ('CHICKENCHINESE', 'CHICKEN CHINESE & NORTH INDIAN'),
        ('BEEF', 'BEEF'),
    )
    category = models.CharField(max_length=40, choices=FOOD_CHOICES)
    recipie = models.TextField(blank=True,null=True )
    fp=models.IntegerField(blank=True,null=True)
    pic=models.ImageField( height_field=None, width_field=None, max_length=100,blank=True,null=True)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.category
    def get_absolute_url(self):
        return reverse('food_detail', args=[str(self.id)])
class hall (models.Model):
    HALL_CHOICES = (
        ('PALACE', 'PALACE AUDITORIUM MANIYAMKAVU'),
        ('M.D', 'M.D HALL KONOTHUKUNNU'),
        ('PANDARIL', 'PANDARIL HALL'),
        ('COMUNITY', 'COMUNITY HALL'),
        ('PRINCE', 'PRINCE AUDITORIUM KONOTHUKUNNU'),
    )
    hname = models.CharField(max_length=40, choices=HALL_CHOICES)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    EVENT_CHOICES = (
        ('BIRTHDAY', 'BIRTHDAY CELEBRATION'),
        ('CUSTOM', 'CUSTOM CELEBRATION'),
        ('PRIVATE', 'PRIVATE CELEBRATION'),
        ('MARRIAGE','MARRIAGE CELEBRATION'),
    )
    event = models.CharField(max_length=40, choices=EVENT_CHOICES)
    HP_CHOICES = (
        ('10000', '10,000 RS'),
        ('20000', '20,000 RS'),
        ('30000', '30,000 RS'),
        ('40000', '40,000 RS'),
        ('50000', '50,000 RS'),
        ('60000', '60,000 RS'),
        ('70000', '70,000 RS'),
        ('80000', '80,000 RS'),
        ('90000', '90,000 RS'),
        ('100000', '100,000 RS'),
    )

    fp=models.IntegerField(blank=True,null=True)
    pic=models.ImageField( height_field=None, width_field=None, max_length=100,blank=True,null=True)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.category
    def get_absolute_url(self):
        return reverse('food_detail', args=[str(self.id)])
class customer(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    cna=models.CharField(max_length=40, )
    cnumber=models.IntegerField(blank=True,null=True,)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    
class foodbill (models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    fid=models.IntegerField(blank=True,null=True)
    fname=models.CharField(max_length=40, )
    fp=models.IntegerField(blank=True,null=True)
    qty=models.IntegerField(blank=True,null=True)
    prise=models.IntegerField(blank=True,null=True)
class hallbill (models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    hid=models.IntegerField(blank=True,null=True)
    hname=models.CharField(max_length=40, )
    hp=models.IntegerField(blank=True,null=True)
    time=models.IntegerField(blank=True,null=True)
    prise=models.IntegerField(blank=True,null=True)

class storebill(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    cid=models.IntegerField(blank=True,null=True)
    cna=models.CharField(max_length=400,blank=True,null=True )
    cnumber=models.IntegerField(blank=True,null=True,)
    idbill=models.IntegerField(blank=True,null=True,)
    fid=models.IntegerField(blank=True,null=True)
    fname=models.CharField(max_length=40, )
    fp=models.IntegerField(blank=True,null=True)
    qty=models.IntegerField(blank=True,null=True)
    prise=models.IntegerField(blank=True,null=True)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    total=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.cna
    def get_absolute_url(self):
        return reverse('storebill_detail', args=[str(self.id)])

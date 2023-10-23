
from urllib import request
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import food,foodbill,hallbill,customer,storebill
from django.urls import reverse_lazy
from django.db.models import Q

def home(request):
    sipmenu = {"JUICE SPLASH" : {"WATER MELON":[30, '   ', '   '],"PINEAPPLE":[40, '   ', '   '],"BANANA":[30, '   ', '   '],"MOSAMBI":[40, '   ', '   '],"ORANGE":[40, '   ', '   '],"GRAPE":[40, '   ', '   '],"MANGO":[50, '   ', '   '],"GUAVA":[50, '   ', '   '],"MIX FRUIT":[50, '   ', '   '],"ORANGE PINAPPLE":[50, '   ', '   '],"HONEY GRAPE":[50, '   ', '   '],"PAPAYA":[60, '   ', '   '],"POMEGRANATE":[60, '   ', '   '],"APPLE":[60, '   ', '   '],"CARROT":[60, '   ', '   '],"RUSSIAN COCKTAIL":[80, '   ', '   '],},"LIME REFRESHER" : {"FRESH LIME" : [20, '   ', '   '],"GINGER LIME" :[25, '   ', '   '],"WATER MELON":[25, '   ', '   '],"MINT LIME":[25, '   ', '   '],"MINT COOLER":[40, '   ', '   '],"CUKUMBER MINT":[30, '   ', '   '],"MOROCCAN LIME":[40, '   ', '   '],"MOJITO":[60, '   ', '   '],"SPECIAL MOJITO":[80, '   ', '   '],"LEMONADE":[60, '   ', '   '],"KULK-E SARBATH(FRESH)":[30, '   ', '   '],"KULK-E SARBATH(CRUSH)":[20, '   ', '   '],"KULK-E BOOST":[30, '   ', '   ']},"SCOOPS" : {"VANILA" : ['   ','   ', '   '],"STRAWBERRY PISTA" : [60, '   ', '   '],"MANGO":['   ','   ', '   '],"PINEAPPLE CHOCOLATE":[60, '   ', '   '],"VANILLA MANGO":[60, '   ', '   '],"BUTTER SCOTCH":[70, '   ', '   '],"SPANISH DELIGHT":[100, '   ', '   '],"SIP SPECIAL":[120, '   ', '   '],},"ICE CREAM CHAT":{"Mango Delight":[70, '   ', '   '],"Cookies n Cream":[60, '   ', '   '],"ice cream with fruit salad":[70, '   ', '   '],"Brownie with ice cream ":[60, '   ', '   '],"Chocolate fudge":[60, '   ', '   '],"Butter scotch fudge":[70, '   ', '   '],"Arabian cocktail":[100, '   ', '   '],"Dates with ice cream":[70, '   ', '   '],"Death by chocolate":[100, '   ', '   '],"Dry fruit sandae":[120, '   ', '   '],"Spanish delight":[90, '   ', '   '],"Black current sundae":[70, '   ', '   ']},"AVIL MILK":{"Avil Milk":[50, '   ', '   '],"Mango":[50, '   ', '   '],"Papaya":[60, '   ', '   '],"Grape":[50, '   ', '   '],"Student Avil Milk":[60, '   ', '   '],"Couple Avil Milk":[70, '   ', '   ']},"SHAKES":{"Sharjah Very Berry":[70,50, '   '],"Kashmeeri":[70,50, '   '],"Belgian Chocolate":[70,50, '   '],"Mango Alphonso Saudi Punch":[70,50, '   '],"Lots of Oats":[70,50, '   '],"Ferrero Roucher":[70,50, '   '],"Banana bonkers":[70,50, '   '],"Mango Strawberry":[70,50, '   '],"Avocado":[80,60, '   '],"Tender Coconut":[80,60, '   '],"Tropical Mix fruit":[80,60, '   '],"Walk like-an Egyptian":[70,50, '   '],"Vanilla":[70,50, '   '],"Pista":[70,50, '   '],"Black Pearl":[70,50, '   '],"Kiw":[70,50, '   '],"Orea":[70,50, '   '],"Kit kat":[70,50, '   '],"Chocolate":[70,50, '   '],"Strawberry":[70,50, '   '],"Gems":[70,50, '   '],"Mango":[70,50, '   '],"Dark fantasy":[70,50, '   '],"Butter Scotch":[70,50, '   '],"Guava":[70,50, '   '],"Bdam":[80,60, '   '],"Dates":[80,60, '   '],},"BURGER":{"Veg Burger":[50,'   ','   '],"Egg Burger":[60,'   ','   '],"Cheese Burger":[60,'   ','   '],"Nuggets Burger":[70,'   ','   '],"Chicken Burger":[70,'   ','   '],"Chicken w. Chese":[90,'   ','   '],"Chicken w Fries":[90,'   ','   '],"Chicken Double":[100,'   ','   '],"Jumbo Burger":[100,'   ','   '],"Sip Special":[150,'   ','   '],"Chicken w. Egg in Cheese":[100,'   ','   '],},"SANDWICH":{"Bread Butter":[20,'   ','   '],"Veg. Sandwich":[30,'   ','   '],"Veg. Club":[60,'   ','   '],"Egg Sandwich":[50,'   ','   '],"Hot Dog":[50,'   ','   '],"Egg N Cheese":[60,'   ','   '],"Parotta Sandwich":[60,'   ','   '],"Sip Special Club":[150,'   ','   '],},"FRENCH FRIES & NUGGETS":{"MEDIUM":[60,'   ','   '],"LARGE":[120,'   ','   '],"NUGGETS":[100,50]},"HOT SPOT":{"TEA":[10,'   ','   '],"COFFEE":[20,'   ','   '],"LIME TEA":[10,'   ','   '],"MINT TEA":[10,'   ','   '],"SPECIAL TEA":[15],"BOOST":[20,'   ','   '],"HORLICS":[20,'   ','   ']},"MANDHI":{"Kuzhi Mandhi Chicken":[550,280,150],"Kuzhi Mandhi Beef":[800,420,220],"Al Faham Mandhi":[650,330,180],"Peri Peri Mandhi":[700,360,200],"Afghani Mandhi":[680,340,190],"Kanthari Mandhi":[680,340,190],"Chilly Honey Mandhi":[700,360,200],},"AL FAHAM":{"Red Chilly":[380,200,110],"Peri Peri":[450,240,130],"Chilly Honey":[450,240,130], "Green Chilly":[420,220,120],"Afghani":[430,230,120], "Al Faham Dragon":[500,260,140],"Sip Special":[500,260,140]},"CURRY & FRY":{"Beef Roast":[100,'   ','   '],"Beef Curry":[90,'   ','   '],"Beef Fry":[120,'   ','   '],"Chicken Curry":[90,'   ','   '],"Chicken Roast":[100,'   ','   '],"Chicken 65":[120,'   ','   ']},"VEG":{"Chena Masala":[40,'   ','   '],"Peas Masala":[40,'   ','   '],"Veg. Kuruma":[30,'   ','   '],"Veg. Masala":[40,'   ','   '],"Paneer Butter Massala":[130,'   ','   '],"Mashrrom Masala":[120,'   ','   '],"Chilly Gobi":[90,'   ','   '],"Gobi Manchurian":[100,'   ','   '],"Chilly Mashroom":[120,'   ','   ']},"CHICKEN CHINESE & NORTH INDIAN":{"Chilly Chicken":[130,'   ','   '],"Chilly Chicken Dry":[140,'   ','   '],"Pepper Chicken":[130,'   ','   '],"Garlic Chicken":[130,'   ','   '],"Ginger Chicken":[130,'   ','   '],"Butter Chicken":[100,'   ','   '],"Schezwan Chicken":[160,'   ','   '],"Dragon Chicken":[150,'   ','   '],"Chicken Kondattam":[150,'   ','   '],"Chicken Manchurian":[140,'   ','   ']},"BEEF":{"CHILLY BEEF":['   ','   ','   '],"DRAGON BEEF":['   ','   ', '   '],"B.D.F":['   ','   ', '   '],"Beef Condattam":['   ','   ', '   '],},}
    return render(request,'home.html',{'sipmenu':sipmenu})
class foodCreateView(ListView):
    model= food
    context_object_name = 'food_menu'
    template_name ='food_new.html'
def Create_food_success(request):
    
    fname=request.POST['fn']
    category=request.POST['category']
    fp=int(request.POST['fp'])
    append=food(fname=fname, category=category, fp=fp,author_id=request.user.id)
    append.save()
    food_menu=food.objects.all()
    return render(request,'food_new.html',{'food_menu':food_menu})
 
class Searchfoodmenu(ListView):
    model = food
    context_object_name = 'food_menu'
    template_name = 'food_new.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return food.objects.filter(Q(category__icontains=query) | Q(fname__icontains=query)| Q(fp__icontains=query) | Q(id__icontains=query))
   
class foodDetailView(DetailView):
    model = food
    template_name = 'food_detail.html'

class foodDeleteView(DeleteView): 
    model = food
    template_name = 'food_delete.html'
    success_url = reverse_lazy('home')
'''
def Update_food_success(request):
    model=food
    id=request.POST['id']
    m=food.objects.get(id)
    m.fname=request.POST['fname']
    m.category=request.POST['category']
    m.fp=int(request.POST['fp'])
    m.save()
    return render(request,'food_new.html',{'object_list':model})
'''
class orderFoodView(ListView):
    model=food
    template_name = 'orderfood.html'
    
class history(ListView):
    model= storebill
    template_name='storebill.html'
    

class storebillDetailView(DetailView):
    model = storebill
    template_name = 'storebill_detail.html'

'''
def food_edit(request):
    id=int(request.POST[id])
    fname=request.POST['fname']
    fp=int(request.POST['fp'])
    return render(request,'food_edit.html',{'id':id,'fp':fp,'fname':fname})
'''


class orderHallView(ListView):
    model=food
    template_name = 'orderhall.html'

def getcustomer(request):
    total=0
    custate=customer.objects.all()
    billstate=foodbill.objects.all()
    model=food.objects.all()
    cna=request.POST['cna']
    cnumber=int(request.POST['cnumber'])
    append=customer(cna=cna,cnumber=cnumber,author_id=request.user.id)
    append.save()
    for i in billstate:
        total=total+i.prise
    for j in custate:
        customername=j.cna
        phonenumber=j.cnumber
    return render(request,'bill.html',{'object_list':model,'billstate':billstate,'total':total,'customername':customername,'phonenumber':phonenumber})
def getcustomerhall(request):
    total=0
    custate=customer.objects.all()
    billstate=foodbill.objects.all()
    model=food.objects.all()
    cna=request.POST['cna']
    cnumber=int(request.POST['cnumber'])
    append=customer(cna=cna,cnumber=cnumber,author_id=request.user.id)
    append.save()
    for i in billstate:
        total=total+i.prise
    for j in custate:
        customername=j.cna
        phonenumber=j.cnumber
    return render(request,'bill.html',{'object_list':model,'billstate':billstate,'total':total,'customername':customername,'phonenumber':phonenumber})


def makebill(request):
    billstate=foodbill.objects.all()
    custate=customer.objects.all()
    model=food.objects.all()
    for cust in custate:
        cid=cust.id
        cna=cust.cna
        cnumber=cust.cnumber
    for i in billstate:
        idb=i.id
        fid=i.fid
        fname=i.fname
        fp=i.fp
        qty=i.qty
        prise=i.prise
        total=request.POST['total']
        append=storebill(cid=cid,cna=cna,cnumber=cnumber,idbill=idb,fid=fid,fname=fname,fp=fp,qty=qty,prise=prise,total=total,author_id=request.user.id)
        append.save()
    customer.objects.all().delete()
    foodbill.objects.all().delete()
    model=storebill.objects.all()
    return render(request,'storebill.html',{'object_list':model})
class SearchResultsListView(ListView):
    model = food
    template_name = 'search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return food.objects.filter(Q(category__icontains=query) | Q(fname__icontains=query)| Q(fp__icontains=query)| Q(id__icontains=query))


def billing(request):
    total=0
    custate=customer.objects.all()
    billstate=foodbill.objects.all()
    model=food.objects.all()
    for i in billstate:
        total=total+i.prise
    for j in custate:
        customername=j.cna
        phonenumber=j.cnumber
    return render(request,'bill.html',{'object_list':model,'billstate':billstate,'total':total,'customername':customername,'phonenumber':phonenumber})

def getdetails(request):
    total=0
    custate=customer.objects.all()
    billstate=foodbill.objects.all()
    model=food.objects.all()
    id=request.POST['id']
    name = request.POST['fname']
    full=int(request.POST['fp'])
    quantity=int(request.POST['q'])
    prise=quantity*full
    append=foodbill(fid=id,fname=name,fp=full,qty=quantity,prise=prise,author_id=request.user.id)
    append.save()
    for i in billstate:
        total=total+i.prise
    for j in custate:
        customername=j.cna
        phonenumber=j.cnumber
    return render(request,'bill.html',{'object_list':model,'billstate':billstate,'total':total,'customername':customername,'phonenumber':phonenumber})

class RecordDeleteView(DeleteView):
    model = foodbill
    template_name = 'bill_delete.html'
    success_url = reverse_lazy('billing')
from django.urls import path
from .views import Searchfoodmenu,foodCreateView,foodDetailView,storebillDetailView,foodDeleteView,orderFoodView,history,SearchResultsListView,RecordDeleteView,orderHallView
from .import views
urlpatterns = [
path('', views.home, name='home'),

# path('bookhall', orderHallView.as_view(), name='book_hall'),
# path('bookhall/history',history.as_view(), name='history'),
# path('getcustomerhall',views.getcustomerhall), 
path('food/new/', foodCreateView.as_view(), name='edit_food_menu'),
path('food/new/Create_food_success', views.Create_food_success),
path('search/', Searchfoodmenu.as_view(),name='search_menu'),
path('search/Create_food_success', views.Create_food_success),
path('food/<int:pk>/', foodDetailView.as_view(), name='food_detail'),
path('food/<int:pk>/delete/',foodDeleteView.as_view(), name='food_delete'),

path('order', orderFoodView.as_view(), name='order_food'),
path('order/history',history.as_view(), name='history'),
path('getcustomer',views.getcustomer, name='getcustomer'),
path('getdetails',views.getdetails),
path('makebill',views.makebill, name='makebill'),
path('search_rec/', SearchResultsListView.as_view(),name='search_results'), 


path('storebill/<int:pk>/', storebillDetailView.as_view(), name='storebill_detail'),
path('bill/<int:pk>/delete/',RecordDeleteView.as_view(), name='record_delete'),
path('bill',views.billing,name='bill'),
path('search_rec/getdetails',views.getdetails),
path('search_rec/getcustomer',views.getcustomer),
path('search_rec/bill',views.billing, name='bill'),
path('getcustomer',views.getcustomer),
path('search_rec/makebill',views.makebill, name='makebill'),


]
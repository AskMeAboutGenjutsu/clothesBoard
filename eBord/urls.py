from django.urls import path
from .views import EBordAddView, \
    EBordView, CategoryView, ByCategoryView, ByUserView, \
    EBordDetailView, EBordUpdateView, EBordDeleteView, CategoryAddView, category_change

urlpatterns = [
    path('', CategoryView.as_view(), name='home'),
    path('all_ads', EBordView.as_view(), name='all_ads'),
    path('add/', EBordAddView.as_view(), name='add'),
    path('ads/<str:pk>', ByCategoryView.as_view(), name='by_category'),
    path('user_ads/<int:pk>', ByUserView.as_view(), name='by_user'),
    path('detail/<int:pk>', EBordDetailView.as_view(), name='detail'),
    path('change/<int:pk>', EBordUpdateView.as_view(), name='change'),
    path('delete/<int:pk>', EBordDeleteView.as_view(), name='delete'),
    path('add-cat/', CategoryAddView.as_view(), name='add-cat'),
    path('change-cat/', category_change, name='change-cat')
]

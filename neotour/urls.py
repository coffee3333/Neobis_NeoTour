from django.urls import path
from neotour.views import CategoryList, TourListView, ReviewList, TourBookView

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('tours/', TourListView.as_view(), name='tour-list'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('tour-book/', TourBookView.as_view(), name='review-list'),
]

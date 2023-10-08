from myapp.api import views
from django.urls import path


urlpatterns = [
    path('list/',views.WatchListAV.as_view(),name='watchlist'),
    path('<int:pk>/',views.WatchDetailAV.as_view(),name='watchdetail'),
    
    path('<int:pk>/review/',views.ReviewListVW.as_view(),name='reviews'),
    path('<int:pk>/create/',views.ReviewCreateVW.as_view(),name='create'),
    path('review/<int:pk>/',views.ReviewDetailVW.as_view(),name='reviewdetail'),
]

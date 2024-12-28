from django.urls import path
from .views import SignupView, SigninView
from .views import AddToWatchlistView, UserWatchlistView
from .views import DeleteFromWatchlistView

from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('watchlist/add/', AddToWatchlistView.as_view(), name='add-to-watchlist'),
    path('watchlist/', UserWatchlistView.as_view(), name='user-watchlist'),
    path('watchlist/delete/<int:movie_id>/', DeleteFromWatchlistView.as_view(), name='delete-from-watchlist'),
]







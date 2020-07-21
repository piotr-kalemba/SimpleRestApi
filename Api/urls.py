from django.urls import path
from .views import HomeView, BookView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/<int:id>', BookView.as_view(), name='book')

]
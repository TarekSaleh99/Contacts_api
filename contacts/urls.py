from django.urls import path
from .views import ContactsList, ContactsDitailView

urlpatterns = [
    path('', ContactsList.as_view()),
    path('<int:pk>', ContactsDitailView.as_view()),
]

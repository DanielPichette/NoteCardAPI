from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.Collections.as_view()),
    path('notecards/', views.Notecards.as_view()),
    path('collections/<int:pk>/', views.CollectionById.as_view()),  # 'as.view()' b/c we are using class views.
    path('notecards/<int:pk>/', views.NotecardById.as_view()),


]

from django.urls import path
from . import views

urlpatterns=[
    path('notes/',views.NotesListView.as_view(),name="Notes_model.list"),
    path('notes/<int:pk>/',views.NotesDetailView.as_view(),name="Notes_model.detail"),
    path('notes/<int:pk>/edit',views.NotesUpdateView.as_view(),name="Notes_model.update"),
    path('notes/<int:pk>/delete',views.NotesDeleteView.as_view(),name="Notes_model.delete"),
    path('notes/new',views.NotesCreateView.as_view(),name="Notes_model.new")

]

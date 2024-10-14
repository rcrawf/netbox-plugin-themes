from django.urls import path
from . import models, views

from netbox.views.generic import ObjectChangeLogView

app_name = "theme"

urlpatterns = (
    path('theme/', views.ThemeListView.as_view(), name='theme_list'),
    path('theme/add/', views.ThemeEditView.as_view(), name='theme_add'),
    path('theme/<int:pk>/', views.ThemeView.as_view(), name='theme'),
    path('theme/<int:pk>/edit/', views.ThemeEditView.as_view(), name='theme_edit'),
    path('theme/<int:pk>/delete/', views.ThemeDeleteView.as_view(), name='theme_delete'),

    path('theme/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='theme_changelog', kwargs={
        'model': models.Theme
    }),
)

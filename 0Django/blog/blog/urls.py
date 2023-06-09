from django.urls import path, re_path
from blog import views

app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', views.PostLV.as_view(), name='index'),
    
    # /blog/post/ (same as /blog/)
    path('post/', views.PostLV.as_view(), name='post_list'),

    # /blog/post/django-example/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    # /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # /blog/archive/2019/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # /blog/archive/2019/nov/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    # /blog/archive/2019/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    # /blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

    # /blog/tag/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),

    # /blog/tag/tagname/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),

    # /blog/search/
    path('search/', views.SearchFormView.as_view(), name='search'),

    # /blog/create/
    path('create/', views.PostCreateView.as_view(), name='create'),
    
    # /blog/99/update
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name="update"),

    # /blog/99/delete/
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name="delete"),

    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]

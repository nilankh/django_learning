# from django.urls import path
# from snippets import views

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]


# use in fucntion based
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

# urlpatterns = [
#     path("snippets/", views.snippet_list),
#     path("snippets/<int:pk>/", views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# use in class based
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

# from snippets import views

# urlpatterns = [
#     path("snippets/", views.SnippetList.as_view()),
#     path("snippets/<int:pk>/", views.SnippetDetail.as_view()),
#     path("users/", views.UserList.as_view()),
#     path("users/<int:pk>/", views.UserDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


from rest_framework import renderers

from snippets.views import SnippetViewSet, UserViewSet

snippet_list = SnippetViewSet.as_view({"get": "list", "post": "create"})
snippet_detail = SnippetViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)
snippet_highlight = SnippetViewSet.as_view(
    {"get": "highlight"}, renderer_classes=[renderers.StaticHTMLRenderer]
)
user_list = UserViewSet.as_view({"get": "list"})
user_detail = UserViewSet.as_view({"get": "retrieve"})


urlpatterns = format_suffix_patterns(
    [
        path("snippets/", snippet_list, name="snippet-list"),
        path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
        path(
            "snippets/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"
        ),
        path("users/", user_list, name="user-list"),
        path("users/<int:pk>/", user_detail, name="user-detail"),
    ]
)

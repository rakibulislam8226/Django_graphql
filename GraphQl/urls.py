from django.contrib import admin
from django.urls import re_path as url
from django.urls import path, include
from graphene_django.views import GraphQLView
from postCreate.schema import schema
from django.views.decorators.csrf import csrf_exempt

GraphQLView.graphiql_template = "graphene_graphiql_explorer/graphiql.html"


urlpatterns = [
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('admin/', admin.site.urls),
    path('', include('postCreate.urls')),
    path('', include('auth_permission.urls')),

]

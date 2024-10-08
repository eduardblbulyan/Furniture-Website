from django.urls import path
from . import views

app_name = "goods"

urlpatterns = [
    path("search/", views.catalog, name="search"), # should be on top to not conflict with below url
    path("<slug:category_slug>/", views.catalog, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),

]

# slug can convert number to its format so we need to put int before slug for working
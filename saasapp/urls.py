from django.urls import path
from .views import register, login, home, logout_view, add_to_cart, view_cart, remove_from_cart, place_order
from django.contrib import admin
from saasapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', register, name='register'),
    path('', login, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout_view'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('place_orders/', place_order, name='place_orders'),

    # path('logout_view',logout_view, name="logout_view"),

    #  path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
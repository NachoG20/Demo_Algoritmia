from django.urls import path

#from rest_framework import routers

from .views import quicksort
from .views import burbuja
from .views import all_methods

#router = routers.DefaultRouter()
#router.register('students', StudentsViewSet)

#urlpatterns = router.urls

urlpatterns = [
    path('algoritmos/quicksort/', quicksort),
    path('algoritmos/burbuja/', burbuja),
    path('algoritmos/all_methods/', all_methods)
]
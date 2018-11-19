from django.urls import path
from .views import div_list,distric_population_wise,all_dis,population_order

urlpatterns=[
    path('division/list/',div_list,name='division-url'),
    path('dis/list/<name>/',distric_population_wise,name='distric-population'),
    path('all/district/',all_dis,name='all-dis'),
    path('order/by/population',population_order)

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio,name='index'),
    path('CompraPag/',views.Compra, name='compra'),
    path('CompraPag/<str:TA>/<str:TP>',views.CompraT, name='compraT'),
    path('agregar_carrito/<str:TA>/<str:TP>',views.agregar_carrito, name='addCarrito'),

    path('eliminar_carrito_compra/<str:TA>/<str:TP>/<str:pk>',views.Del_Compra_Producto, name='del_Compra_Producto'),
    path('eliminar_carrito_index/<str:pk>',views.Del_Index_Producto, name='del_Index_Producto'),
    
    path('Admin_Producto', views.adminProduct,name='product_admin'),

    path('agregar_producto',views.agregar_producto, name='producto_add'),
    path('eliminar_producto/<str:pk>',views.eliminar_producto, name='producto_del'),
    path('buscar_producto/<str:pk>',views.buscar_producto, name='producto_find'),
    path('actualizar_producto',views.modificar_producto, name='productoUpdate'),

    path('log', views.Login2,name='Login2'),
    path('log/<str:TA>/<str:TP>', views.Login3,name='Login3'),
    path('logout', views.Logout2,name='logout2'),
    path('logout/<str:TA>/<str:TP>', views.Logout3,name='logout3'),
    path('Reg', views.Register,name='Register'),
]
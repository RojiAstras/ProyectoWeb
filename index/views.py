from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Carusel1, Carusel2, Banner, Producto, Carrito, TipoArticulo, TipoMascota

# Create your views here.
def inicio(request):
    uname= request.user.username
    Car1 = Carusel1.objects.raw('SELECT * FROM index_Carusel1')
    Car2 = Carusel2.objects.raw('SELECT * FROM index_Carusel2')
    Banners = Banner.objects.raw('SELECT * FROM index_Banner')
    Carro = Carrito.objects.filter(usuario_var = uname)
    CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
    context = {"Car1": Car1, "Car2": Car2, "Banners": Banners, "CarritoProductos": Carro, "CTotal": CarroTotal}
    return render(request, 'index/index.html', context)

def Compra(request):
    uname= request.user.username
    TA=" "
    TP=" "
    Productos = Producto.objects.all()
    Carro = Carrito.objects.filter(usuario_var = uname)
    CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
    context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
    return render(request, 'index/compra.html', context)

def CompraT(request,TA,TP):
    uname= request.user.username
    Tart =TipoArticulo.objects.get(tipoArticulo = TA)
    Tpet =TipoMascota.objects.get(tipoMascota = TP)
    Productos = Producto.objects.filter(id_tipoArticulo= Tart.id_tipoArticulo, id_tipoMascota=Tpet.id_tipoMascota)
    Carro = Carrito.objects.filter(usuario_var = uname)
    CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
    context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
    return render(request, 'index/compra.html', context)

def Del_Compra_Producto(request,TA,TP, pk):
    try:
        if TA !='' and TP !='':
            uname= request.user.username
            product = Carrito.objects.get(id_producto=pk)
            product.delete()

            Tart =TipoArticulo.objects.get(tipoArticulo = TA)
            Tpet =TipoMascota.objects.get(tipoMascota = TP)
            Productos = Producto.objects.filter(id_tipoArticulo= Tart.id_tipoArticulo, id_tipoMascota=Tpet.id_tipoMascota)
    
            Carro = Carrito.objects.filter(usuario_var = uname)
            CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
            context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
            return render(request, 'index/compra.html', context)
        else:
            uname= request.user.username
            product = Carrito.objects.get(id_producto=pk)
            product.delete()

            Productos = Producto.objects.all()
            Carro = Carrito.objects.filter(usuario_var = uname)
            CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
            context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
            return render(request, 'index/compra.html', context)
    except:
        uname= request.user.username
        TP=' '
        TA=' '
        Productos = Producto.objects.all()
        Carro = Carrito.objects.filter(usuario_var = uname)
        CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
        context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
        return render(request, 'index/compra.html', context)

def Del_Index_Producto(request, pk):
    try:
        uname= request.user.username
        product = Carrito.objects.get(id_producto=pk)
        product.delete()

        Car1 = Carusel1.objects.raw('SELECT * FROM index_Carusel1')
        Car2 = Carusel2.objects.raw('SELECT * FROM index_Carusel2')
        Banners = Banner.objects.raw('SELECT * FROM index_Banner')
        Carro = Carrito.objects.filter(usuario_var = uname)
        CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
        context = {"Car1": Car1, "Car2": Car2, "Banners": Banners, "CarritoProductos": Carro, "CTotal": CarroTotal}
        return render(request, 'index/index.html', context)
    except:
        uname= request.user.username
        Car1 = Carusel1.objects.raw('SELECT * FROM index_Carusel1')
        Car2 = Carusel2.objects.raw('SELECT * FROM index_Carusel2')
        Banners = Banner.objects.raw('SELECT * FROM index_Banner')
        Carro = Carrito.objects.filter(usuario_var = uname)
        CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
        context = {"Car1": Car1, "Car2": Car2, "Banners": Banners, "CarritoProductos": Carro, "CTotal": CarroTotal}
        return render(request, 'index/index.html', context)


def agregar_carrito(request, TA, TP):
    if request.method != "POST":
        if TA !='' and TP !='':
            uname= request.user.username
            Tart =TipoArticulo.objects.get(tipoArticulo = TA)
            Tpet =TipoMascota.objects.get(tipoMascota = TP)
            Productos = Producto.objects.filter(id_tipoArticulo= Tart.id_tipoArticulo, id_tipoMascota=Tpet.id_tipoMascota)
    
            Carro = Carrito.objects.filter(usuario_var = uname)
            CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
            context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
            return render(request, 'index/compra.html', context)
        else:
            uname= request.user.username
            Productos = Producto.objects.all()
            Carro = Carrito.objects.filter(usuario_var = uname)
            CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
            context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
            return render(request, 'index/compra.html', context)
    else:
        if TA !=' ' and TP !=' ':
            idp=request.POST["idpro"]
            uname= request.user.username
            objPro=Producto.objects.get(id_producto = idp)
            obj=Carrito.objects.create(nom_producto = objPro.nom_producto,
                                    usuario_var = uname,
                                    img_producto = objPro.img_producto,
                                    precio_producto = objPro.precio_producto)
            obj.save()
            Tart =TipoArticulo.objects.get(tipoArticulo = TA)
            Tpet =TipoMascota.objects.get(tipoMascota = TP)
            Productos = Producto.objects.filter(id_tipoArticulo= Tart.id_tipoArticulo, id_tipoMascota=Tpet.id_tipoMascota)
    
            Carro = Carrito.objects.filter(usuario_var = uname)
            CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
            context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
            return render(request, 'index/compra.html', context)
        else:
            idp=request.POST["idpro"]
            uname= request.user.username
            objPro=Producto.objects.get(id_producto = idp)
            obj=Carrito.objects.create(nom_producto = objPro.nom_producto,
                                    usuario_var = uname,
                                    img_producto = objPro.img_producto,
                                    precio_producto = objPro.precio_producto)
            obj.save()
            TP=' '
            TA=' '
            Productos = Producto.objects.all()
            Carro = Carrito.objects.filter(usuario_var = uname)
            CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
            context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
            return render(request, 'index/compra.html', context)

def adminProduct(request):
    lista_productos = Producto.objects.all()
    context = {"Productos":lista_productos}
    return render(request,'index/Product_admin.html', context)

def agregar_producto(request):
    if request.method != "POST":
        lista_articulos = TipoArticulo.objects.all()
        lista_mascotas = TipoMascota.objects.all()
        context = {"mascotas": lista_mascotas, "articulos":lista_articulos}
        return render(request,'index/producto_add.html', context)
    else:
        nomPro=request.POST["nombre"]
        rutaImg=request.POST["rutaImagen"]
        Tarticulo=request.POST["tipoArt"]
        Tmascota=request.POST["tipoPet"]
        detalle=request.POST["detalle"]
        precio=request.POST["precio"]

        objArticulo=TipoArticulo.objects.get(id_tipoArticulo = Tarticulo)
        objMascota =TipoMascota.objects.get(id_tipoMascota = Tmascota)
        obj=Producto.objects.create(
                                    nom_producto = nomPro,
                                    img_producto = rutaImg,
                                    id_tipoArticulo = objArticulo,
                                    id_tipoMascota = objMascota,
                                    detalle_producto = detalle,
                                    precio_producto = precio)
        obj.save()
        lista_articulos = TipoArticulo.objects.all()
        lista_mascotas = TipoMascota.objects.all()
        context = {"mascotas": lista_mascotas, "articulos":lista_articulos,'mensaje': "OK, datos grabados..."}
        return render(request, 'index/producto_add.html', context)

def buscar_producto(request,pk):
    if pk != "":
        lista_articulos = TipoArticulo.objects.all()
        lista_mascotas = TipoMascota.objects.all()
        producto = Producto.objects.get(id_producto=pk)
        context = {"mascotas": lista_mascotas, "articulos":lista_articulos,"Producto": producto}
        return render(request,'index/producto_mod.html', context)
    else:
        mensaje= "producto NO existe"
        context={"mensaje":mensaje}
        return render(request,'index/Product_admin.html', context)

def modificar_producto(request):
    if request.method == "POST":
        
        idpro = request.POST["id"]
        nombre=request.POST["nombre"]
        rutaImagen=request.POST["rutaImagen"]
        Tarticulo=request.POST["tipoArticulo"]
        Tmascota=request.POST["tipoMascota"]
        detalle=request.POST["detalle"]
        precio=request.POST["precio"]


        objArticulo=TipoArticulo.objects.get(id_tipoArticulo = Tarticulo)
        objMascota =TipoMascota.objects.get(id_tipoMascota = TMascota)
        objPro=Producto()
        objPro.id_producto=idpro
        objPro.nom_producto=nombre
        objPro.img_producto=rutaImagen
        objPro.id_tipoArticulo=objArticulo
        objPro.id_tipoMascota= objMascota
        objPro.detalle_producto=detalle
        objPro.precio_producto= precio

        objPro.save()
        lista_articulos = TipoArticulo.objects.all()
        lista_mascotas = TipoMascota.objects.all()
        context = {"mascotas": lista_mascotas, "articulos":lista_articulos,'mensaje': "Se Actualizo Producto", "producto": objPro}
        return render(request, 'index/producto_mod.html', context)
    else:
        lista_productos = Producto.objects.all()
        context = {"Productos":lista_productos}
        return render(request,'index/Product_admin.html', context)

def eliminar_producto(request, pk):
    try:
        producto = Producto.objects.get(id_producto=pk)
        producto.delete()
        mensaje = "El Producto se elimino"
        lista_productos = Producto.objects.all()
        context = {"Productos":lista_productos, "mensaje":mensaje}
        return render(request,'index/Product_admin.html', context)
    except:
        mensaje = "El Producto NO se elimino"
        lista_productos = Producto.objects.all()
        context = {"Productos":lista_productos, "mensaje":mensaje}
        return render(request,'index/Product_admin.html', context)

def Logout2(request):
    logout(request)
    uname= request.user.username
    Car1 = Carusel1.objects.raw('SELECT * FROM index_Carusel1')
    Car2 = Carusel2.objects.raw('SELECT * FROM index_Carusel2')
    Banners = Banner.objects.raw('SELECT * FROM index_Banner')
    Carro = Carrito.objects.filter(usuario_var = uname)
    CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
    context = {"Car1": Car1, "Car2": Car2, "Banners": Banners, "CarritoProductos": Carro, "CTotal": CarroTotal}
    return render(request, 'index/index.html', context)

def Logout3(request, TA, TP):
    logout(request)
    if TP != '' and TA != '':
        uname= request.user.username
        Tart =TipoArticulo.objects.get(tipoArticulo = TA)
        Tpet =TipoMascota.objects.get(tipoMascota = TP)
        Productos = Producto.objects.filter(id_tipoArticulo= Tart.id_tipoArticulo, id_tipoMascota=Tpet.id_tipoMascota)
        Carro = Carrito.objects.filter(usuario_var = uname)
        CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
        context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
        return render(request, 'index/compra.html', context)
    else:
        uname= request.user.username
        Productos = Producto.objects.all()
        Carro = Carrito.objects.filter(usuario_var = uname)
        CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
        context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal}
        return render(request, 'index/compra.html', context)       

    
def Login2(request):
    if request.method == "POST":
        name = request.POST["nombre"]
        contra = request.POST["contraseña"]

        user = authenticate(username = name, password=contra)
        if user is not None:
            login(request, user)
            uname= request.user.username
            Car1 = Carusel1.objects.raw('SELECT * FROM index_Carusel1')
            Car2 = Carusel2.objects.raw('SELECT * FROM index_Carusel2')
            Banners = Banner.objects.raw('SELECT * FROM index_Banner')
            Carro = Carrito.objects.filter(usuario_var = uname)
            CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
            context = {"Car1": Car1, "Car2": Car2, "Banners": Banners, "CarritoProductos": Carro, "CTotal": CarroTotal}
            return render(request, 'index/index.html', context)
        else:
            uname= request.user.username
            Car1 = Carusel1.objects.raw('SELECT * FROM index_Carusel1')
            Car2 = Carusel2.objects.raw('SELECT * FROM index_Carusel2')
            Banners = Banner.objects.raw('SELECT * FROM index_Banner')
            Carro = Carrito.objects.filter(usuario_var = uname)
            CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
            context = {"Car1": Car1, "Car2": Car2, "Banners": Banners, "CarritoProductos": Carro, "CTotal": CarroTotal}
            return render(request, 'index/index.html', context)
    else:
        uname= request.user.username
        Car1 = Carusel1.objects.raw('SELECT * FROM index_Carusel1')
        Car2 = Carusel2.objects.raw('SELECT * FROM index_Carusel2')
        Banners = Banner.objects.raw('SELECT * FROM index_Banner')
        Carro = Carrito.objects.filter(usuario_var = uname)
        CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
        context = {"Car1": Car1, "Car2": Car2, "Banners": Banners, "CarritoProductos": Carro, "CTotal": CarroTotal}
        return render(request, 'index/index.html', context)

def Login3(request,TA, TP):
    if request.method == "POST":
        name = request.POST["nombre"]
        contra = request.POST["contraseña"]

        user = authenticate(username = name, password=contra)
        if user is not None:
            login(request, user)
            if TP != '' and TA != '':
                uname= request.user.username
                Tart =TipoArticulo.objects.get(tipoArticulo = TA)
                Tpet =TipoMascota.objects.get(tipoMascota = TP)
                Productos = Producto.objects.filter(id_tipoArticulo= Tart.id_tipoArticulo, id_tipoMascota=Tpet.id_tipoMascota)
                Carro = Carrito.objects.filter(usuario_var = uname)
                CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
                context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
                return render(request, 'index/compra.html', context)
            else:
                uname= request.user.username
                Productos = Producto.objects.all()
                Carro = Carrito.objects.filter(usuario_var = uname)
                CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
                context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal}
                return render(request, 'index/compra.html', context)
        else:
            if TP != '' and TA != '':
                uname= request.user.username
                Tart =TipoArticulo.objects.get(tipoArticulo = TA)
                Tpet =TipoMascota.objects.get(tipoMascota = TP)
                Productos = Producto.objects.filter(id_tipoArticulo= Tart.id_tipoArticulo, id_tipoMascota=Tpet.id_tipoMascota)
                Carro = Carrito.objects.filter(usuario_var = uname)
                CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
                context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal, "Tpet":TP, "Tart":TA}
                return render(request, 'index/compra.html', context)
            else:
                uname= request.user.username
                Productos = Producto.objects.all()
                Carro = Carrito.objects.filter(usuario_var = uname)
                CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
                context = {"Productos": Productos, "CarritoProductos": Carro, "CTotal": CarroTotal}
                return render(request, 'index/compra.html', context)
    
def Register(request):
     if request.method == "POST":
        name = request.POST["nombre"]
        mail = request.POST["mail"]
        contra = request.POST["contraseña"]
        user = User.objects.create_user(name, mail, contra)
        user.save()
        login(request, user)
        uname= request.user.username

        Car1 = Carusel1.objects.raw('SELECT * FROM index_Carusel1')
        Car2 = Carusel2.objects.raw('SELECT * FROM index_Carusel2')
        Banners = Banner.objects.raw('SELECT * FROM index_Banner')
        Carro = Carrito.objects.filter(usuario_var = uname)
        CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
        context = {"Car1": Car1, "Car2": Car2, "Banners": Banners, "CarritoProductos": Carro, "CTotal": CarroTotal}
        return render(request, 'index/index.html', context)
     else:
        uname= request.user.username
        Car1 = Carusel1.objects.raw('SELECT * FROM index_Carusel1')
        Car2 = Carusel2.objects.raw('SELECT * FROM index_Carusel2')
        Banners = Banner.objects.raw('SELECT * FROM index_Banner')
        Carro = Carrito.objects.filter(usuario_var = uname)
        CarroTotal = Carrito.objects.filter(usuario_var = uname).aggregate(T = Sum('precio_producto'))
        context = {"Car1": Car1, "Car2": Car2, "Banners": Banners, "CarritoProductos": Carro, "CTotal": CarroTotal}
        return render(request, 'index/index.html', context)
        


        
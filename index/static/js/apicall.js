$(document).ready(function() {
    $("#enviar").click(function(){
        $.get("https://proyecto-ba762-default-rtdb.firebaseio.com/1.json",
            function(data){
                console.log(data);
                $.each(data.productos, function(i, item){
                    $("#productos").append("<div class='col-sm-4 bg-white'><div class='card m-2 min-vh-25 text-center shadow p-3 mb-5 bg-body rounded'><img src='"+
                     item.imagen +"' class='card-img-top'><div class='card-body'><p class='card-text'>"+
                      item.descripcion +"</p><p class='card-text'><em>"+
                      item.precio+"</em></p><a href='#' class='btn btn-primary'>Agregar al carrito</a></div></div></div>");
                });
            });
    });
});
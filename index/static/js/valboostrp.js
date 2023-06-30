$(document).ready(function() {
    $("#basic-form").validate({
        rules:{
            emailindex:{
                email:true,
                required:true
            },
            pwd:{
                required:true,
                minlength: 10
            }
        },
        messages:{
            emailindex:{
                email:"El correo ingresado no es válido",
                required:"Ingrese correo electronico"
            },
            pwd:{
                required:"Ingrese contraseña",
                minlength:"La contraseña debe tener minimo 10 caracteres"
            }
        }
    });
    $('#enviar-index').click(function() {
        if ($("#basic-form").valid()==false){

        }
    });
  });

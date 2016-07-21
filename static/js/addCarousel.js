$(document).ready(load)
var faIcon = {
  valid: 'fa fa-check-circle fa-lg text-success',
  invalid: 'fa fa-times-circle fa-lg',
  validating: 'fa fa-refresh'
}
function load(){
  var colapsed = $('#mainnav-menu').find('.active-link');
  if(colapsed.length){
      colapsed.removeClass('active-link');
  }

  $( "[href='/administrator/carousel/view/']" ).parent().addClass('active-link').parent().addClass('in').parent().addClass('active-sub active');

  $("#form-add-item").bootstrapValidator({
    excluded: [':disabled'],

    fields: {
      tittle:{
        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          }
        }
      },
      description:{

        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          }
        }
      },
      fileImage:{
        icon:'false',
        validators:{
          notEmpty:{
            message: "Seleccione una imagen"
          }
          /*file:{
            extension: 'jpeg, jpg, png',
            type: 'image/jpeg,image/png,image/jpg',
            message: 'La imagen no es valida'

          }*/
        }
      }

    }
  }).on("success.form.bv", function(e, data){
    e.preventDefault();
    var formData = new FormData( $( "form[name='form-add-item']" )[0] );
    var fileInput = $("form[name='form-add-item']").find("input[type=file]")[0]
    var file = fileInput.files && fileInput.files[0];
    if( file ) {
        var img = new Image();

        img.src = window.URL.createObjectURL( file );

        img.onload = function() {
            var width = img.naturalWidth,
                height = img.naturalHeight;

            window.URL.revokeObjectURL( img.src );

            if( width == 1200 && height == 800 ) {
              $.ajax({
                  url : '/administrator/carousel/insert/',
                  type : 'post',
                  data : formData,
                  async : true,
                  contentType: false,
                  processData: false,
                  success: function(data) {

                      if( data.status === '1' ) {

                        $.niftyNoty({
                            type: 'warning',
                            container : 'floating',
                            html : "<strong>Error:</strong><br>" + data.message,
                            timer : true ? 5000 : 0
                        });

                      } else if (data.status === '2') {
                        $.niftyNoty({
                            type: 'danger',
                            container : 'floating',
                            html : "<strong>Excelente:</strong><br>" + data.message,
                            timer : false ? 5000 : 0
                        });
                      }else if( data.status === '3' ) {
                        $.niftyNoty({
                            type: 'success',
                            container : 'floating',
                            html : "<strong>Excelente:</strong><br>" + data.message,
                            timer : true ? 5000 : 0
                        });
                        location.reload();
                      }
                  },
                  error: function (XMLHttpRequest, estado, errorS) {
                      var error = eval("(" + XMLHttpRequest.responseText + ")");
                      console.log(error.Message);
                      console.log(estado);
                      console.log(errorS);
                  },
                  complete: function (jqXHR, estado) {

                  }
              });
            }
            else {
              $.niftyNoty({
                  type: 'warning',
                  container : 'floating',
                  html : "<strong>Error:</strong><br>" + "La dimensión de la imagen debe de ser 1200 x 800",
                  timer : true ? 5000 : 0
              });
            }
        };
    }
    else { //No file was input or browser doesn't support client side reading

    }

  });

  $(".spanFigure").on('click', function(){
    var id = $(this).children(':nth-child(3)').val();
    var token = $(this).children(':nth-child(2)').val();
    var formData = new FormData();
    formData.append("idItem", id);
    formData.append("csrfmiddlewaretoken", token);
    $.ajax({
        url : '/administrator/carousel/view_item/',
        type : 'post',
        data : formData,
        async : true,
        contentType: false,
        processData: false,
        success: function(data) {

            if( data.status === '1' ) {

              $.niftyNoty({
                  type: 'warning',
                  container : 'floating',
                  html : "<strong>Error:</strong><br>" + data.message,
                  timer : true ? 5000 : 0
              });

            } else if (data.status === '2') {
              $.niftyNoty({
                  type: 'danger',
                  container : 'floating',
                  html : "<strong>Excelente:</strong><br>" + data.message,
                  timer : false ? 5000 : 0
              });
            }else if( data.status === '3' ) {
              $("#tittle").val(data.titulo);
              $("#description").val(data.caption);
            }
        },
        error: function (XMLHttpRequest, estado, errorS) {
            var error = eval("(" + XMLHttpRequest.responseText + ")");
            console.log(error.Message);
            console.log(estado);
            console.log(errorS);
        },
        complete: function (jqXHR, estado) {

        }
    });
  });
}

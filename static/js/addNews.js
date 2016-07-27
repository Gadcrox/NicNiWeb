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

  $( "[href='/administrator/news/add/']" ).parent().addClass('active-link').parent().addClass('in').parent().addClass('active-sub active');

  $("#editor").summernote({
    height: 600
  });

  $("#form-add-news").bootstrapValidator({
    excluded: [':disabled'],
    feedbackIcons: faIcon,
    fields:{
      title:{
        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          }
        }
      },
      titulo:{
        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          }
        }
      },
      tags:{
        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          }
        }
      }
    }

  }).on('success.form.bv', function( e, data) {
    e.preventDefault();
    var formData = new FormData( $( "form[name='form-add-news']" )[0] );
    formData.append('contenido', $("#editor").code());
    $.ajax({
        url : '/administrator/news/insert/',
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
                  timer : false ? 5000 : 0
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
                  timer : false ? 5000 : 0
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

  });
  $('#btnLimpiar').on('click', function(){
      location.reload();
  });


}

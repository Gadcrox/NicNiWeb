$(document).ready(load)
var faIcon = {
  valid: 'fa fa-check-circle fa-lg text-success',
  invalid: 'fa fa-times-circle fa-lg',
  validating: 'fa fa-refresh'
}
function load() {
  var colapsed = $('#mainnav-menu').find('.active-link');
  if(colapsed.length){
      colapsed.removeClass('active-link');
  }

  $( "[href='/administrator/accounts/add/']" ).parent().addClass('active-link').parent().addClass('in').parent().addClass('active-sub active');
  $("#form-add-account").bootstrapValidator({
    excluded: [':disabled'],
    feedbackIcons: faIcon,
    fields:{
      username:{
        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          }
        }
      },
      firstname:{
        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          }
        }
      },
      lastname:{
        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          }
        }
      },
      password:{
        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          },
          identical:{
            field: 'confirmpassword',
            message: 'La contraseña debe coincidir'
          },
          stringLength: {
  					min: 1,
  					max: 3,
  					message: 'La contraseña debe tener de 6-8 caracteres'
  				},
        }
      },
      confirmpassword:{
        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          },
          identical: {
  					field: 'password',
  					message: 'La contraseña debe coincidir'
  				}
        }
      },
      active:{
        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          }
        }
      }
    }
  }).on('success.form.bv', function(e, data) {

    e.preventDefault();
    var formData = new FormData( $( "form[name='form-add-account']" )[0] );
      $.ajax({
          url : '/administrator/accounts/insert/',
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

              } else if (data.status === 2) {
                $.niftyNoty({
                    type: 'danger',
                    container : 'floating',
                    html : "<strong>Excelente:</strong><br>" + data.message,
                    timer : true ? 5000 : 0
                });
              }else if( data.status === '3' ) {
                limpiar();
                $.niftyNoty({
                    type: 'success',
                    container : 'floating',
                    html : "<strong>Excelente:</strong><br>" + data.message,
                    timer : true ? 5000 : 0
                });
              
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
      limpiar();
  });

}

function limpiar() {
  $('#lblAdmin').niftyCheck('toggleOff');
  $('#lblActive').niftyCheck('toggleOff');
  $('#form-add-account').each(function(){
    this.reset();
  });
  $('#form-add-account :input').each(function(){
    if(this.nodeName != 'BUTTON'){
      $element = $(this).parent();
      var $icon = $element.find('i');
      $icon.removeClass(faIcon.valid);
      $icon.removeClass(faIcon.invalid);
      $element.children('div').children().removeClass("has-success");
      $element.children('div').children().children('div').find('small').remove();
      $element.children('div').children().removeClass("has-error");

    }

  });
}

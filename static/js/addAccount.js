$(document).ready(load)

function load() {
  var colapsed = $('#mainnav-menu').find('.active-link');
  if(colapsed.length){
      colapsed.removeClass('active-link');
  }
  var faIcon = {
		valid: 'fa fa-check-circle fa-lg text-success',
		invalid: 'fa fa-times-circle fa-lg',
		validating: 'fa fa-refresh'
	}
   $( "[href='/administrator/accounts/add/']" ).parent().addClass('active-link').parent().addClass('in').parent().addClass('active-sub active');

   $(document).on( 'submit' , "form[name='form-add-account']" ,function (evt) {
  //  $( '.load' ).removeClass( 'hide' );
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
      //$( '.load' ).addClass( 'hide' );
      evt.preventDefault();
    });

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
  					min: 6,
  					max: 8,
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
  }).on('success.field.bv', function(e, data) {
		// $(e.target)  --> The field element
		// data.bv      --> The BootstrapValidator instance
		// data.field   --> The field name
		// data.element --> The field element

		var $parent = data.element.parents('.form-group');

		// Remove the has-success class
		$parent.removeClass('has-success');
	});

  $('#btnLimpiar').on('click', function(){
      limpiar();
  });


}

function limpiar() {
  $('#lblAdmin').niftyCheck('toggleOff');
  $('#lblActive').niftyCheck('toggleOff');
  $('#form-add-account').each (function(){
    this.reset();
  });

}

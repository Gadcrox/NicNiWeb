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
    feedbackIcons: faIcon,
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
      }

    }
  }).on("success.form.bv", function(e, data){
    e.preventDefault();
    var formData = new FormData( $( "form[name='form-add-item']" )[0] );
  });
}

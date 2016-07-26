$(document).ready(load)
var faIcon = {
  valid: 'fa fa-check-circle fa-lg text-success',
  invalid: 'fa fa-times-circle fa-lg',
  validating: 'fa fa-refresh'
}
function load(){
  $("#editor").summernote({
    height: 500
  });

  $("#form-add-services").bootstrapValidator({
    excluded: [':disabled'],
    feedbackIcons: faIcon,
    fields:{
      titulo:{
        validators:{
          notEmpty:{
            message: "Este campo es requerido"
          }
        }
      }
    }
  }).on('success.form.bv',function(e, data){
      e.preventDefault();
      var formData = new FormData( $( "form[name='form-add-services']" )[0] );
      formData.append('descripcion', $("#editor").code());
      $.ajax({
          url : '/administrator/services/insert/',
          type : 'post',
          data : formData,
          async : true,
          contentType: false,
          processData: false,
          success: function(data) {

              if( data.status === '1' ) {

                $.niftyNoty({
                    type: 'danger',
                    container : 'floating',
                    html : "<strong>Error:</strong><br>" + data.message,
                    timer : true ? 5000 : 0
                });

              } else if (data.status === '2') {
                $.niftyNoty({
                    type: 'warning',
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
  });
}

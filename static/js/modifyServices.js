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
  $("#form-modify-services").bootstrapValidator({
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
      var formData = new FormData( $( "form[name='form-modify-services']" )[0] );
      formData.append('descripcion', $("#editor").code());
      $.ajax({
          url : '/administrator/services/update/',
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

  $(document).on('click','i.ace-icon.fa.fa-pencil.icon-lg', function(e){
    var idService = $.trim($($(this).parent().parent().parent().parent().children(":nth-child(1)")).text());
    $("#idService").val(idService);
    var formData = new FormData( $( "form[name='form-id-service']" )[0] );

    $.ajax({
            url : '/administrator/services/view_service/',
            type : 'post',
            data : formData,
            async : true,
            contentType: false,
            processData: false,
            success: function(data) {
              if(data.status == '3'){
                $("#idServiceForm").val(data.id);
                $("#titulo").val(data.titulo);
                $(".note-editable p").remove();
                $(".note-editable").append(data.descripcion);
                $("#div-modify").show('slow');
              }else if(data.status == '2') {
                $.niftyNoty({
                    type: 'warning',
                    container : 'floating',
                    html : "<strong>Excelente:</strong><br>" + data.message,
                    timer : false ? 5000 : 0
                });
              }else if (data.status == '1') {
                $.niftyNoty({
                    type: 'danger',
                    container : 'floating',
                    html : "<strong>Error:</strong><br>" + data.message,
                    timer : false ? 5000 : 0
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

  $("#btnCancelar").on("click", function(){
    location.reload();
  });
}

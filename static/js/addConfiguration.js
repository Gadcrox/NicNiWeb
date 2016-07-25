$(document).ready(load)

function load(){

  $("input[name='telefono']").mask('(999) 9999-9999');
  $('#editorHistoria').summernote({
    height: 500
  });

  $("#btnGuardar").on('click',function(){
    var formData = new FormData($( "form[name='form-modify-configuration']" )[0]);
    var codeHistoria = $("#editorHistoria").code();
    formData.append('historia', codeHistoria);
    formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
    $.ajax({
        url : '/administrator/configuration/update/',
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
  });
}

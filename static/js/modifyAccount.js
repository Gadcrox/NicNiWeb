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

  $( "[href='/administrator/accounts/modify/']" ).parent().addClass('active-link').parent().addClass('in').parent().addClass('active-sub active');

  $('#table-data').dataTable({
    "responsive": true,
    "language": {
      "lengthMenu": "Mostrar _MENU_ registros",
      "zeroRecords": "No se encontraron coincidencias...",
      "infoEmpty": "registros encontrados:",
      "infoFiltered": "(0 de 0)",
      "processing": "Procesando...",
      "search": "Buscar:",
      "info": "Páginas Mostradas: _PAGE_ de _PAGES_",
      "paginate": {
        "previous": '<i class="fa fa-angle-left"></i>',
        "next": '<i class="fa fa-angle-right"></i>'
      }
    }
  });
  $("#form-modify-account").bootstrapValidator({
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
      }
    }
  }).on('success.form.bv', function(e){
    e.preventDefault();
    var formData = new FormData( $( "form[name='form-modify-account']" )[0] );
      $.ajax({
          url : '/administrator/accounts/update/',
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
    var idAccount = $.trim($($(this).parent().parent().parent().parent().children(":nth-child(1)")).text());
    $("#idAccount").val(idAccount);
    var formData = new FormData( $( "form[name='form-id-account']" )[0] );

    $.ajax({
            url : '/administrator/accounts/view_account/',
            type : 'post',
            data : formData,
            async : true,
            contentType: false,
            processData: false,
            success: function(data) {
              if(data.status == '3'){
                $("#username").val(data.username);
                $("#firstname").val(data.firstname);
                $("#lastname").val(data.lastname);
                if(data.is_superuser == true){
                  $('#lblAdmin').niftyCheck('toggleOn');
                }
                if(data.is_active == true){
                  $('#lblActive').niftyCheck('toggleOn');
                }
              }else {

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
      $("#formModify").show('slow');
  });
}

function limpiar() {
  $('#lblAdmin').niftyCheck('toggleOff');
  $('#lblActive').niftyCheck('toggleOff');
  $('#form-modify-account').each(function(){
    this.reset();
  });
  $('#form-modify-account :input').each(function(){
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

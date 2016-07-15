$(document).ready(load)

function load(){
  var colapsed = $('#mainnav-menu').find('.active-link');
  if(colapsed.length){
      colapsed.removeClass('active-link');
  }

  $( "[href='/administrator/accounts/modify/']" ).parent().addClass('active-link').parent().addClass('in').parent().addClass('active-sub active');

  $('#table-data').dataTable( {
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
                $("#password").val(data.password);
                $("#confirmpassword").val(data.password);
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
  });
}

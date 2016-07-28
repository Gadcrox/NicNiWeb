$(document).ready(load)

function load(){
  $("#editor").summernote({
    height:500
  });
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

  $(document).on('click','i.ace-icon.fa.fa-pencil.icon-lg', function(e){
    var idNew = $.trim($($(this).parent().parent().parent().parent().children(":nth-child(1)")).text());
    $("#idNew").val(idNew);
    var formData = new FormData( $( "form[name='form-id-new']" )[0] );

    $.ajax({
            url : '/administrator/news/view_new/',
            type : 'post',
            data : formData,
            async : true,
            contentType: false,
            processData: false,
            success: function(data) {
              if(data.status == '3'){
                $("#autor").val(data.autor);
                $("#titulo").val(data.titulo);
                $("#tags").val(data.tags);
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
}

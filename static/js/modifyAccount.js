$(document).ready(load)

function load(){
  var colapsed = $('#mainnav-menu').find('.active-link');
  if(colapsed.length){
      colapsed.removeClass('active-link');
  }

  $( "[href='/administrator/accounts/modify/']" ).parent().addClass('active-link').parent().addClass('in').parent().addClass('active-sub active');

  $('#demo-dt-basic').dataTable( {
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
}

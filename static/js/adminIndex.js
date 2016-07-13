$(document).ready(load)

function load(){
  $.niftyNoty({
      type: 'dark',
      container : 'floating',
      html : "<strong>Bienvenido " + $(".username").html() + ",</strong><br>Que tenga muy buen día",
      timer : true ? 5000 : 0
  });
}

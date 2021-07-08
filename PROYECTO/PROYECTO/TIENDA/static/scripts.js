
/* DEFINO UN EDITOR WYSIWYG PARA EL CONTENIDO DEL ARTICULO */

document.addEventListener("DOMContentLoaded", function(event) {
    tinymce.init({
        selector: 'textarea#id_descripcion',
        menubar: false
      });
   
});
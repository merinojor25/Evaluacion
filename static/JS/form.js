$(document).ready(function() {
    $('#form').submit(function(event) {
      event.preventDefault();
      var name = $('#name').val();
      var email = $('#email').val();
      var password = $('#password').val();
      var confirmPassword = $('#confirm-password').val();
  
      // Validaciones de entrada
      if (name === '' || email === '' || password === '' || confirmPassword === '') {
        alert('Por favor, completa todos los campos.');
        return;
      }
  
      if (!email.includes('@') || !email.includes('.')) {
        alert('Por favor, introduce una dirección de correo electrónico válida.');
        return;
      }
  
      if (password !== confirmPassword) {
        alert('Las contraseñas no coinciden. Por favor, verifica e inténtalo de nuevo.');
        return;
      }
  
      // Llamada al servicio web
      $.ajax({
        url: 'index.html',
        type: 'POST',
        data: {
          name: name,
          email: email,
          password: password,
          confirmPassword: confirmPassword
        },
        success: function(data) {
          // Manejo de respuesta del servicio web
          if (data.success) {
            alert('Mensaje enviado correctamente.');
            $('#name').val('');
            $('#email').val('');
            $('#password').val('');
            $('#confirm-password').val('');
          } else {
            alert('Ha ocurrido un error al enviar el mensaje.');
          }
        },
        error: function() {
          alert('Ha ocurrido un error al enviar el mensaje.');
        }
      });
    });
  });
  
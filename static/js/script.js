        // JavaScript para manejar el "envío" del formulario
        document.addEventListener('DOMContentLoaded', () => {
            const submitButton = document.getElementById('submitButton');
            const confirmationMessage = document.getElementById('confirmationMessage');
            const contactForm = document.getElementById('contactForm');

            submitButton.addEventListener('click', (event) => {
                // Previene el comportamiento por defecto de un botón de tipo submit (aunque es type="button")
                event.preventDefault();

                // Muestra el mensaje de confirmación
                confirmationMessage.classList.remove('hidden');

                // Opcional: Reinicia el formulario después de un breve retraso
                setTimeout(() => {
                    contactForm.reset();
                    confirmationMessage.classList.add('hidden');
                }, 3000); // El mensaje se oculta después de 3 segundos
            });
        });
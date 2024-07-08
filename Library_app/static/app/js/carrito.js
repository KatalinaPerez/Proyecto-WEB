document.addEventListener("DOMContentLoaded", function () {
    var modal = document.getElementById("modal-confirmacion");
    var btnPagarModal = document.getElementById("btn-pagar-modal");
    var btnCancelar = document.getElementById("btn-cancelar");

    // Mostrar la ventana modal al hacer clic en el botón "Pagar"
    btnPagarModal.addEventListener("click", function () {
        modal.style.display = "block";
    });

    // Cerrar la ventana modal al hacer clic en el botón "Cancelar"
    btnCancelar.addEventListener("click", function () {
        modal.style.display = "none";
    });

    // Cerrar la ventana modal al hacer clic fuera de ella
    window.addEventListener("click", function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
});

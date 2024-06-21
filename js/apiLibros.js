const booksContainer = document.getElementById('book-container');

document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío del formulario y la recarga de la página
    const searchText = document.getElementById('search-input').value; // Obtener el valor del campo de búsqueda
    const URL = `https://www.googleapis.com/books/v1/volumes?q=${encodeURIComponent(searchText)}&printType=books&key=AIzaSyCIArC-oQMQEeAVANVdk49zJitA3fcL90Y`;
    
    fetch(URL)
        .then(response => {
            if (!response.ok) {
                throw new Error('La solicitud a la API falló');
            }
            return response.json();
        })
        .then(data => {
            booksContainer.innerHTML = ''; // Limpiar el contenedor de libros antes de agregar los nuevos resultados
            data.items.forEach(libro => {
                const titulo = libro.volumeInfo.title;
                const autor = libro.volumeInfo.authors ? libro.volumeInfo.authors.join(', ') : 'Autor desconocido';
                const imagenUrl = libro.volumeInfo.imageLinks ? libro.volumeInfo.imageLinks.thumbnail : 'https://via.placeholder.com/150';
                
                //Crao el div para mis libros
                const libroDiv = document.createElement('div');
                libroDiv.classList.add('libro');
                libroDiv.innerHTML = `
                    <img src="${imagenUrl}" alt="Portada libro">
                    <h3>${titulo}</h3>
                    <p>${autor}</p>
                `;
                //Con esto al hacer click en el libro me dirije al una pagina con el detalle
                libroDiv.addEventListener('click', () => {
                    const url = `detalle_libro.html?titulo=${encodeURIComponent(titulo)}&autor=${encodeURIComponent(autor)}&descripcion=${encodeURIComponent(libro.volumeInfo.description || 'Descripción no disponible')}`;
                    window.open(url, '_blank');
                });

                booksContainer.appendChild(libroDiv);
            });
        })
        .catch(error => {
            console.error('Error en solicitud de API: ', error);
        });
});
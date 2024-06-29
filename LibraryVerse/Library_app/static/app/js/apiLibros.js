document.addEventListener('DOMContentLoaded', function() {
    const booksContainer = document.getElementById('book-container');

    if (!booksContainer) {
        console.error('No se encontró el contenedor de libros');
        return;
    }

    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');

    if (!searchForm || !searchInput) {
        console.error('No se encontró el formulario de búsqueda o el campo de búsqueda');
        return;
    }

    searchForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Evitar el envío del formulario y la recarga de la página
        const searchText = searchInput.value; // Obtener el valor del campo de búsqueda
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
                    const autores = libro.volumeInfo.authors ? libro.volumeInfo.authors.join(', ') : 'Autor desconocido';
                    const imagenUrl = libro.volumeInfo.imageLinks ? libro.volumeInfo.imageLinks.thumbnail : 'https://via.placeholder.com/150';

                    // Crear el objeto con los datos del libro
                    const libroData = {
                        titulo: titulo,
                        autor: autores,
                        portada: imagenUrl
                    };

                    // Enviar los datos al backend Django usando fetch
                    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                    fetch('/guardar_libro/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrftoken // Incluye el token CSRF en los encabezados
                        },
                        body: JSON.stringify(libroData)
                    })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Error al guardar el libro');
                        }
                        return response.json();
                    })
                    .then(data => {
                        console.log('Libro guardado:', data);
                        // Puedes hacer algo con la respuesta si es necesario
                    })
                    .catch(error => {
                        console.error('Error al guardar el libro:', error);
                    });

                    // Crear el elemento HTML para mostrar el libro (como ya lo tenías)
                    const libroDiv = document.createElement('div');
                    libroDiv.classList.add('libro');
                    libroDiv.innerHTML = `
                        <img src="${imagenUrl}" alt="Portada libro">
                        <h3>${titulo}</h3>
                        <p>${autores}</p>
                    `;
                    libroDiv.addEventListener('click', () => {
                        const url = `detalle_libro.html?titulo=${encodeURIComponent(titulo)}&autor=${encodeURIComponent(autores)}&descripcion=${encodeURIComponent(libro.volumeInfo.description || 'Descripción no disponible')}`;
                        window.open(url, '_blank');
                    });

                    booksContainer.appendChild(libroDiv);
                });
            })
            .catch(error => {
                console.error('Error en solicitud de API: ', error);
            });
    });
});

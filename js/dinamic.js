document.addEventListener('DOMContentLoaded', function () {
    const header = document.querySelector("header");
    const footer = document.querySelector("footer");

    header.innerHTML = `
    <!-- ::: Barra de navegación ::: -->

    <div class="container-navbar fixed-top">

        <nav class="navbar container">
            
            <!-- ::: Logo ::: -->

            <div class="container-logo">
                <i class="fa-solid fa-book-bookmark"></i>
                <h1 class="logo"><a href="#">LibraryVerse</a></h1>
            </div>

            <!-- ::: Elementos de la barra ::: -->

            <ul class="menu">
                <li><a href="index.html">Inicio</a></li>
                <li><a href="libros.html">Libros</a></li>
                <li><a href="#">Comics</a></li>
                <li><a href="#">Mangas</a></li>
            </ul>

            <!-- ::: Usuario, Favoritos y Carrito ::: -->

            <div class="container-user">
                <a href="login.html"><i class="fa-solid fa-user"></i></a>
                <a href="#"><i class="fa-solid fa-heart"></i></a>
                <a href="cart.html"><i class="fa-solid fa-basket-shopping"></i></a>
            </div>

            <!-- ::: Barra de busqueda ::: -->

            <form class="search-form" id="search-form">
                <input type="search" id="search-input" placeholder="Buscar..." />
                <button class="btn-search" type="submit">
                    <i class="fa-solid fa-magnifying-glass"></i>
                </button>
            </form>
        </nav>
    </div>
    `;

    footer.innerHTML = `
    <div class="container container-footer">
        <div class="menu-footer">

            <!-- ::: Contacto ::: -->

            <div class="contact-info">
                <p class="title-footer">Información de Contacto</p>
                <ul>
                    <li>Mail: libraryverse@gmail.com</li>
                </ul>
                <div class="social-icons">
                    <span class="facebook">
                        <i class="fa-brands fa-facebook-f"></i>
                    </span>
                    <span class="x">
                        <i class="fa-brands fa-x-twitter"></i>
                    </span>
                    <span class="instagram">
                        <i class="fa-brands fa-instagram"></i>
                    </span>
                </div>
            </div>

            <!-- ::: Información ::: -->

            <div class="information">
                <p class="title-footer">Información</p>
                <ul>
                    <li><a href="#">Acerca de Nosotros</a></li>
                    <li><a href="#">Politicas de Privacidad</a></li>
                    <li><a href="#">Términos y condiciones</a></li>
                </ul>
            </div>

        </div>
    </div>
    `;

    const searchForm = document.getElementById('search-form');
    const booksContainer = document.getElementById('book-container');

    searchForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Evitar el envío del formulario y la recarga de la página
        const searchText = document.getElementById('search-input').value; // Obtener el valor del campo de búsqueda
        console.log('Search Text:', searchText); // Log de depuración

        const URL = `https://www.googleapis.com/books/v1/volumes?q=${encodeURIComponent(searchText)}&printType=books&key=AIzaSyCIArC-oQMQEeAVANVdk49zJitA3fcL90Y`;
        console.log('API URL:', URL); // Log de depuración

        fetch(URL)
            .then(response => {
                if (!response.ok) {
                    throw new Error('La solicitud a la API falló');
                }
                return response.json();
            })
            .then(data => {
                console.log('API Response:', data); // Log de depuración
                booksContainer.innerHTML = ''; // Limpiar el contenedor de libros antes de agregar los nuevos resultados
                data.items.forEach(libro => {
                    const titulo = libro.volumeInfo.title;
                    const autor = libro.volumeInfo.authors ? libro.volumeInfo.authors.join(', ') : 'Autor desconocido';
                    const imagenUrl = libro.volumeInfo.imageLinks ? libro.volumeInfo.imageLinks.thumbnail : 'https://via.placeholder.com/150';
                    
                    const libroDiv = document.createElement('div');
                    libroDiv.classList.add('libro');
                    libroDiv.innerHTML = `
                        <img src="${imagenUrl}" alt="Portada libro">
                        <h3>${titulo}</h3>
                        <p>${autor}</p>
                    `;
                    
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
});

/*const APIKey = 'AIzaSyCIArC-oQMQEeAVANVdk49zJitA3fcL90Y';
const QUERY = 'mar';*/
const URL = 'https://www.googleapis.com/books/v1/volumes?q=mar&printType=books&key=AIzaSyCIArC-oQMQEeAVANVdk49zJitA3fcL90Y';
const booksContainer = document.getElementById('book-container');

fetch(URL)
    .then(response =>{
        //Si la respuesta es exitosa
        if(!response.ok){
            throw new Error('La solicitud a la API falló')
        }
        return response.json();
        })

    .then(data=>{
        data.items.forEach(libro => {
            //const Idlibro = libro.id;****
            const titulo = libro.volumeInfo.title;
            //      Operador ternario
            /*Si "libro.volumeInfo.authors" es verdadero obtenemos el nombre del autor, si no ponemos "Autor desconocido"
             Si hay muchos autores, se separaran por coma */
            const autor = libro.volumeInfo.authors ? libro.volumeInfo.authors.join(', ') : 'Autor desconocido';
            /*Este tambien es un operador ternario. 
              thumbnail es un tamaño que me proporciona la misma API*/
            const imagenUrl = libro.volumeInfo.imageLinks ? libro.volumeInfo.imageLinks.thumbnail : 'https://via.placeholder.com/150';
            
            //Crao el div para mis libros
            const libroDiv = document.createElement('div');
            const libroImg = document.createElement('div');
            libroDiv.classList.add
            libroDiv.classList.add('libro')
            libroDiv.innerHTML = `
                <img src="${imagenUrl}" alt="Portada libro">
                <h3>${titulo}</h3>
                <p>${autor}</p>
            `;

            //Con esto al hacer click en el libro me dirije al una pagina con el detalle
            libroDiv.addEventListener('click',() => {
                const url = `detalle_libro.html?
                            titulo=${encodeURIComponent(titulo)}
                            autor=${encodeURIComponent(autor)}&
                            descripcion=${encodeURIComponent(book.volumeInfo.description ||'Descripción no disponible')}
                            `;
                window.open(url,'_blank');

            });
            /*libroDiv.addEventListener('click', () => {
                // Redirigir a la página del libro cuando se hace clic en él
                window.location.href = `detalle_libro.htmls?
                titulo=${encodeURIComponent(titulo)}&
                autor=${encodeURIComponent(autor)}&
                descripcion=${encodeURIComponent(libro.volumeInfo.description || 'Descripción no disponible')}`;
            });*/
            booksContainer.appendChild(libroDiv);


        });
    })

    .catch(error =>{
        console.error('Error en solicitud de API: ', error);
    });

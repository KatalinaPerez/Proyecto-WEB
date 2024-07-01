
const cargarMangas = async () => {
    try {
        const respuesta = await fetch(`https://api.jikan.moe/v4/top/manga`);

        console.log(respuesta);

        // Si la respuesta es correcta
        if (respuesta.status === 200) {
            const datos = await respuesta.json();

            let mangas = '';
            datos.data.forEach(manga => {
                mangas += `
			<div class="contenedor-items">
                <div class="item">
                <span class="titulo-item">${manga.title}</span>
                <img src="${manga.images.jpg.image_url}" alt="" class="img-item">
                <h3 class="precio-item">$15.000</h3>
                <button class="boton-item">Agregar al Carrito</button>
                </div>
            </div>
				`;
            });

            document.getElementById('mangaList').innerHTML = mangas;

        } else if (respuesta.status === 401) {
            console.log('Pusiste la llave mal');
        } else if (respuesta.status === 404) {
            console.log('El manga que buscas no existe');
        } else {
            console.log('Hubo un error y no sabemos que paso');
        }

    } catch (error) {
        console.log(error);
    }

}

cargarMangas();
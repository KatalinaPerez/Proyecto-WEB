const url = 'https://api.jikan.moe/v4/top/manga';

function makeCard (character){
    
    const {title,synopsis} = character;
    const contenedor = document.querySelector(".contenedor");

    const titulo = document.createElement("h5");
    titulo.textContent = title;

    const portada = document.createElement("img");
    portada.src = character.images.jpg.image_url;

    const resumen = document.createElement("p");
    resumen.textContent= synopsis;

    const Card = document.createElement("div");
    Card.appendChild(titulo);
    Card.appendChild(portada);
    Card.appendChild(resumen);

    contenedor.appendChild(Card);
} 

async function getManga(){
    try {
        const response = await fetch(url);
        const {data} = await response.json();

        for(let i = 0; i< data.length; i++){
            makeCard(data[i]);
        }
    } catch (error) {
        console.error(error);
    }

}
getManga();
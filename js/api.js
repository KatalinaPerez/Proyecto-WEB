$(function () {
    
        const settings = {
            async: true,
            crossDomain: true,
            url: 'https://myanimelist.p.rapidapi.com/manga/top/all',
            method: 'GET',
            headers: {
                'x-rapidapi-key': 'fc0fb70579msh955e56d05f10734p17e85cjsn0c1d06da3006',
                'x-rapidapi-host': 'myanimelist.p.rapidapi.com',
                'Content-Type': 'application/json'
            }
        };

        $.ajax(settings).done(function (response) {
            // Obtener el elemento donde se insertarán los datos
            var mangaList = $('#Resultado');

            // Iterar sobre cada elemento en la respuesta y mostrar los datos
            response.forEach(function (manga) {
                var mangaInfo = `
                    <div class="container-products">
                        <div class="card-product">
                            <div class="container-img">
                                <img src="${manga.picture_url}" alt="Manga Cover">
                            </div>
                            <div class="content-card-product">
                                <h2>Title: ${manga.title}</h2>
                                <p><strong>Rank:</strong> ${manga.rank}</p>
                                <p><strong>Score:</strong> ${manga.score}</p>
                                <p><strong>Type:</strong> ${manga.type}</p>
                            </div>
                        </div>
                    </div>
                    <hr>
                `;
                mangaList.append(mangaInfo);
            });
        });
    });
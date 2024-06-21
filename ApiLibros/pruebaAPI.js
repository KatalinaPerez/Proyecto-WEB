//https://www.googleapis.com/books/v1/volumes?q=mar&printType=books&key=AIzaSyCIArC-oQMQEeAVANVdk49zJitA3fcL90Y
v_q='mar';
fetch(`https://www.googleapis.com/books/v1/volumes?q=&printType=books&key=AIzaSyCIArC-oQMQEeAVANVdk49zJitA3fcL90Y`)
    .then(response =>{
        //Si la respuesta es exitosa
        if(!response.ok){
            throw new Error('La solicitud a la API falló')
        }
        return response.json();
        })

    .then(data=> {
        const booksContainer = document.getElementById('book-container');
        const librodata = data.data;   

    })

    .catch(error =>{
        console.error('Error en solicitud de API: ', error);
    });

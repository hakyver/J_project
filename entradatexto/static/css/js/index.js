const listacomentariosjs = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/entrada/2');
        const data = await response.json();
        let content = ''; // Define la variable content antes del bucle
        data.formularios.forEach((formularios, index) => {
            content +=
                `<tr>
                    <td>${index+1}</td>
                    <td>${formularios.nombre}</td>
                    <td>${formularios.nombre}</td>
                 </tr>`;
        });
        tablebody_comentarios.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener('load', async () => {
    await listacomentariosjs();
});
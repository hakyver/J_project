
const listacomentariosjs = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/entrada/2');
        const data = await response.json();
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await listacomentariosjs();
});
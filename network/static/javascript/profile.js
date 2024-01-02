// Manejo de los eventos follow.

const cantidad_seguidores = document.querySelector("#cantidad_seguidores");
const seguir = document.querySelector("#follow_button");

if (cantidad_seguidores && seguir) {
    seguir.addEventListener("click", () => {
        const username = seguir.dataset.usuario;
        const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    
        fetch(`/follow/${username}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrf_token,
            },
        })
        .then(response => response.json())
        .then(data => {
            cantidad_seguidores.textContent = `${data.seguidores} Seguidores`;
            seguir.textContent = (seguir.textContent === "Seguir") ? "Siguiendo" : "Seguir";
        })
        .catch(error => console.error("Error con la solicitud:", error));
    });
}
// Manejo de los eventos de Like.

const likes = document.querySelectorAll(".like_button");

likes.forEach(like => {
    like.addEventListener("click", () => {
        const post_id = like.dataset.postId;
        const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

        fetch(`/like_post/${post_id}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrf_token,
            },
        })
        .then(response => response.json())
        .then(data => {
            like.innerHTML = `${data.likes} Likes`;

            if (like.classList.contains("btn-light")) {
                like.classList.remove("btn-light");
                like.classList.add("btn-dark");
            } else {
                like.classList.remove("btn-dark");
                like.classList.add("btn-light");
            }
        })
        .catch(error => console.error("Error con la solicitud:", error));
    });
});

// Manejo de los eventos follow.

const cantidad_seguidores = document.querySelector("#cantidad_seguidores");
const seguir = document.querySelector("#follow_button");

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
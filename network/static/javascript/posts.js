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

// Manejo de la eliminación de publicaciones.

const deletes = document.querySelectorAll(".delete_post");

deletes.forEach(del_post => {
    del_post.addEventListener("click", () => {
        const post_id = del_post.dataset.postId;
        const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    
        fetch(`/del_post/${post_id}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrf_token,
            },
        })
        .then(response => {
            if (response.ok) {
                const contenedor = document.querySelector(`#post-${post_id}`);
                contenedor.innerHTML = "<h4 class='red_message'>Eliminaste esta publicación</h4>";
            } else {
                console.error("Error con la solicitud:", response.statusText);
            }
        })
        .catch(error => console.error("Error con la solicitud:", error));
    });
});

// Manejo de las ediciones de publicaciones.

const edits = document.querySelectorAll(".edit_post");
const send_edit = document.querySelectorAll(".submit_edit")

edits.forEach(edit_post => {
    edit_post.addEventListener("click", () => {
        const post_id = edit_post.dataset.postId;
        const post_estatico = document.querySelector(`#post-${post_id}`);
        const post_cambio = document.querySelector(`#edit-${post_id}`);

        post_cambio.style.display = (post_cambio.style.display === "block") ? "none" : "block";
        post_estatico.style.display = (post_cambio.style.display === "block") ? "none" : "block";
    });
});

send_edit.forEach(submit => {
    submit.addEventListener("click", () => {
        const post_id = submit.dataset.postId;
        const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

        const nuevo_post = document.querySelector(`#area-${post_id}`);
        const fe_data = {
            "nuevo_post" : nuevo_post.value
        }

        fetch(`/edit_post/${post_id}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrf_token,
            },
            body: JSON.stringify(fe_data),
        })
        .then(response => response.json())
        .then(data => {
            const post_estatico = document.querySelector(`#post-${post_id}`);
            const post_cambio = document.querySelector(`#edit-${post_id}`);
            const contenido = document.querySelector(`#content-${post_id}`);
    
            post_cambio.style.display = (post_cambio.style.display === "block") ? "none" : "block";
            post_estatico.style.display = (post_cambio.style.display === "block") ? "none" : "block";

            contenido.textContent = data.post_actualizado;
        })
        .catch(error => console.error("Error con la solicitud:", error));
    });
});
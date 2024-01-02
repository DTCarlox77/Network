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
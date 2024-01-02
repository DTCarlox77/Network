likes = document.querySelectorAll(".like_button");

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
        })
        .catch(error => console.error("Error con la solicitud:", error));
    });
});

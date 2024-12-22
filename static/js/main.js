htmx.on("htmx:beforeRequest", (e) => {
    try {
        const newURL = e.target.getAttribute("data-url");
        window.history.pushState({ page: "Post" }, "", newURL);
    } catch (error) {
        console.error(error);
    }
    console.log("HTMX EVENT:", e);
});

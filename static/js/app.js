document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("appSidebar");
    const sidebarToggle = document.getElementById("sidebarToggle");

    if (sidebar && sidebarToggle) {
        sidebarToggle.addEventListener("click", function () {
            sidebar.classList.toggle("is-open");
        });
    }
});
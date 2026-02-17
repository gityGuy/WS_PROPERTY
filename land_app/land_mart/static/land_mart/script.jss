document.addEventListener("DOMContentLoaded", function () {

    const tabs = document.querySelectorAll(".tab");

    tabs.forEach(tab => {
        tab.addEventListener("click", () => {
            tabs.forEach(t => t.classList.remove("active"));
            tab.classList.add("active");
        });
    });

    const searchBtn = document.querySelector(".search-btn");

    if (searchBtn) {
        searchBtn.addEventListener("click", () => {
            alert("Search feature coming soon on AG!");
        });
    }

});

document.addEventListener("DOMContentLoaded", function() {
    const yearElement = document.querySelector("#current-year");
    
    if (yearElement) {
        const currentYear = new Date().getFullYear();
        yearElement.textContent = currentYear;
    }
});
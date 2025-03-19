document.addEventListener('DOMContentLoaded', function() {
    // Navigation handling
    document.querySelectorAll('[data-page]').forEach(element => {
        element.addEventListener('click', function() {
            const pageId = this.getAttribute('data-page');
            showPage(pageId);
        });
    });

    function showPage(pageId) {
        // Hide all pages
        document.querySelectorAll('.page').forEach(page => {
            page.classList.remove('active');
        });

        // Show selected page
        const targetPage = document.getElementById(pageId);
        if (targetPage) {
            targetPage.classList.add('active');
        }

        // Update navigation active state
        document.querySelectorAll('.nav-link').forEach(nav => {
            nav.classList.remove('active');
            if (nav.getAttribute('data-page') === pageId) {
                nav.classList.add('active');
            }
        });

        // Scroll to top
        window.scrollTo(0, 0);
    }

    // Initialize with home page
    showPage('home');
});

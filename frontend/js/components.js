(function() {
    function initNavigation() {
        const userName = localStorage.getItem('user_name') || 'User';

        // Sidebar HTML
        const sidebarHTML = `
            <nav class="sidebar" id="sidebar">
                <div class="user-welcome">
                    <h2>Willkommen</h2>
                    <h1 id="userName">${userName}</h1>
                </div>
                <div style="flex: 1; overflow-y: auto;">
                    <ul class="nav-links">
                        <li><a href="dashboard.html"><i class="fas fa-home"></i> Startseite</a></li>
                        <li><a href="locations.html"><i class="fas fa-map-marker-alt"></i> Lagerorte</a></li>
                        <li><a href="shopping_list.html"><i class="fas fa-shopping-cart"></i> Einkaufsliste</a></li>
                        <li><a href="items.html"><i class="fas fa-box"></i> Alle Artikeln</a></li>
                        <li><a href="notifications.html"><i class="fas fa-bell"></i> Benachrichtigung</a></li>
                        <li><a href="profile.html"><i class="fas fa-user"></i> Mein Profil</a></li>
                    </ul>
                </div>
                <button class="btn-logout" id="logoutBtn">ABMELDEN</button>
            </nav>
        `;

        // Top-Bar HTML
        const topBarHTML = `
            <header class="top-bar">
                <div class="top-bar-left">
                    <i class="fas fa-bars" id="menuToggle"></i>
                    <div class="logo-placeholder" style="margin-left: 15px;">
                        <img src="/frontend/assets/logo.png" height="40" alt="TRACKit">
                    </div>
                </div>
                <div class="search-container">
                    <input type="text" placeholder="Suchen" id="searchInput">
                    <i class="fas fa-search" id="searchIcon"></i>
                </div>
            </header>
        `;

        const wrapper = document.querySelector('.dashboard-wrapper');
        const main = document.querySelector('.main-content');

        // Sidebar einfügen
        if (wrapper && !document.getElementById('sidebar')) {
            wrapper.insertAdjacentHTML('afterbegin', sidebarHTML);
        }

        if (main && !document.querySelector('.top-bar')) {
            main.insertAdjacentHTML('afterbegin', topBarHTML);
        }

        const sidebar = document.getElementById('sidebar');
        const menuToggle = document.getElementById('menuToggle');

        // Gespeicherten Zustand auf allen seiten anwenden
        if (sidebar && wrapper) {
            const isClosed = localStorage.getItem('sidebarClosed') === 'true';
            if (isClosed) {
                sidebar.classList.add('closed');
                wrapper.classList.add('sidebar-closed');
            }
        }

        if (menuToggle && sidebar && wrapper) {
            menuToggle.onclick = function() {
                sidebar.classList.toggle('closed');
                wrapper.classList.toggle('sidebar-closed');
                localStorage.setItem('sidebarClosed', sidebar.classList.contains('closed'));
            };
        }

        const logoutBtn = document.getElementById('logoutBtn');
        if (logoutBtn) {
            logoutBtn.onclick = () => {
                localStorage.clear();
                window.location.href = 'login.html';
            };
        }

        //Suchfunktionalität
        const searchInput = document.getElementById('searchInput');
        const searchIcon = document.getElementById('searchIcon');

        function performSearch() {
            const query = searchInput.value.trim();
            if (query) {
                window.location.href = `search_results.html?q=${encodeURIComponent(query)}`;
            }
        }

        if (searchInput) {
            // Suche bei Enter-Taste ausführen
            searchInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    performSearch();
                }
            });
        }

        if (searchIcon) {
            searchIcon.addEventListener('click', function() {
                performSearch();
            });
            searchIcon.style.cursor = 'pointer';
        }

        // Aktiven link hervorheben
        const currentPath = window.location.pathname;
        document.querySelectorAll('.nav-links a').forEach(link => {
            if (currentPath.includes(link.getAttribute('href'))) {
                link.parentElement.classList.add('active');
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initNavigation);
    } else {
        initNavigation();
    }
})();
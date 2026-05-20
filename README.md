# **TRACKit** - Inventarverwaltung

> _"Mach Ordnung leicht mit TRACKit"_

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-database-003B57?logo=sqlite&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green)

🌐 **Live Demo**: [TRACKit auf Render](https://inventorymanager-u6v6.onrender.com)

## Preview

![TRACKit Dashboard](/frontend/assets/sc.png)

Eine Inventarverwaltungs-App, mit der Benutzer ihre Artikel in verschiedenen Räumen organisieren können. Die Anwendung bietet automatische Einkaufslisten basierend auf Mindestbeständen, Ablaufdatum-Warnungen und eine übersichtliche Dashboard-Ansicht.

---

## Features

- **Benutzerverwaltung**: Registrierung und Anmeldung mit sicherer Passwort-Hashierung.
- **Raumverwaltung**: Erstellen und Organisieren von Lagerorten (Küche, Bad, Keller etc.)
- **Artikelverwaltung**: Artikel mit Bestand, Mindestmenge, Preis, Kategorue und Ablaufdatum
- **Automatische Einkaufsliste**: Generiert sich aus Artikeln unter Mindestbestand
- **Benachrichtigungen**: Warnungen bei niedrigem Bestand und bald ablaufenden Artikeln
- **Ausgabenübersicht**: Berechnung der Gesamtausgaben basierend auf Artikelpreisen
- **Responsive Design**: Funktioniert auf Desktop und Mobilgeräten

---

## Installation & Setup

1. **Clone the repository**

```bash
   git clone https://github.com/berinaademi/InventoryManager.git
   cd InventoryManager
```

2. **Create a virtual environment**

```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
   pip install -r requirements.txt
```

4. **Run the app**

```bash
   python app.py
```

5. **Open in browser**

```
   http://localhost:5000
```

---

## Technologien

### Backend:

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- Werkzeug
- SQLite

### Frontend:

- HTML5
- CSS3
- JavaScript
- Font Awesome
- LocalStorage

---

## Projektstruktur

```
trackit/
├── app.py # Flask-Anwendung & Konfiguration
├── config.py # Konfigurationseinstellungen
├── database.py # SQLAlchemy-Instanz
├── database.db # SQLite-Datenbank
├── requirements.txt # Python-Abhängigkeiten
│
├── models/
│ ├── __init__.py
│ ├── user.py # Benutzer-Model
│ ├── room.py # Raum-Model
│ └── item.py # Artikel-Model
│
├── services/
│ ├── user_service.py # Benutzer-Geschäftslogik
│ ├── room_service.py # Raum-Geschäftslogik
│ └── item_service.py # Artikel-Geschäftslogik
│
├── routes/
│ ├── user_routes.py # Benutzer-Endpunkte
│ ├── room_routes.py # Raum-Endpunkte
│ └── item_routes.py # Artikel-Endpunkte
│
└── frontend/
  ├── assets/
  │ ├── logo.png
  │ └── illustration.png
  │
  ├── css/
  │ └── style.css # Globale Styles
  │
  ├── js/
  │ ├── api.js # API-Verbindungstests
  │ └── components.js # Wiederverwendbare UI-Komponenten
  │
  └── html/
  ├── login.html # Anmeldeseite
  ├── register.html # Registrierungsseite
  ├── dashboard.html # Übersicht
  ├── locations.html # Lagerorte
  ├── rooms.html # Raumdetails
  ├── items.html # Alle Artikel
  ├── shopping_list.html # Einkaufsliste
  ├── notifications.html # Benachrichtigungen
  ├── profile.html # Benutzerprofil
  └── search_results.html # Suchergebnisse
```

---

_TRACKit für einfache Haushaltsverwaltung_

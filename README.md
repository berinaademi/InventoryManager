# **TRACKit** - Inventarverwaltung
> *"Mach Ordnung leicht mit TRACKit"*

Eine Inventawverwaltungs-App, mit der Benutzer ihre Artikel in verschiedenen Räumen organisieren können. Die Anwendung bietet automatische Einkaufslisten basierend auf Mindestbeständen, Ablaufdatum-Warnungen und eine übersichtliche Dashboard-Ansicht.

---

## Features
- **Benutzerverwaltung**: Registrierung und Anmeldung mit sicherer Passwort-Hashierung.
- **Raumverwaltung**: Erstellen und Organisieren von Lagerorten (Küche, Bad, Keller etc.)
- **Artikelverwaltung**: Artikel mit Bestand, Mindestmenge, Preis, Kategorue und Ablaufdatum
- **Automatische Einkaufsliste**: Generiert sich aus Artikeln unter Mindestbestand
- **Benachrichtigungen**: Warnungen bei niedrigem Bestand und bald ablaufenden Artikeln
- **Ausgabenübersicht**: Berechnung der Gesamtausgaben basierend auf Artikelpreisen
- **Responsive Desgin**: Funktioniert auf Desktop und Mobilgeräten

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

*TRACKit für einfache Haushaltsverwaltung*

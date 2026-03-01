# Route-Paket Initialisierung

from flask import Blueprint

# Blueprint für die Hauptrouten erstellen
main = Blueprint('main', __name__)

# Einzelne Routen-Module importieren
from app.routes import home, auth, dashboard, api

# Alle Blueprints in einer Liste bündeln
all_blueprints = [main, auth.auth_bp, dashboard.dash_bp, api.api_bp]

// Flask Debugger - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('Flask Debugger initialized');
    
    // Überprüfe, ob der Debug-Modus aktiv ist
    checkDebugMode();
    
    // FÜge interaktive Funktionen zu den Feature-Karten hinzu
    initializeFeatureCards();
    
    // Initialisiere den Statusprüfer
    initializeStatusChecker();
});

/**
 * Überprüft, ob der Debug-Modus aktiv ist und zeigt eine Warnung an, wenn dies der Fall ist
 */
function checkDebugMode() {
    const debugBadge = document.querySelector('.debug-badge');
    if (debugBadge) {
        console.warn('⚠️ DEBUG MODE IS ACTIVE - This should not be enabled in production!');
    }
}

/**
 * Füge interaktive Funktionen zu den Feature-Karten hinzu
 */
function initializeFeatureCards() {
    const featureCards = document.querySelectorAll('.feature-card');
    
    featureCards.forEach(card => {
        card.addEventListener('click', function() {
            // Optional: Füge Click Analytics oder zusätzliche Funktionalität hinzu
            console.log('Feature card clicked:', this.querySelector('h3').textContent);
        });
    });
}

/**
 * Periodisch den Status der Anwendung überprüfen
 */
function initializeStatusChecker() {
    // Status überprüfen, alle 30 Sekunden
    setInterval(async () => {
        try {
            const response = await fetch('/status');
            if (!response.ok) {
                console.error('Status check failed:', response.status);
            }
        } catch (error) {
            console.error('Error checking status:', error);
        }
    }, 30000);
}

/**
 * Format JSON zum displayen
 */
function formatJSON(obj) {
    return JSON.stringify(obj, null, 2);
}

/**
 * Text zum Clipboard kopieren
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        console.log('Copied to clipboard');
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

/**
 * Notifikationsanzeige displayen
 */
function showNotification(message, type = 'info') {
    // Notifikationselement erzeugen 
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Zur Seite hinzufügen 
    document.body.appendChild(notification);
    
    // Auto-remove nach 3 Sekunden
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Fuktion exportieren für den Nutzen in anderen Skripten
window.FlaskDebugger = {
    formatJSON,
    copyToClipboard,
    showNotification
};

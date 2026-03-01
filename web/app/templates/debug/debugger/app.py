"""
Flask Debugger Application
A development debugging tool for Flask applications
"""

from flask import Flask, render_template, request, jsonify, session
from werkzeug.debug import DebuggedApplication
import os
from dotenv import load_dotenv
import logging

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

logging.basicConfig(
    level=logging.DEBUG if os.getenv('FLASK_ENV') == 'development' else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

DEBUG_MODE = os.getenv('DEBUG', '0') == '1'
WERKZEUG_PIN = os.getenv('WERKZEUG_PIN', None)

if DEBUG_MODE:
    logger.warning("⚠️  DEBUG MODE IS ENABLED - DO NOT USE IN PRODUCTION!")
    app.debug = True
    if WERKZEUG_PIN:
        os.environ['WERKZEUG_DEBUG_PIN'] = WERKZEUG_PIN


@app.route('/')
def index():
    """Main landing page"""
    return render_template('index.html', debug_enabled=DEBUG_MODE)


@app.route('/status')
def status():
    """Application status endpoint"""
    return jsonify({
        'status': 'running',
        'debug_mode': DEBUG_MODE,
        'environment': os.getenv('FLASK_ENV', 'production'),
        'version': '1.0.0'
    })


@app.route('/debug/info')
def debug_info():
    """Debug information endpoint - only available in debug mode"""
    if not DEBUG_MODE:
        return jsonify({'error': 'Debug mode not enabled'}), 403
    
    return jsonify({
        'app_name': app.name,
        'config': {k: str(v) for k, v in app.config.items() if not k.startswith('SECRET')},
        'environment_variables': {
            'FLASK_ENV': os.getenv('FLASK_ENV'),
            'DEBUG': os.getenv('DEBUG'),
            'DATABASE_URL': os.getenv('DATABASE_URL', 'Not configured')
        }
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


@app.errorhandler(404)
def not_found(error):
    """Custom 404 handler"""
    if DEBUG_MODE:
        return render_template('404_debug.html'), 404
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Custom 500 handler"""
    logger.error(f"Internal server error: {error}")
    if DEBUG_MODE:
        return render_template('500_debug.html', error=str(error)), 500
    return render_template('500.html'), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '127.0.0.1')
    
    if DEBUG_MODE:
        logger.warning(f"Starting Flask app in DEBUG mode on {host}:{port}")
        app.run(host=host, port=port, debug=True)
    else:
        logger.info(f"Starting Flask app on {host}:{port}")
        app.run(host=host, port=port, debug=False)

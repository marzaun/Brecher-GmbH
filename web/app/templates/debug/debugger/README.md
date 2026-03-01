# Flask Debugger

A professional debugging and development tool for Flask applications. This debugger provides comprehensive insights into your Flask application's runtime behavior, configuration, and potential issues.

## Features

-  **Real-time Debugging** - Interactive debugging console for live code inspection
-  **Performance Monitoring** - Track request/response cycles and identify bottlenecks
-  **Security Analysis** - Built-in security checks and vulnerability scanning
-  **Detailed Logging** - Comprehensive logging with customizable log levels
-  **Error Tracking** - Automatic error detection and stack trace analysis
-  **Hot Reload** - Automatic application reload on code changes (development mode)

## Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Virtual environment (recommended)

### Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd debugger
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run the application:
```bash
python app.py
```



## Docker Deployment

### Using Docker Compose (Recommended)

```bash
docker-compose up -d
```

### Using Docker directly

```bash
docker build -t flask-debugger .

# Run container
docker run -p 5000:5000 --env-file .env flask-debugger
```

## Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_ENV` | Environment mode (development/production) | `production` |
| `DEBUG` | Enable debug mode (0/1) | `0` |
| `SECRET_KEY` | Secret key for session management | Required |
| `WERKZEUG_PIN` | PIN for Werkzeug debugger | Auto-generated |
| `HOST` | Server host address | `127.0.0.1` |
| `PORT` | Server port | `5000` |

### Debug Mode

**WARNING**: Debug mode should NEVER be enabled in production environments!

Debug mode provides:
- Interactive Python console in browser
- Detailed error pages with stack traces
- Automatic code reloading
- Access to application internals

To enable debug mode (development only):
```bash
DEBUG=1 python app.py
```

## API Endpoints

### Status Endpoint
```
GET /status
```
Returns application status and configuration.

### Health Check
```
GET /health
```
Returns health status for monitoring systems.

### Debug Information (Debug Mode Only)
```
GET /debug/info
```
Returns detailed debug information. Only available when `DEBUG=1`.

## Security Considerations

1. **Never enable debug mode in production**
   - Exposes sensitive application internals
   - Allows arbitrary code execution
   - Reveals configuration and environment variables

2. **Protect the Werkzeug PIN**
   - Keep `.env` file secure and out of version control
   - Use strong, random PIN values
   - Rotate PINs regularly

3. **Use HTTPS in production**
   - All production deployments should use TLS/SSL
   - Configure proper certificate management

4. **Environment Variables**
   - Never commit `.env` to version control
   - Use secret management systems in production
   - Regularly rotate sensitive credentials

## Development

### Project Structure

```
debugger/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── .env.example          # Environment template
├── .gitignore           # Git ignore rules
├── templates/           # HTML templates
│   ├── index.html
│   ├── 404.html
│   ├── 404_debug.html
│   ├── 500.html
│   └── 500_debug.html
├── static/              # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
└── logs/                # Application logs
```

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run with coverage
pytest --cov=app
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Common Issues

**Issue**: Application won't start
- Check if port 5000 is already in use
- Verify all environment variables are set
- Check Python version compatibility

**Issue**: Debug mode not working
- Ensure `DEBUG=1` in `.env`
- Check if WERKZEUG_PIN is set correctly
- Verify Flask is running in development mode

**Issue**: Docker container fails to start
- Check Docker logs: `docker logs flask-debugger`
- Verify `.env` file exists and is readable
- Ensure port 5000 is not in use

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask framework and the Pallets team
- Werkzeug debugging tools
- The Python community

## Support

For issues, questions, or contributions, please open an issue on the repository.

---

**Security Notice**: This is a debugging tool intended for development purposes only. Never deploy with debug mode enabled in production environments.

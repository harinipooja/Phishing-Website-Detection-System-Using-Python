# Phishing Website Detection System

A web-based application to help users identify potentially malicious websites through URL analysis. Built with Python, Flask, and rule-based detection methods.

## Features

- **URL Analysis**: Analyze website URLs for phishing indicators
- **Rule-Based Detection**: Transparent detection using multiple URL features
- **Risk Scoring**: Provides a risk score (0-100) based on analysis
- **Scan History**: Track all previously analyzed URLs
- **Modern UI**: Responsive design that works on desktop and mobile
- **Educational**: Provides safety tips and explanations

## Technology Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Detection**: Rule-based analysis (no ML required for basic version)

## Project Structure

```
chumma3/
├── app.py                 # Flask application with all routes
├── detector.py            # URL feature extraction and detection logic
├── database.py            # SQLite database operations
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   ├── base.html         # Base template with navigation
│   ├── home.html         # Home page
│   ├── analyze.html      # URL analysis page
│   ├── result.html       # Result display page
│   ├── history.html      # Scan history page
│   └── about.html        # About project page
└── static/
    ├── css/
    │   └── style.css     # Styling
    └── js/
        └── script.js     # Frontend JavaScript
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Navigate to the project directory**
   ```bash
   cd chumma3
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open the application in your browser**
   
   The application will be available at: `http://localhost:5001`

3. **Stop the server**
   
   Press `Ctrl+C` in the terminal to stop the server.

## Usage

### Analyzing a URL

1. Click on "Analyze URL" in the navigation menu
2. Enter a website URL (e.g., `https://example.com`)
3. Click the "Check URL" button
4. View the analysis results with risk score and explanations

### Viewing Scan History

1. Click on "History" in the navigation menu
2. View all previously analyzed URLs
3. Click "Clear History" to remove all records

### About the Project

1. Click on "About" in the navigation menu
2. Read about the project, architecture, and features

## Testing with Sample URLs

### Legitimate URLs (Should show "Likely Legitimate")
- `https://www.google.com`
- `https://amazon.com`
- `https://facebook.com`

### Suspicious URLs (Should show "Suspicious")
- `http://192.168.1.1/login` (IP address)
- `http://secure-bank-verify.com/account` (Suspicious words)
- `http://example@fake-site.com` (@ symbol)

## Detection Features

The system analyzes the following URL features:

- URL length
- Presence of IP address instead of domain name
- HTTPS encryption
- Number of subdomains
- Suspicious words (login, verify, bank, etc.)
- Suspicious top-level domains
- Special characters (@, -, etc.)
- Domain characteristics

## Important Notes

- **This tool is for educational purposes only**
- **Results are estimates, not guarantees**
- **Never automatically visit submitted URLs**
- **HTTPS alone does not prove legitimacy**
- **Always verify through official channels**

## Security Considerations

- The system does not visit or fetch content from submitted URLs
- No personal information or passwords are collected
- Input validation prevents malicious input
- Safe HTML rendering prevents XSS attacks

## Troubleshooting

### Port already in use

If port 5000 is already in use, you can change the port in `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change to 5001 or another port
```

### Database errors

If you encounter database errors, delete the `phishing_detector.db` file and restart the application. The database will be automatically recreated.

### Import errors

Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## Future Enhancements

- Machine learning model integration
- Real-time domain reputation checking
- Browser extension
- API for integration with other tools
- Multi-language support
- User authentication

## License

This project is for educational purposes. Use responsibly and ethically.

## Disclaimer

This tool provides an estimate based on URL analysis only. It cannot guarantee website safety. Always exercise caution when visiting unfamiliar websites. The developers are not responsible for any damages or losses resulting from the use of this tool.

## Contact

For questions or issues, please refer to the project documentation or contact your instructor.

---

**Built with ❤️ for educational purposes**

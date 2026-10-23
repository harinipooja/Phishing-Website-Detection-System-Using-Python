# Phishing Website Detection System - Project Documentation

## Abstract

The Phishing Website Detection System is a web-based application designed to help users identify potentially malicious websites before visiting them. With the increasing prevalence of phishing attacks through SMS, email, and social media, users need a simple and effective tool to analyze suspicious URLs. This system uses rule-based detection methods to examine various URL characteristics such as length, IP address presence, HTTPS encryption, suspicious words, and domain patterns. The application provides users with a risk score, detailed analysis, and safety tips to make informed decisions about website safety. Built with Python, Flask, and SQLite, the system offers a user-friendly interface with features including URL analysis, scan history tracking, and educational content about online security.

## Problem Statement

Internet users frequently receive fake website links through various communication channels including SMS, email, and social media platforms. These malicious links often imitate legitimate banking, shopping, or other trusted websites with the intent to steal passwords, personal information, and financial data. Phishing attacks have become increasingly sophisticated, making it difficult for average users to distinguish between legitimate and malicious websites.

**Key Problems:**
- Users lack easy-to-use tools to verify website legitimacy
- Manual verification is time-consuming and requires technical knowledge
- Existing security tools are often complex or expensive
- Users are vulnerable to social engineering attacks
- No centralized system to track and learn from previous encounters with suspicious URLs

**Impact:**
- Financial losses due to stolen credentials
- Identity theft and privacy breaches
- Loss of trust in online services
- Emotional distress and anxiety for victims

## Objectives

### Primary Objectives

1. **Develop a User-Friendly URL Analysis Tool**
   - Create an intuitive web interface for URL input
   - Provide real-time analysis with clear results
   - Ensure accessibility for non-technical users

2. **Implement Transparent Detection Methods**
   - Use rule-based analysis for clear explanations
   - Avoid black-box algorithms that users cannot understand
   - Provide detailed reasons for each classification

3. **Educate Users About Online Safety**
   - Offer safety tips based on analysis results
   - Explain common phishing techniques
   - Promote security awareness

4. **Maintain Scan History**
   - Store analysis results for future reference
   - Allow users to track patterns in suspicious URLs
   - Provide option to clear history for privacy

### Secondary Objectives

5. **Ensure System Security**
   - Never automatically visit submitted URLs
   - Protect against malicious input
   - Prevent XSS and other web vulnerabilities

6. **Provide Responsive Design**
   - Ensure compatibility with mobile devices
   - Maintain usability across different screen sizes
   - Optimize for various browsers

7. **Create Extensible Architecture**
   - Design for future ML integration
   - Allow for additional detection rules
   - Support API development

## Existing System vs Proposed System

### Existing Approaches

| Aspect | Current Approach | Limitations |
|--------|----------------|-------------|
| **Verification** | Manual URL inspection | Time-consuming, requires expertise |
| **Security Tools** | Browser extensions, antivirus | Often complex, may miss sophisticated attacks |
| **Blacklisting** | Known malicious URL databases | Cannot detect new phishing sites |
| **User Awareness** | Security education programs | Limited reach, not always practical |
| **History Tracking** | None or manual notes | Difficult to maintain and reference |

### Proposed System

| Aspect | Proposed Solution | Advantages |
|--------|-------------------|------------|
| **Verification** | Automated rule-based analysis | Fast, accessible, no expertise needed |
| **Detection Method** | Transparent rule-based system | Users understand why a URL is flagged |
| **Coverage** | Heuristic analysis | Can detect new and unknown phishing attempts |
| **User Interface** | Simple web application | Easy to use for all skill levels |
| **History Tracking** | Automatic database storage | Easy reference, pattern recognition |
| **Educational Value** | Built-in tips and explanations | Improves user security awareness |

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface Layer                  │
│  (HTML, CSS, JavaScript - Responsive Web Interface)    │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   Application Layer                       │
│              (Flask - Web Server & Routing)             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ Home Route   │  │ Analyze Route│  │ History Route│  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   Detection Layer                        │
│            (URL Feature Extraction & Analysis)           │
│  ┌──────────────────────────────────────────────────┐  │
│  │ • URL Length Analysis                            │  │
│  │ • IP Address Detection                           │  │
│  │ • HTTPS Verification                             │  │
│  │ • Subdomain Counting                             │  │
│  │ • Suspicious Word Matching                       │  │
│  │ • Domain Pattern Analysis                        │  │
│  │ • Risk Score Calculation                         │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                    Data Layer                            │
│              (SQLite - Scan History Storage)             │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Table: scan_history                              │  │
│  │ - id, url, result, risk_score, reasons, date     │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

1. **User Input**: User enters URL through web interface
2. **Validation**: Flask validates URL format
3. **Feature Extraction**: Detector extracts URL features
4. **Analysis**: Rules applied to calculate risk score
5. **Classification**: URL classified as legitimate/suspicious
6. **Storage**: Result saved to SQLite database
7. **Display**: Results shown to user with explanations

## Module Descriptions

### 1. app.py (Flask Application)

**Purpose**: Main application file handling web server and routing

**Key Functions**:
- `home()`: Renders the home page
- `analyze()`: Handles URL submission and analysis
- `result()`: Displays analysis results with safety tips
- `history()`: Shows scan history from database
- `clear_history()`: Clears all scan records
- `about()`: Displays project information

**Dependencies**: Flask, detector, database

### 2. detector.py (URL Detection Logic)

**Purpose**: Extracts features from URLs and performs phishing detection

**Key Classes**:
- `URLDetector`: Main detection class with analysis methods

**Key Methods**:
- `is_valid_url()`: Validates URL format
- `extract_features()`: Extracts URL characteristics
- `calculate_risk_score()`: Computes risk score based on features
- `classify_url()`: Classifies URL as legitimate or suspicious

**Detection Features**:
- URL length analysis
- IP address detection
- HTTPS verification
- Subdomain counting
- Suspicious word matching
- Domain pattern analysis
- Special character detection

**Dependencies**: urllib.parse, re, ipaddress

### 3. database.py (Database Operations)

**Purpose**: Manages SQLite database for scan history

**Key Functions**:
- `get_db_connection()`: Creates database connection
- `init_database()`: Initializes database tables
- `add_scan_record()`: Saves scan results
- `get_scan_history()`: Retrieves scan history
- `clear_scan_history()`: Deletes all records
- `get_scan_count()`: Returns total scan count

**Database Schema**:
```sql
CREATE TABLE scan_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    result TEXT NOT NULL,
    risk_score INTEGER,
    reasons TEXT,
    scan_date TEXT NOT NULL
)
```

**Dependencies**: sqlite3, datetime

### 4. Templates (HTML Pages)

**base.html**: Base template with navigation and common layout

**home.html**: Landing page with features overview and statistics

**analyze.html**: URL input form with example URLs

**result.html**: Displays analysis results with risk score and safety tips

**history.html**: Table showing all previous scans with clear option

**about.html**: Comprehensive project documentation

### 5. static/css/style.css (Styling)

**Purpose**: Provides modern, responsive styling

**Key Features**:
- Gradient background
- Card-based layout
- Responsive design for mobile
- Color-coded results (green for safe, red for suspicious)
- Animations for user engagement
- Accessible color contrast

### 6. static/js/script.js (Frontend Logic)

**Purpose**: Handles client-side interactions

**Key Functions**:
- Flash message auto-dismiss
- Form submission loading states
- URL input validation
- Example URL selection
- Risk score animation

## Detection Algorithm

### Risk Score Calculation

The system uses a weighted scoring mechanism:

| Feature | Weight | Condition | Points Added |
|---------|--------|-----------|--------------|
| URL Length | 15 | > 75 characters | +15 |
| URL Length | 10 | > 54 characters | +10 |
| IP Address | 25 | Present | +25 |
| HTTPS | 10 | Not present | +10 |
| Subdomains | 15 | > 3 subdomains | +15 |
| Subdomains | 5 | > 1 subdomain | +5 |
| Suspicious Words | 20 | > 2 words | +20 |
| Suspicious Words | 10 | > 0 words | +10 |
| Suspicious TLD | 15 | Present | +15 |
| @ Symbol | 20 | Present | +20 |
| Dash in Domain | 10 | Present | +10 |
| Special Characters | 5 | Present | +5 |
| Legitimate Domain | -30 | Known legitimate | -30 |

### Classification Rules

- **Risk Score ≥ 50**: Suspicious
- **Risk Score 25-49**: Suspicious
- **Risk Score 10-24**: Suspicious
- **Risk Score < 10**: Likely Legitimate

## Testing Procedure

### Unit Testing

1. **URL Validation Testing**
   - Test valid URLs: `https://google.com`
   - Test invalid URLs: `not-a-url`
   - Test edge cases: empty strings, special characters

2. **Feature Extraction Testing**
   - Test IP address detection
   - Test HTTPS detection
   - Test subdomain counting
   - Test suspicious word matching

3. **Risk Score Testing**
   - Test legitimate URLs (should score low)
   - Test suspicious URLs (should score high)
   - Test edge cases (boundary values)

### Integration Testing

1. **Database Operations**
   - Test record insertion
   - Test record retrieval
   - Test history clearing
   - Test database initialization

2. **Flask Routes**
   - Test home page loading
   - Test URL submission
   - Test result display
   - Test history page
   - Test navigation

### End-to-End Testing

1. **Complete User Flow**
   ```
   1. Open application
   2. Navigate to Analyze page
   3. Enter legitimate URL
   4. Submit and view results
   5. Check history page
   6. Clear history
   7. Repeat with suspicious URL
   ```

2. **Sample Test Cases**

   **Test Case 1: Legitimate URL**
   - Input: `https://www.google.com`
   - Expected Result: Likely Legitimate
   - Expected Risk Score: < 10

   **Test Case 2: IP Address URL**
   - Input: `http://192.168.1.1/login`
   - Expected Result: Suspicious
   - Expected Risk Score: ≥ 25

   **Test Case 3: Suspicious Words**
   - Input: `http://secure-bank-verify.com/account`
   - Expected Result: Suspicious
   - Expected Risk Score: ≥ 25

   **Test Case 4: Invalid URL**
   - Input: `not-a-valid-url`
   - Expected Result: Invalid
   - Expected Behavior: Error message

### Browser Compatibility Testing

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari (if available)

### Responsive Design Testing

- Desktop (1920x1080)
- Laptop (1366x768)
- Tablet (768x1024)
- Mobile (375x667)

## Security Considerations

### Input Validation

- URL format validation before processing
- Sanitization of user input
- Prevention of SQL injection through parameterized queries

### Output Encoding

- Safe HTML rendering using Jinja2 auto-escaping
- Prevention of XSS attacks
- No direct execution of user-provided code

### Data Protection

- No automatic URL fetching (prevents server-side attacks)
- No collection of personal information
- Local SQLite database (no external data transmission)

### Error Handling

- Generic error messages to users
- Detailed error logging for developers
- Graceful degradation on errors

## Future Enhancements

### Short-term Enhancements

1. **Machine Learning Integration**
   - Train a classifier using labeled phishing datasets
   - Improve detection accuracy beyond rule-based methods
   - Implement model versioning and updates

2. **Real-time Domain Reputation**
   - Integrate with domain reputation APIs
   - Check against known blacklists
   - Verify SSL certificate validity

3. **Browser Extension**
   - Chrome extension for quick URL analysis
   - Firefox extension support
   - Context menu integration

### Long-term Enhancements

4. **API Development**
   - RESTful API for third-party integration
   - Rate limiting and authentication
   - API documentation

5. **Advanced Heuristics**
   - Visual similarity detection (homograph attacks)
   - Brand impersonation detection
   - Behavioral analysis of landing pages

6. **User Features**
   - User authentication and accounts
   - Personalized scan history
   - Custom alert settings
   - Reporting mechanism for new phishing sites

7. **Multi-language Support**
   - Internationalization (i18n)
   - Localization for different regions
   - Region-specific phishing patterns

8. **Mobile Application**
   - Native iOS and Android apps
   - Push notifications for alerts
   - Offline mode capability

## Conclusion

The Phishing Website Detection System provides a valuable tool for internet users to identify potentially malicious websites. By implementing transparent rule-based detection, the system offers users clear explanations for why a URL might be suspicious, rather than relying on black-box algorithms.

The project successfully addresses the problem of phishing attacks by:
- Providing an accessible, user-friendly interface
- Using transparent detection methods that users can understand
- Educating users about online safety through detailed explanations
- Maintaining a history of scans for pattern recognition
- Ensuring security by never automatically visiting submitted URLs

While no system can guarantee 100% accuracy in detecting phishing websites, this project serves as an important step towards improving online security awareness. The modular architecture allows for future enhancements, including machine learning integration and real-time reputation checking.

The system is designed with beginners in mind, using simple, well-organized code that is easy to understand and modify. This makes it an excellent educational project for students learning about web development, cybersecurity, and Python programming.

**Key Achievements:**
- Fully functional web application with all required features
- Transparent rule-based detection system
- Modern, responsive user interface
- Complete scan history functionality
- Comprehensive documentation
- Security-focused design

**Limitations:**
- Rule-based detection may miss sophisticated attacks
- No real-time domain reputation checking
- Limited to URL analysis only (does not check page content)
- Risk scores are estimates, not guarantees

**Overall Impact:**
This project demonstrates how simple web technologies can be combined to create a useful security tool that helps protect users from phishing attacks. It serves as both a practical application and an educational resource for understanding cybersecurity concepts.

---

**Project Status**: Complete and Ready for Use
**Last Updated**: October 2024
**Version**: 1.0.0

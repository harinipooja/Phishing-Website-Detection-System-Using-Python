from flask import Flask, render_template, request, redirect, url_for, flash
from detector import URLDetector
from database import init_database, add_scan_record, get_scan_history, clear_scan_history, get_scan_count

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Initialize detector
detector = URLDetector()

# Initialize database
init_database()

@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    """Render the URL analysis page and process URL submission."""
    if request.method == 'POST':
        url = request.form.get('url', '').strip()
        
        if not url:
            flash('Please enter a URL to analyze.', 'error')
            return render_template('analyze.html')
        
        # Analyze the URL
        analysis_result = detector.classify_url(url)
        
        if analysis_result['result'] == 'Invalid':
            flash('Invalid URL format. Please enter a valid URL (e.g., https://example.com).', 'error')
            return render_template('analyze.html')
        
        # Save to database
        add_scan_record(
            url=url,
            result=analysis_result['result'],
            risk_score=analysis_result['risk_score'],
            reasons=analysis_result['reasons']
        )
        
        # Redirect to result page
        return redirect(url_for('result', url=url))
    
    return render_template('analyze.html')

@app.route('/result')
def result():
    """Render the result page with analysis details."""
    url = request.args.get('url', '')
    
    if not url:
        flash('No URL provided for analysis.', 'error')
        return redirect(url_for('analyze'))
    
    # Analyze the URL again for display
    analysis_result = detector.classify_url(url)
    
    # Generate safety tips based on result
    safety_tips = []
    if analysis_result['result'] == 'Suspicious':
        safety_tips = [
            "Do not enter any personal information on this website.",
            "Verify the website URL carefully before proceeding.",
            "Look for spelling errors or slight variations in the domain name.",
            "Check if the website has a valid SSL certificate.",
            "Contact the official company through their verified channels to confirm.",
            "Report this URL to your IT department or cybersecurity team."
        ]
    elif analysis_result['result'] == 'Likely Legitimate':
        safety_tips = [
            "Still exercise caution when entering sensitive information.",
            "Ensure the website uses HTTPS encryption.",
            "Verify the website's contact information and privacy policy.",
            "Look for trust seals and security badges.",
            "Use strong, unique passwords for each website."
        ]
    else:
        safety_tips = [
            "Please verify the URL format and try again.",
            "Ensure the URL starts with http:// or https://",
            "Check for any typos in the URL."
        ]
    
    return render_template('result.html', 
                         url=url,
                         result=analysis_result['result'],
                         risk_score=analysis_result['risk_score'],
                         reasons=analysis_result['reasons'],
                         features=analysis_result['features'],
                         safety_tips=safety_tips)

@app.route('/history')
def history():
    """Render the scan history page."""
    records = get_scan_history()
    scan_count = get_scan_count()
    return render_template('history.html', records=records, scan_count=scan_count)

@app.route('/clear-history', methods=['POST'])
def clear_history():
    """Clear all scan history."""
    clear_scan_history()
    flash('Scan history has been cleared.', 'success')
    return redirect(url_for('history'))

@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

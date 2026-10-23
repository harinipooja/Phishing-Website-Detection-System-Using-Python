import re
from urllib.parse import urlparse
from ipaddress import ip_address

class URLDetector:
    """URL feature extraction and phishing detection logic."""
    
    def __init__(self):
        self.suspicious_words = [
            'login', 'signin', 'verify', 'account', 'secure', 'bank',
            'update', 'confirm', 'password', 'credential', 'wallet',
            'crypto', 'bitcoin', 'paypal', 'amazon', 'apple', 'microsoft',
            'google', 'facebook', 'instagram', 'twitter', 'support',
            'security', 'alert', 'urgent', 'suspended', 'blocked'
        ]
        
        self.suspicious_tlds = ['.xyz', '.top', '.zip', '.mov', '.tk', '.ml', '.ga', '.cf']
        
        self.legitimate_domains = [
            'google.com', 'facebook.com', 'amazon.com', 'apple.com',
            'microsoft.com', 'paypal.com', 'twitter.com', 'instagram.com',
            'linkedin.com', 'netflix.com', 'ebay.com', 'walmart.com'
        ]
    
    def is_valid_url(self, url):
        """Validate if the input is a properly formatted URL."""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
    
    def extract_features(self, url):
        """Extract various features from the URL for analysis."""
        features = {
            'url_length': len(url),
            'has_ip_address': False,
            'has_https': False,
            'subdomain_count': 0,
            'has_suspicious_words': [],
            'has_suspicious_tld': False,
            'has_at_symbol': False,
            'has_dash': False,
            'has_special_chars': False,
            'domain_length': 0,
            'path_length': 0,
            'is_legitimate_domain': False
        }
        
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            
            # Check for HTTPS
            features['has_https'] = parsed.scheme == 'https'
            
            # Check for IP address
            try:
                ip_address(domain.split(':')[0])
                features['has_ip_address'] = True
            except:
                pass
            
            # Count subdomains
            domain_parts = domain.split('.')
            features['subdomain_count'] = max(0, len(domain_parts) - 2)
            
            # Check for suspicious words
            url_lower = url.lower()
            for word in self.suspicious_words:
                if word in url_lower:
                    features['has_suspicious_words'].append(word)
            
            # Check for suspicious TLD
            for tld in self.suspicious_tlds:
                if domain.endswith(tld):
                    features['has_suspicious_tld'] = True
                    break
            
            # Check for @ symbol
            features['has_at_symbol'] = '@' in url
            
            # Check for dash in domain
            features['has_dash'] = '-' in domain
            
            # Check for special characters
            special_chars = ['%', '&', '=', '?', '$', '#']
            for char in special_chars:
                if char in url:
                    features['has_special_chars'] = True
                    break
            
            # Domain length
            features['domain_length'] = len(domain)
            
            # Path length
            features['path_length'] = len(parsed.path)
            
            # Check if it's a legitimate domain
            for legit_domain in self.legitimate_domains:
                if domain == legit_domain or domain.endswith('.' + legit_domain):
                    features['is_legitimate_domain'] = True
                    break
                    
        except Exception as e:
            print(f"Error extracting features: {e}")
        
        return features
    
    def calculate_risk_score(self, features):
        """Calculate risk score based on extracted features."""
        score = 0
        reasons = []
        
        # URL length check
        if features['url_length'] > 75:
            score += 15
            reasons.append("URL is unusually long")
        elif features['url_length'] > 54:
            score += 10
            reasons.append("URL is longer than normal")
        
        # IP address check
        if features['has_ip_address']:
            score += 25
            reasons.append("URL contains IP address instead of domain name")
        
        # HTTPS check
        if not features['has_https']:
            score += 10
            reasons.append("URL does not use HTTPS")
        
        # Subdomain count
        if features['subdomain_count'] > 3:
            score += 15
            reasons.append("URL has too many subdomains")
        elif features['subdomain_count'] > 1:
            score += 5
            reasons.append("URL has multiple subdomains")
        
        # Suspicious words
        if len(features['has_suspicious_words']) > 2:
            score += 20
            reasons.append(f"URL contains suspicious words: {', '.join(features['has_suspicious_words'][:3])}")
        elif len(features['has_suspicious_words']) > 0:
            score += 10
            reasons.append(f"URL contains suspicious words: {', '.join(features['has_suspicious_words'][:3])}")
        
        # Suspicious TLD
        if features['has_suspicious_tld']:
            score += 15
            reasons.append("URL uses suspicious top-level domain")
        
        # @ symbol
        if features['has_at_symbol']:
            score += 20
            reasons.append("URL contains @ symbol")
        
        # Dash in domain
        if features['has_dash']:
            score += 10
            reasons.append("Domain contains dashes")
        
        # Special characters
        if features['has_special_chars']:
            score += 5
            reasons.append("URL contains unusual special characters")
        
        # Legitimate domain (reduces risk)
        if features['is_legitimate_domain']:
            score = max(0, score - 30)
        
        return min(100, max(0, score)), reasons
    
    def classify_url(self, url):
        """Classify URL as legitimate, suspicious, or inconclusive."""
        if not self.is_valid_url(url):
            return {
                'result': 'Invalid',
                'risk_score': 0,
                'reasons': ['Invalid URL format'],
                'features': {}
            }
        
        features = self.extract_features(url)
        risk_score, reasons = self.calculate_risk_score(features)
        
        if risk_score >= 50:
            result = 'Suspicious'
        elif risk_score >= 25:
            result = 'Suspicious'
        elif risk_score >= 10:
            result = 'Suspicious'
        else:
            result = 'Likely Legitimate'
        
        return {
            'result': result,
            'risk_score': risk_score,
            'reasons': reasons,
            'features': features
        }

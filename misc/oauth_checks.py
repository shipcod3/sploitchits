import requests
import re
import urllib.parse

def check_open_redirect(target_url, redirect_param='redirect_uri'):
    """Check if the OAuth implementation allows open redirects."""
    malicious_redirect = "https://evil.com"
    parsed_url = urllib.parse.urlparse(target_url)
    query_params = dict(urllib.parse.parse_qsl(parsed_url.query))
    
    if redirect_param in query_params:
        query_params[redirect_param] = malicious_redirect
        modified_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?" + urllib.parse.urlencode(query_params)
        
        response = requests.get(modified_url, allow_redirects=False)
        
        if response.status_code in [301, 302] and malicious_redirect in response.headers.get("Location", ""):
            print(f"⚠️ Open Redirect Found: {modified_url}")
        else:
            print("✅ No Open Redirect Found")
    else:
        print("⚠️ Redirect Parameter Not Found in URL")

def check_hardcoded_secrets(file_path):
    """Scan files for hardcoded OAuth client secrets."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        
        api_keys = re.findall(r'[0-9a-fA-F]{32,64}', content)
        
        if api_keys:
            print("⚠️ Possible Hardcoded Secrets Found:")
            for key in api_keys:
                print(f" - {key}")
        else:
            print("✅ No Hardcoded Secrets Found")

def check_token_leakage(target_url):
    """Check if tokens are exposed in URL parameters."""
    response = requests.get(target_url)
    
    token_patterns = [r'access_token=[A-Za-z0-9._-]+', r'id_token=[A-Za-z0-9._-]+']
    for pattern in token_patterns:
        if re.search(pattern, response.text):
            print(f"⚠️ Token Leakage Detected in {target_url}")
        else:
            print("✅ No Token Leakage Detected")

# Example Usage
if __name__ == "__main__":
    oauth_url = "https:/example.com/oauth?client_id=123&redirect_uri=https://example.com/callback"
    check_open_redirect(oauth_url)
    
    check_hardcoded_secrets("example_config.txt")
    
    check_token_leakage("https://example.com/profile")

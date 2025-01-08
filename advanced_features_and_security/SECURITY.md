# Security Measures Implemented

## HTTPS Configuration
- Enforced HTTPS by setting `SECURE_SSL_REDIRECT = True` in `settings.py`.
- Configured HSTS with `SECURE_HSTS_SECONDS = 31536000`, `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`, and `SECURE_HSTS_PRELOAD = True`.

## Secure Cookies
- Enabled `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` to ensure cookies are only sent over HTTPS.

## HTTP Security Headers
- Added `X_FRAME_OPTIONS = "DENY"` to prevent clickjacking.
- Enabled `SECURE_CONTENT_TYPE_NOSNIFF` to prevent MIME-sniffing.
- Enabled `SECURE_BROWSER_XSS_FILTER` for browser XSS filtering.

## Deployment
- Configured SSL/TLS certificates using Let's Encrypt and updated the web server (Nginx/Apache) for HTTPS.

## Testing
- Tested application using SSL Labs to verify HTTPS implementation.
- Conducted manual tests to ensure secure redirections and proper header responses.

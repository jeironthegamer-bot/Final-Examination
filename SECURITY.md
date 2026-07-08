# SECURITY REPORT

## Dependency Pinning

The project uses dependency pinning to ensure consistent and reproducible builds. The following third-party packages are required:

| Package | Version | Purpose |
|---------|---------|---------|
| PyJWT | 2.13.0 | JSON Web Token generation and validation |
| bcrypt | 5.0.0 | Secure password hashing |
| python-dotenv | 1.2.2 | Environment variable management |

---

## Mock Vulnerability Scan

A simulated dependency security review identified the following potential concerns.

| Component | Potential Risk | Mitigation |
|-----------|----------------|------------|
| Hardcoded Secret Key | The `.env` secret could be exposed if committed to version control. | `.env` is excluded using `.gitignore`. |
| JWT Tokens | Token theft could allow unauthorized access. | Tokens should use expiration times and HTTPS during transmission. |
| Password Storage | Plain-text passwords are insecure. | Passwords are verified using bcrypt hashing. |
| Dependency Versions | Floating package versions may introduce breaking changes. | Exact dependency versions are pinned in `requirements.txt`. |

---

## Security Recommendations

- Store secrets in environment variables.
- Never commit `.env` files.
- Rotate secret keys periodically.
- Use HTTPS when transmitting JWT tokens.
- Apply regular dependency updates after compatibility testing.
- Monitor dependencies for published security advisories.

---

## Authentication

Authentication is implemented using JSON Web Tokens (JWT). User passwords are verified using bcrypt before a signed JWT is issued. The generated token can later be validated by protected services without transmitting user credentials again.
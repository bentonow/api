# Bento OpenAPI

This repository publishes the OpenAPI 3.0 spec for Bento's public HTTP API.

- Spec: `bento-api.yaml`
- Guides: [docs.bentonow.com](https://docs.bentonow.com/)
- API: [app.bentonow.com/api/v1/](https://app.bentonow.com/api/v1/)

Authenticate with HTTP Basic. Use your publishable key as the username and your secret key as the password.

Check that every public operation in `scripts/expected-endpoints.txt` is present in the spec:

```
python3 scripts/check-openapi-coverage.py
```

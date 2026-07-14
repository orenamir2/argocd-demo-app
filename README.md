# argocd-demo-app

Tiny web application for testing Argo CD deployments and rollbacks.

`GET /` returns the application contract as JSON when requested with an
`Accept: application/json` header:

```json
{
  "application": "argocd-demo",
  "version": "1.0.0",
  "environment": "dev"
}
```

Opening `/` in a browser renders a version-colored status page:

- `APP_VERSION=1.0.0`: blue page
- `APP_VERSION=2.0.0`: green page

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python app/main.py
```

Then open `http://localhost:8080`.

To test version `2.0.0`:

```bash
APP_VERSION=2.0.0 python app/main.py
```

## Docker

Build version `1.0.0`:

```bash
docker build --build-arg APP_VERSION=1.0.0 -t argocd-demo-app:1.0.0 .
docker run --rm -p 8080:8080 argocd-demo-app:1.0.0
```

Build version `2.0.0`:

```bash
docker build --build-arg APP_VERSION=2.0.0 -t argocd-demo-app:2.0.0 .
docker run --rm -p 8080:8080 argocd-demo-app:2.0.0
```

## Test

```bash
pip install -r requirements-dev.txt
pytest
```

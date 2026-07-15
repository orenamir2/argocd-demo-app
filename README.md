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

## Publish image

GitHub Actions builds and pushes `ghcr.io/orenamir2/argocd-demo` on pushes to `main`,
version tags, and manual workflow runs.

- Pushes to `main` publish `1.0.0` and `sha-<commit>`.
- Tags like `v2.0.0` publish `2.0.0` and `sha-<commit>`.
- Manual runs use the supplied `app_version` input.

The workflow uses GitHub's built-in `GITHUB_TOKEN` with `packages: write` permission.

## Test

```bash
pip install -r requirements-dev.txt
pytest
```

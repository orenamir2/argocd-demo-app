import os

from flask import Flask, jsonify, render_template_string, request


APPLICATION_NAME = "argocd-demo"
DEFAULT_VERSION = "1.0.0"
DEFAULT_ENVIRONMENT = "dev"

VERSION_COLORS = {
    "1.0.0": {
        "name": "blue",
        "background": "#0f62fe",
        "accent": "#d0e2ff",
    },
    "2.0.0": {
        "name": "green",
        "background": "#198038",
        "accent": "#defbe6",
    },
}

PAGE_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ application }} {{ version }}</title>
    <style>
      :root {
        color-scheme: light;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      body {
        min-height: 100vh;
        margin: 0;
        display: grid;
        place-items: center;
        background: {{ background }};
        color: white;
      }

      main {
        width: min(520px, calc(100vw - 40px));
      }

      h1 {
        margin: 0 0 16px;
        font-size: clamp(2.5rem, 8vw, 5rem);
        line-height: 1;
        letter-spacing: 0;
      }

      dl {
        display: grid;
        grid-template-columns: max-content 1fr;
        gap: 12px 18px;
        margin: 0;
        padding: 24px;
        border: 1px solid rgb(255 255 255 / 0.28);
        border-radius: 8px;
        background: rgb(255 255 255 / 0.14);
        box-shadow: 0 24px 80px rgb(0 0 0 / 0.22);
      }

      dt {
        color: {{ accent }};
        font-weight: 700;
      }

      dd {
        margin: 0;
        overflow-wrap: anywhere;
      }
    </style>
  </head>
  <body>
    <main aria-label="Application status">
      <h1>{{ color_name }}</h1>
      <dl>
        <dt>application</dt>
        <dd>{{ application }}</dd>
        <dt>version</dt>
        <dd>{{ version }}</dd>
        <dt>environment</dt>
        <dd>{{ environment }}</dd>
      </dl>
    </main>
  </body>
</html>
"""


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        payload = {
            "application": APPLICATION_NAME,
            "version": os.getenv("APP_VERSION", DEFAULT_VERSION),
            "environment": os.getenv("APP_ENVIRONMENT", DEFAULT_ENVIRONMENT),
        }

        if request.accept_mimetypes.best == "application/json":
            return jsonify(payload)

        color = VERSION_COLORS.get(payload["version"], VERSION_COLORS[DEFAULT_VERSION])
        return render_template_string(
            PAGE_TEMPLATE,
            **payload,
            background=color["background"],
            accent=color["accent"],
            color_name=color["name"],
        )

    @app.get("/healthz")
    def healthz():
        return {"status": "ok"}

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))

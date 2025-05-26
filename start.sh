# #!/bin/bash
gunicorn multimedia_webapp.wsgi --bind 0.0.0.0:$PORT
chmod +x start.sh

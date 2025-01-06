from flask import Flask
from flask_cors import CORS
from routes.tasks import tasks_bp
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Registrar las tareas blueprint
app.register_blueprint(tasks_bp, url_prefix='/api/tasks')

# Server configuration
PORT = int(os.getenv("PORT", 5000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
    
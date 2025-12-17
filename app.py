from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# App Config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

db = SQLAlchemy(app)

# --- MODELS (Paste the models code here from Phase-6) ---
# (সংক্ষিপ্ততার জন্য আমি মডেল কোডটি এখানে রিপিট করছি না, 
# আপনি Phase-6 এর পুরো মডেল কোডটি এখানে বসাবেন)
# *নোট: মডেল কোডের শেষে db.create_all() কল করতে হবে*

# --- ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

# (এখানে Phase-6 এর বাকি API Route গুলো বসাতে হবে)
# Register, Login, Verify API routes...

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Auto create tables
    app.run(debug=False)

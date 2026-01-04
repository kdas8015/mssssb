from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Required for session/flash messages

# --- Data Handling (Simulated Database) ---
# In a real app, use SQLite or PostgreSQL
attendance_log = []

# --- Routes ---

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/in-memory')
def memory():
    founder = {
        "name": "John Doe",
        "years": "1980 - 2023",
        "bio": "A visionary leader who laid the foundation of our success. His legacy lives on in every innovation we create."
    }
    return render_template('memory.html', founder=founder)

@app.route('/team')
def team():
    executives = [
        {"name": "Alice Smith", "role": "CEO", "img": "https://via.placeholder.com/150"},
        {"name": "Bob Jones", "role": "CTO", "img": "https://via.placeholder.com/150"}
    ]
    staff = [
        {"name": "Charlie", "role": "Developer"},
        {"name": "Dana", "role": "Designer"},
        {"name": "Evan", "role": "Marketing"}
    ]
    return render_template('team.html', executives=executives, staff=staff)

@app.route('/services')
def services():
    services_list = [
        {"title": "Web Development", "desc": "Full-stack solutions."},
        {"title": "Digital Marketing", "desc": "SEO and Social Media growth."},
        {"title": "Consulting", "desc": "Business strategy and tech advisory."}
    ]
    return render_template('services.html', services=services_list)

@app.route('/payment')
def payment():
    # Replace with your actual UPI ID
    upi_id = "kdas8015@upi" 
    return render_template('payment.html', upi_id=upi_id)

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        name = request.form.get('name')
        status = request.form.get('status')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        attendance_log.append({"name": name, "status": status, "time": time})
        flash(f"Attendance marked for {name}!", "success")
        return redirect(url_for('attendance'))
    
    return render_template('attendance.html', logs=attendance_log)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

if __name__ == '__main__':
    app.run(debug=True)
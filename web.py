# web.py
from flask import Flask, render_template, request, redirect, url_for
from core import Journal

app = Flask(__name__)
journal = Journal()
journal.load_from_file('journal.json')  # Load entries from file at startup

@app.route('/')
def index():
    entries = journal.get_all_entries()
    return render_template('index.html', entries=entries)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    title = request.form.get('title')
    content = request.form.get('content')
    journal.add_entry(title, content)
    journal.save_to_file('journal.json')  # Save entries after adding a new one
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
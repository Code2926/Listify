from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    name = request.form.get('name')
    category = request.form.get('category')
    if name and category:
        tasks.append({'name': name, 'category': category, 'status': 'pending'})
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['status'] = 'completed'
    return redirect(url_for('index'))

@app.route('/remove_task/<int:task_id>', methods=['POST'])
def remove_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

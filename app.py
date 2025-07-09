from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    data = request.form.to_dict()
    return render_template('resume_template.html', data=data, preview=True)

if __name__ == '__main__':
    app.run(debug=True)

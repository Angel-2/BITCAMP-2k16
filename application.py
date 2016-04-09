from flask import Flask, render_template, url_for

app = Flask(__name__)

ROOT_TEMPLATE = 'root.html'

@app.route('/')
def redirect_root():
    return render_template(ROOT_TEMPLATE)

if __name__ == '__main__':
    app.run()

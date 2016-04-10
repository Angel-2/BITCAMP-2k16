from driver import get_total_scan_score
from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap


def create_app():
	app = Flask(__name__)
	Bootstrap(app)
	return app

app = create_app()
ROOT_TEMPLATE = 'root.html'
LOAD_TEMPLATE = 'load.html'
SCAN_TEMPLATE = 'scan.html'

@app.route('/')
def redirect_root():
    return render_template(ROOT_TEMPLATE)

@app.route('/load')
def redirect_load():
    return render_template(LOAD_TEMPLATE)

@app.route('/scan',methods=["POST"])
def redirect_scan():
    total = get_total_scan_score()
    return render_template(SCAN_TEMPLATE, total=total, network=request.form["network"], password_field=request.form["password_field"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

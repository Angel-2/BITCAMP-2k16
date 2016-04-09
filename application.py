from driver import get_total_scan_score

from flask import Flask, render_template, url_for

app = Flask(__name__)
app.debug = True
ROOT_TEMPLATE = 'root.html'
SCAN_TEMPLATE = 'scan.html'

@app.route('/')
def redirect_root():
    return render_template(ROOT_TEMPLATE)

@app.route('/scan')
def redirect_scan():
    total = get_total_scan_score()
    return render_template(SCAN_TEMPLATE, total = total)

if __name__ == '__main__':
    app.run()

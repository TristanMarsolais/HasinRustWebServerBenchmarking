from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/small')
def small():
    return render_template('./small/index.html')

@app.route('/large')
def large():
    return render_template('./large/index.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8081))
    app.run(debug=True, host='0.0.0.0', port=port)
# Web Server using Flask (http://flask.pocoo.org/)
#
# Run in background:
#  python ./server/server.py &
#
# Run in background with no output:
#  nohup python ./server/server.py > /dev/null 2>&1 &
#
# View on actual server at http://localhost:5000/
# View on local network using device's local IP, e.g. http://192.168.0.16:5000/
# To view on Internet, the Local Area Network should have Port Forwarding set up

from flask import Flask, Response, render_template
import csv
import json

# Create new Flask app
app = Flask(__name__)

# Define route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Define route for raw data
@app.route('/data.json')
def data():
    data = ''

    # Open the CSV
    fp = open('./data/data.csv', 'rU')

    # Parse the CSV into JSON
    reader = csv.DictReader(fp)
    data = json.dumps([row for row in reader], indent=2)

    # Return the data with an HTTP Content-Type of "application/json"
    return Response(data, mimetype='application/json')

# Run app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

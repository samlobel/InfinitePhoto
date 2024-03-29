import sys
from flask import Flask, render_template, request
app = Flask(__name__)


"""
Where our temporary server will live.
"""

PORT = None
if len(sys.argv) == 1:
  HOST='127.0.0.1'
  PORT=5000
else:
  HOST='0.0.0.0'
  PORT=int(sys.argv[1])
  
@app.route("/")
def main():
  return render_template('main.html')

if __name__ == "__main__":
  app.run(host=HOST, port=PORT)


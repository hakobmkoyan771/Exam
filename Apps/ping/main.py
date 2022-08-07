#!/usr/bin/python3
from asyncore import write
from flask import Flask, redirect, request, render_template, url_for
from pythonping import ping
import os

server_ip = os.getenv('SERVER_IP_ADDRESS')

app = Flask(__name__)

@app.route("/success", methods=['GET'])
def success():
    return render_template('success.html')

@app.route("/fail", methods=['GET'])
def fail():
    return render_template('fail.html')

@app.route("/", methods=['GET', 'POST'])
def ping_to_server():
    if request.method == "POST":
        x = ping(str(server_ip), verbose=True)
        with open('./log.out', 'w') as file:
            file.write(str(x))

        with open('./log.out', 'r') as file:
            output = file.readline()

        if output.strip() == "Request timed out":
            return redirect(url_for('fail'))
        else:
            return redirect(url_for('success'))

    if request.method == "GET":
        return render_template('ping.html')

if __name__ == "__main__":
  app.run(debug=False, host="0.0.0.0", port=80)

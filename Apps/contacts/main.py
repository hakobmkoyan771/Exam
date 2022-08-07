#!/usr/bin/python3
from flask import Flask, redirect, request, render_template, url_for
import dbconnection as coredb
import attributes as attr

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def users_list():
    users = coredb.read_users()
    return attr.users_on_html(users)


@app.route("/success", methods=['GET', 'POST'])
def success():
    print(request.method)
    if request.method == "POST":
        print('ok')
        if request.form.get('main') != None:
            print('ok')
            return redirect(url_for('users_list'))
    return render_template('reg-success.html')

@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('name')
        surname = request.form.get('surname')
        
        main_page = request.form.get('main')
        
        check_mail = coredb.match_email(str(email))
        
        if main_page != None:
            return redirect(url_for('users_list'))

        if check_mail == None:
            coredb.register_user(email, name, surname)
            return redirect(url_for('success'))
            #return render_template('reg-success.html')
        else:
            return render_template('reg-fail.html')
    return render_template('registration.html')

if __name__ == "__main__":
  #parser = argparse.ArgumentParser(description='Pass MongoDB IP address')
  #parser.add_argument('--db-address', type=str, required=True, help='Address of MongoDB')
  #args = parser.parse_args()
  app.run(debug=False, host="0.0.0.0", port=80)


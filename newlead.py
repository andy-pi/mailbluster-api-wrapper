from flask import Flask, request, render_template
import re
import os
from mailbluster import Mailbluster

mailbluster_api_key = os.environ['MAILBLUSTER_API_KEY']
mailblusterclient = Mailbluster(mailbluster_api_key)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    Signup to mailbluster API
    '''
    if request.method == 'GET':
        return render_template('index.html')
    else: # POST METHOD
        lead_email = re.sub('[^a-zA-Z0-9-_@.]', '', request.form['email'])
        first_name = re.sub('[^a-zA-Z0-9-_ @.]', '', request.form['firstname'])
        last_name = re.sub('[^a-zA-Z0-9-_@ .]', '', request.form['lastname'])
        response = mailblusterclient.create_lead(email=lead_email,firstName=first_name,lastName=last_name)
        if response['message'] =='Lead created':
            status = 'You have been succesfully subscribed'
        else:
            status = 'An error occured'
        return render_template('index.html', status=status)

if __name__ == '__main__':
    app.run()
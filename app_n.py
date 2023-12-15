from distutils.log import debug
from fileinput import filename
import pandas as pd
from flask import *
import os
from werkzeug.utils import secure_filename
import csv
from Cleaner1 import temp_files

UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')

current_step = 1

List1 = ['FirstClass', 'BusinessClass', 'PremiumEconomyClass', 'EconomyClass', 'DEAF', 'WCHR', 'BLND', 'NRSA',
         'NRPS', 'Platinum', 'Gold', 'Silver', 'S65', 'ADT', 'CHD', 'INF', 'INS', 'UNN', 'GN', 'PAX']

default_values = [1000, 800, 600, 500, 200, 200, 200, 750,
                  1000, 2000, 1750, 1500, 500, 0, 500, 750, 1000, 1000, 500, 50]

default_checked = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]

ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'This is your secret key to utilize session in Flask'


# def allowed_file(filename):
# return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# def save_file_and_session(file, session_key):
#     data_filename = f'{session_key}.csv'
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
#     session[f'uploaded_data_file_path_{session_key}'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)


@app.route('/', methods=['GET', 'POST'])
def uploadFile():
    global current_step
    if request.method == 'POST':
        # current_step = int(request.form.get('current_step', 1))
        # current_step = 1
        # print(current_step)
        if current_step == 1:
            current_step += 1
            f1 = request.files.get('f')
            if f1:
                # data_filename1 = 'SCH.csv'
                f1.save(os.path.join(app.config['UPLOAD_FOLDER'], 'SCH.csv'))
                return render_template('index_new.html', rule_list=List1, default_values=default_values, default_checked=default_checked, current_step=current_step, file='PNR Passenger')
        elif current_step == 2:
            current_step += 1
            f2 = request.files.get('f')
            if f2:
                # data_filename2 = 'PNRP.csv'
                f2.save(os.path.join(app.config['UPLOAD_FOLDER'], 'PNRP.csv'))
                return render_template('index_new.html', rule_list=List1, default_values=default_values, default_checked=default_checked, current_step=current_step, file='PNR Booking')
        elif current_step == 3:
            current_step += 1
            f3 = request.files.get('f')
            if f3:
                # data_filename3 = 'PNRB.csv'
                f3.save(os.path.join(app.config['UPLOAD_FOLDER'], 'PNRB.csv'))
                return render_template('index_new.html', rule_list=List1, default_values=default_values, default_checked=default_checked, current_step=current_step, file='Inventory')
        elif current_step == 4:
            current_step += 1
            f4 = request.files.get('f')
            if f4:
                # data_filename4 = 'INV.csv'
                f4.save(os.path.join(app.config['UPLOAD_FOLDER'], 'INV.csv'))
            return render_template('index_wtver.html')

        # if current_step == 5:
        #     return render_template('index_wtver.html')

        # If none of the above conditions match, show the current step
        return render_template('index_new.html', rule_list=List1, default_values=default_values,
                               default_checked=default_checked, current_step=current_step)

    return render_template('index_new.html', rule_list=List1, default_values=default_values,                        default_checked=default_checked, current_step=1, file='Flight Schedule')


if __name__ == '__main__':
    app.run(debug=True)

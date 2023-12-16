from distutils.log import debug
from fileinput import filename
import pandas as pd
from flask import *
import os
from werkzeug.utils import secure_filename
import csv
from Cleaner1 import temp_files
from Ash import main1
from Converter import main2
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


@app.route('/', methods=['GET', 'POST'])
def uploadFile():
    global current_step
    global flights_cancelled
    global Max_layover_time, Min_layover_time, Max_departure_delay, downline
    if request.method == 'POST':
        # current_step = int(request.form.get('current_step', 1))
        # current_step = 1
        # print(current_step)

        if current_step == 1:
            current_step += 1
            f1 = request.files.get('f')
            if f1:
                f1.save(os.path.join(app.config['UPLOAD_FOLDER'], 'PNRP.csv'))
                return render_template('index_new.html', rule_list=List1, default_values=default_values, default_checked=default_checked, current_step=current_step, file='PNR Booking Data')

        elif current_step == 2:
            current_step += 1
            f2 = request.files.get('f')
            if f2:
                f2.save(os.path.join(app.config['UPLOAD_FOLDER'], 'PNRB.csv'))
                return render_template('index_new.html', rule_list=List1, default_values=default_values, default_checked=default_checked, current_step=current_step, file='Flight Schedule')

        elif current_step == 3:
            current_step += 1
            f3 = request.files.get('f')
            if f3:
                f3.save(os.path.join(app.config['UPLOAD_FOLDER'], 'SCH.csv'))
                return render_template('index_new.html', rule_list=List1, default_values=default_values, default_checked=default_checked, current_step=current_step, file='Inventory')

        elif current_step == 4:
            current_step += 1
            f4 = request.files.get('f')
            if f4:
                f4.save(os.path.join(app.config['UPLOAD_FOLDER'], 'INV.csv'))
            return render_template('index_new_flights_cancelled.html', rule_list=List1, default_values=default_values, default_checked=default_checked, current_step=current_step)

        elif current_step == 5:
            current_step += 1
            f5 = request.form['f']
            if f5:
                flights_cancelled = f5.split(', ')
            return render_template('index_new_RuleEngine.html', rule_list=List1, default_values=default_values, default_checked=default_checked, current_step=current_step)


        if current_step == 6:
            current_step += 1
            rules = [['Condition', 'Score', 'FK']]
            for i in range(1, 21):
                rule_weight = int(request.form[f"rule{i}_weight"])
                rule_bool = request.form.get(f"rule{i}_bool") is not None
                rules.append([List1[i-1], rule_weight, rule_bool])

            with open("staticFiles\\uploads\\RULES.csv", 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(rules)

            return render_template('index_new_rule_engine_2.html', rule_list=List1, default_values=default_values, default_checked=default_checked, current_step=current_step)
            
        elif current_step == 7:
            current_step += 1
            downline = request.form['Downline']
            Max_departure_delay = request.form['Max-Departure-Delay']
            Max_layover_time = request.form['Max-Layover-Time']
            Min_layover_time = request.form['Min-Layover-Time']

            temp_files()

            main1(flights_cancelled)

            main2(flights_cancelled)

            return render_template('index_wtver.html')

        # If none of the above conditions match, show the current step
        return render_template('index_new.html', rule_list=List1, default_values=default_values, default_checked=default_checked, current_step=current_step)

    return render_template('index_new.html', rule_list=List1, default_values=default_values, default_checked=default_checked, current_step=1, file='PNR Passenger Data')


if __name__ == '__main__':
    app.run(debug=True)

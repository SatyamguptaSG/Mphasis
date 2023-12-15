from flask import Flask, render_template, request, redirect, url_for, session
import os
import csv

UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')

List1 = ['FirstClass', 'BusinessClass', 'PremiumEconomyClass', 'EconomyClass', 'DEAF', 'WCHR', 'BLND', 'NRSA',
         'NRPS', 'Platinum', 'Gold', 'Silver', 'S65', 'ADT', 'CHD', 'INF', 'INS', 'UNN', 'GN', 'PAX']

default_values = [1000, 800, 600, 500, 200, 200, 200, 750, 1000, 2000, 1750, 1500, 500, 0, 500, 750, 1000, 1000, 500, 50]

default_checked = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]

ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'This is your secret key to utilize session in Flask'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file_and_session(file, session_key):
    data_filename = f'{session_key}.csv'
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
    session[f'uploaded_data_file_path_{session_key}'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)


@app.route('/', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        current_step = int(request.form.get('current_step', 1))

        if current_step == 1:
            f1 = request.files.get('flightSchedule')
            if f1 and allowed_file(f1.filename):
                save_file_and_session(f1, 'SCH')
                return redirect(url_for('uploadFile', current_step=2))
        elif current_step == 2:
            f2 = request.files.get('PNRP')
            if f2 and allowed_file(f2.filename):
                save_file_and_session(f2, 'PNRP')
                return redirect(url_for('uploadFile', current_step=3))
        elif current_step == 3:
            f3 = request.files.get('PNRB')
            if f3 and allowed_file(f3.filename):
                save_file_and_session(f3, 'PNRB')
                return redirect(url_for('uploadFile', current_step=4))
        elif current_step == 4:
            f4 = request.files.get('INV')
            if f4 and allowed_file(f4.filename):
                save_file_and_session(f4, 'INV')
                return redirect(url_for('uploadFile', current_step=5))

        # If none of the above conditions match, show the current step
        return render_template('index_new.html', rule_list=List1, default_values=default_values,
                               default_checked=default_checked, current_step=current_step)

    return render_template('index_new.html', rule_list=List1, default_values=default_values,
                           default_checked=default_checked, current_step=1)


if __name__ == '__main__':
    app.run(debug=True)










# from flask import Flask, render_template, request, session
# import os
# import csv
# from Cleaner import temp_files  # Assuming this is a valid import

# UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')

# List1 = ['FirstClass', 'BusinessClass', 'PremiumEconomyClass', 'EconomyClass', 'DEAF', 'WCHR', 'BLND', 'NRSA', 'NRPS',
#          'Platinum', 'Gold', 'Silver', 'S65', 'ADT', 'CHD', 'INF', 'INS', 'UNN', 'GN', 'PAX']

# default_values = [1000, 800, 600, 500, 200, 200, 200, 750, 1000, 2000, 1750, 1500, 500, 0, 500, 750, 1000, 1000, 500, 50]

# default_checked = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]

# # Define allowed files
# ALLOWED_EXTENSIONS = {'csv'}

# app = Flask(__name__)

# # Configure upload file path flask
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# app.secret_key = 'This is your secret key to utilize session in Flask'


# def save_file_and_update_session(file_key, session_key):
#     file = request.files.get(file_key)
#     data_filename = f'{file_key.upper()}.csv'
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
#     session[session_key] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)


# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     current_step = int(request.form.get('current_step', 1)) if request.method == 'POST' else 1

#     if request.method == 'POST':
#         if current_step == 1:
#             save_file_and_update_session('flightSchedule', 'uploaded_data_file_path1')
#         elif current_step == 2:
#             save_file_and_update_session('PNRP', 'uploaded_data_file_path2')
#         elif current_step == 3:
#             save_file_and_update_session('PNRB', 'uploaded_data_file_path3')
#         elif current_step == 4:
#             save_file_and_update_session('INV', 'uploaded_data_file_path4')
#             rules = [['Condition', 'Score', 'FK']]
#             for i in range(1, 21):
#                 rule_weight = int(request.form[f"rule{i}_weight"])
#                 rule_bool = request.form.get(f"rule{i}_bool") is not None
#                 rules.append([List1[i - 1], rule_weight, rule_bool])

#             with open("staticFiles\\uploads\\RULES.csv", 'w', newline='') as f:
#                 writer = csv.writer(f)
#                 writer.writerows(rules)

#             temp_files()

#         if current_step < 5:
#             current_step += 1

#     return render_template('index_new.html', rule_list=List1, default_values=default_values,
#                            default_checked=default_checked, current_step=current_step)


# if __name__ == '__main__':
#     app.run(debug=True)










# from distutils.log import debug
# from fileinput import filename
# import pandas as pd
# from flask import *
# import os
# from werkzeug.utils import secure_filename
# import csv
# from Cleaner import temp_files

# UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')

# List1 = ['FirstClass','BusinessClass','PremiumEconomyClass','EconomyClass','DEAF','WCHR','BLND','NRSA','NRPS','Platinum','Gold','Silver','S65','ADT','CHD','INF','INS','UNN','GN','PAX']

# default_values = [1000,800,600,500,200,200,200,750,1000,2000,1750,1500,500,0,500,750,1000,1000,500,50]

# default_checked = [1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0]

# # Define allowed files
# ALLOWED_EXTENSIONS = {'csv'}

# app = Flask(__name__)

# # Configure upload file path flask
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# app.secret_key = 'This is your secret key to utilize session in Flask'


# @app.route('/', methods=['GET', 'POST'])
# def uploadFile():
#     if request.method == 'POST':
#         # upload file flask

#         f1 = request.files.get('flightSchedule')
#         # Extracting uploaded file name
#         data_filename1 = 'SCH.csv'
#         f1.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename1))
#         session['uploaded_data_file_path1'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename1)

#         f2 = request.files.get('PNRP')
#         # Extracting uploaded file name
#         data_filename2 = 'PNRP.csv'
#         f2.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename2))
#         session['uploaded_data_file_path2'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename2)

#         f3 = request.files.get('PNRB')
#         # Extracting uploaded file name
#         data_filename3 = 'PNRB.csv'
#         f3.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename3))
#         session['uploaded_data_file_path3'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename3)

#         f4 = request.files.get('INV')
#         # Extracting uploaded file name
#         data_filename4 = 'INV.csv'
#         f4.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename4))
#         session['uploaded_data_file_path4'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename4)
    
#         rules = [['Condition','Score','FK']]
#         for i in range(1, 21):
#             rule_weight = int(request.form[f"rule{i}_weight"])
#             rule_bool = request.form.get(f"rule{i}_bool") is not None
#             rules.append([List1[i-1],rule_weight, rule_bool])

#         with open("staticFiles\\uploads\\RULES.csv", 'w', newline='') as f:
#             writer = csv.writer(f)
#             writer.writerows(rules)

#         temp_files()
#         return render_template('index_new.html', rule_list=List1, default_values=default_values, default_checked=default_checked)
#     return render_template("index_new.html", rule_list=List1, default_values=default_values, default_checked=default_checked)
# # def soft_install():


# # @app.route('/show_data')
# # def showData():
# #     # Uploaded File Path
# #     data_file_path = session.get('uploaded_data_file_path', None)
# #     # read csv
# #     uploaded_df = pd.read_csv(data_file_path, encoding= 'unicode_escape')
# #     # Converting to html Table
# #     uploaded_df_html = uploaded_df.to_html()
# #     return render_template('show_csv_data.html',data_var=uploaded_df_html)


# if __name__ == '__main__':
#     app.run(debug=True)

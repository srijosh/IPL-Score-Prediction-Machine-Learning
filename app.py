from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'ipl.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            input = input + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            input = input + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            input = input + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            input = input + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            input = input + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            input = input + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            input = input + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            input = input + [0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            input = input + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            input = input + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            input = input + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            input = input + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            input = input + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            input = input + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            input = input + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            input = input + [0,0,0,0,0,0,0,1]
            
            
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
        input = input + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
        result = np.array([input])
        my_prediction = int(regressor.predict(result)[0])
              
        return render_template('result.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)



if __name__ == '__main__':
	app.run(debug=True)
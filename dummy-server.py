from flask import Flask, jsonify  # Flask is imported for building the API; jsonify is used for JSON responses
import pandas as pd  # Importing pandas to handle CSV file operations and data manipulation

app = Flask(__name__)  # Creating an instance of the Flask app
data = pd.read_csv('weatherHistory.csv')  # Reading the CSV file named 'weatherHistory.csv' into a DataFrame called 'data'
current_index = 0  # Setting an initial index variable to track the row number

@app.route('/')  # Setting the route to the root endpoint ('/')
def get_next_row():  # Defining the function that will run when the root URL is accessed
    global current_index  # Declaring the use of the global variable 'current_index' within this function
    if current_index < len(data):  # Condition to check if the index is within the bounds of the data
        row = data.iloc[current_index].to_dict()  # Fetch the current row, convert it to a dictionary
        current_index += 1  # Increment the index for the next request to return the following row
        return jsonify(row)  # Return the row as JSON to the client
    else:
        return jsonify(error='No more data available'), 404  # If no data is left, return an error message with a 404 status code

if __name__ == '__main__':  # This condition checks if this file is being executed directly
    app.run(debug=True)  # Run the app with debug mode enabled, which provides error logs in the console

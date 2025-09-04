from flask import Flask, jsonify, request, Response
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import io

# Load dataset
df = pd.read_csv('Sample.csv', parse_dates=['date'])
print(df)

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome to the Simple Flask API! "

# Route to show plot
@app.route("/show")
def show():
    # Create line plot
    plt.figure()
    plt.plot(df['date'], df['sales'], label='Sales')
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.legend(loc="upper left")

    # Save plot to in-memory buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)

    return Response(buf.getvalue(), mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)

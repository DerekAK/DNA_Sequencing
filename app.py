from flask import Flask, render_template, request, jsonify
import os
from RunSpecifiedAlgorithm import runAlgorithm
from algorithms import editDistance

app = Flask(__name__)

# Define directories for the dropdown menus
DNA_SEQUENCES_DIR = 'dnaSequences'
DNA_SEQUENCE_TO_CHECK_DIR = 'dnaQueries'

@app.route('/')
def index():
    # Get files in each directory for dropdowns
    dna_sequences = os.listdir(DNA_SEQUENCES_DIR)
    dna_sequence_to_check = os.listdir(DNA_SEQUENCE_TO_CHECK_DIR)
    return render_template('index.html', dna_sequences=dna_sequences, dna_sequence_to_check=dna_sequence_to_check)

@app.route('/run_algorithm', methods=['POST'])
def run_algorithm(): # handles POST requests from app.py when app.py sends over json data of the algorithm chosen and the two dna files
    data = request.get_json()
    algorithm = data['algorithm']
    dna_seq_file = data['dna_seq_file']
    dna_check_file = data['dna_check_file']

    # Here you would load and run the chosen algorithm
    # For demonstration, we simulate output


    bestSeq, bestSim, totalTime = runAlgorithm(dna_check_file, dna_seq_file, algorithm)

    output = f"Algorithm: {algorithm}\n\nSequences file: {dna_seq_file}\n\nQuery file: {dna_check_file}\n\nBest Sequence: {bestSeq}\nSim score: {bestSim}\n\nTotal time: {totalTime} seconds"

    return jsonify({"output": output})

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host = '0.0.0.0', port=5001, debug=True)
    #app.run(port=5001, debug=True)


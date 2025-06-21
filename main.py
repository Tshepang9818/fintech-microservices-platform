# app/main.py
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging for compliance (logs to a file)
logging.basicConfig(filename='compliance.log', level=logging.INFO)

@app.route('/transaction', methods=['POST'])
def log_transaction():
    data = request.get_json()
    # Log transaction data (simulate compliance logging)
    logging.info(f"Transaction logged: {data}")
    return jsonify({"message": "Transaction logged successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

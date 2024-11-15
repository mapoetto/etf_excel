import justetf_scraping
from io import StringIO





from flask import Flask, request, jsonify

app = Flask(__name__)

# Dati in memoria come esempio
data_ret = {}

# Endpoint per gestire le richieste GET
@app.route('/etf/<string:isin>', methods=['GET'])
def get_data(isin):

    csv_buffer = StringIO()
    
    df = justetf_scraping.load_chart(isin)
    
    df = df[["quote"]] # lascio solo la colonna quote
    
    df.to_csv(csv_buffer, index=True)
    
    csv_string = csv_buffer.getvalue()
    
    data_ret["result"] = csv_string
    
    return jsonify(csv_string), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)




#df = justetf_scraping.load_chart("IE00B0M62Q58")

#print(str(df))
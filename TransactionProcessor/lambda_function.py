import json
from constants.constant import db_host,db_user,db_pass,db_name,db_charset
from utility.database import db

print("Loading Function: TransactionProcessor")

def lambda_handler(event, context):
    db_obj = db(db_host,db_user,db_pass,db_name,db_charset)
    db_conn = db_obj.connect()
    
    cur = db_conn.cursor()
    cur.execute(r'select uuid,id,scheme_id,is_internal from wcms.concept limit 1')
    output = cur.fetchall()
        
      
    # To close the connection
    #connection.close()
    ##Parse out query string parameters
    transaction_id = event['queryStringParameters']['id']
    transaction_type = event['queryStringParameters']['type']
    transaction_amount = event['queryStringParameters']['amount']

    log_dict = {
        'transaction_id' : transaction_id,
        'transaction_type': transaction_type,
        'transaction_amount': transaction_amount,
    }

    print(log_dict)

    ##Construct body of response object
    transactionResponse = {
        'transaction_id': transaction_id,
        'transaction_type': transaction_type,
        'transaction_amount': transaction_amount,
        'concept_id' : output,
        'message': 'response from AWS lambda'
    }

    ##Contruct http response object
    responseObject = {
        'statusCode' : 200,
        'headers' : {'Content-Type' : 'application/json'},
        'body' : json.dumps(transactionResponse,indent=4, sort_keys=True)
    }

    ##return response object
    return responseObject

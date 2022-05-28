from smart_open import smart_open

def readS3(bucket_s3_url):
    print("Reading csv from s3...")
    with smart_open(bucket_s3_url, 'rb') as s3_source:
        transaction_list = []
        date_list=[]
        credit_list = []
        debit_list = []
        index = 0 
        for line in s3_source:
            if(index == 0):
                print("Titles")
                index = 1
            else:
                temp_line = line.decode('utf8')
                temp_array_line = temp_line.split(',')
                # Mapping transaction into a dictonary
                transaction = float(temp_array_line[2])                
                transaction_list.append(transaction)
                debit_list.append(transaction) if transaction > 0 else credit_list.append(transaction)
                date_list.append(temp_array_line[1])

    accounts_transaction = {
        "transactions" : transaction_list,
        "debit_transactions" : debit_list,
        "credit_transactions" : credit_list,
        "dates" : date_list
    }
    print("accounts_transactions", accounts_transaction)
    return accounts_transaction
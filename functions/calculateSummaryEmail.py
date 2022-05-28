
from datetime import datetime
from statistics import median

def wordsFrequency(words_list):
    months = []    
    frequency = [words_list.count(word) for word in words_list]
    for indice, word in enumerate(words_list):
        month = {
            "name": word,
            "number_transactions" : frequency[indice]
        }   
        months.append(month)
    return months

def formatDate(dt_str):
    dt_obj = datetime.strptime(dt_str, '%m/%d').date()
    return dt_obj.strftime("%B")

def calculateSummary(account_transactions):
    print("Function calculateSummary")
    #Calculate Balance
    balance = sum(account_transactions["transactions"]) 
    #Calculate average credit card
    average_debit_amount = median(account_transactions["debit_transactions"])
    #Calculate average debit card
    average_credit_amount = median(account_transactions["credit_transactions"])
    #Number of transactions by month 
    month_list = list(map(formatDate, account_transactions["dates"]))
    number_transactions_by_month = wordsFrequency(month_list)

    summary = {
            "balance" : balance,
            "average_debit_amount" : average_debit_amount,
            "average_credit_amount" : average_credit_amount,
            "transactions_month" : number_transactions_by_month
    }

    return summary


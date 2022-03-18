import requests


def main():
    currency = get_target_currency()
    bitcoin = get_bitcoin_amount()
    converted = convert_bitcoin_to_target(bitcoin,
    currency)
    display_result(bitcoin,
    currency, converted)

def get_target_currency():
    #for this api it has to be predefined dollars, but this can be made into a user input later
    #dollars_exchange = data['bpi']['USD']['rate_float']
    while True:
        try:
            currency = input('Enter target currency code(either USD, GBP, or EUR): ')
            currency_list = ['EUR', 'GBP' , 'USD']
            if currency.upper() not in currency_list:
                raise ValueError('Enter target currency code(either USD, GBP, or EUR):  ')
            elif len(currency) == 0 :
                raise ValueError('Enter target currency code(either USD, GBP, or EUR): ')
            else:      
                return currency.upper()
        except:
            print('Enter target currency code(either USD, GBP, or EUR): ')
    
def get_bitcoin_amount():
        while True:
            try:
                bitcoin = float(input('Your bitcoin amount: '))
                if bitcoin <= 0:
                    raise ValueError('nothing to convert')
                else:
                    return bitcoin  
            except:
                print('Your bitcoin amount: ')

def convert_bitcoin_to_target(bitcoin,target_currency):
    exchange_rate = get_exchange_rate(target_currency)
    converted= convert(bitcoin, exchange_rate)
    return converted

def get_exchange_rate(currency):
    response = request_rates(currency)
    rate = extract_rate(response, currency)
    return rate 

def request_rates(currency):
    try: 
        params = {'base': 'USD', 'symbols': currency}
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        return requests.get(url, params=params).json()
    except Exception as e:
        print('Error processing the request. Try again later')


def extract_rate(rates, currency):
    return rates['bpi'][currency]['rate_float'] 


def convert(amount, exchange_rate):
    return amount * exchange_rate 

def display_result(bitcoin, currency, converted):
    """ Format and display the result """
    print(f'{bitcoin} is equal to {currency} {converted:.2f} for you')


if __name__ == '__main__':
    main()

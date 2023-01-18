from flask import Flask
app = Flask(__name__)

""" https://en.wikipedia.org/wiki/Payment_card_number """
issuing_network = {}

issuer_category = {
    '0': "ISO/TC 68 and other industry assignments",
    '1': "Airlines",
    '2': "Airlines, financial and other future industry assignments",
    '3': "Travel and entertainment",
    '4': "Banking and financial",
    '5': "Banking and financial",
    '6': "Merchandising and banking/financial",
    '7': "Petroleum and other future industry assignments",
    '8': "Healthcare, telecommunications and other future industry assignments",
    '9': "For assignment by national standards bodies",
}

@app.route('/cardnumber/validate/<string:card_number>')
def validate_cardnumber(card_number):
    if card_number.isnumeric():
        return {
            "card_number": card_number,
            "is_valid": is_valid_card_number(card_number),
            "issuer_category": get_issuer_category(card_number),
            "issuing_network": get_issuing_network(card_number),
        }
    else:
        return {
            "card_number": card_number,
            "result": False,
            "error": "Not a card number",
        }

@app.route('/cardnumber/generate/')
def generate_cardnumber():
    return {
        "card_number": "9792087730395886",
    }

def get_issuing_network(card_number):
    return "Other"

""" The first (leading) digit of the IIN identifies the major industry of the card issuer. """
def get_issuer_category(card_number):
    return issuer_category[card_number[0]]

""" https://en.wikipedia.org/wiki/Luhn_algorithm """
def is_valid_card_number(card_number):
    sum = 0
    parity = len(card_number) % 2
    i = 1
    for num in card_number:
        if i % 2 == parity:
            sum = sum + int(num)
        elif int(num) > 4:
            sum = sum + 2 * int(num) - 9
        else:
            sum = sum + 2 * int(num)
        i = i + 1

    return sum % 10 == 0


if __name__ == "__main__":
    app.run()

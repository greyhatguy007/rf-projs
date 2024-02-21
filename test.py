import re
from datetime import datetime, timedelta

def extract_transaction_details(input_line):
    # Define patterns to extract amount, date, recipient, and reason
    amount_pattern = r'(\d+)rs'
    date_pattern = r'\b(?:today|yesterday|\d+\s+days\s+ago)\b'
    to_pattern = r'to\s+(\w+)'
    reason_pattern = r'(\b\w+\b\s*)+$'

    # Extract amount
    amount_match = re.search(amount_pattern, input_line, re.IGNORECASE)
    amount = amount_match.group(1) if amount_match else None

    # Extract date
    date_match = re.search(date_pattern, input_line, re.IGNORECASE)
    if date_match:
        if date_match.group().lower() == 'today':
            transaction_date = datetime.now().strftime('%Y-%m-%d')
        elif date_match.group().lower() == 'yesterday':
            transaction_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        else:
            days_ago = int(re.search(r'\d+', date_match.group()).group())
            transaction_date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
    else:
        transaction_date = None

    # Extract recipient
    to_match = re.search(to_pattern, input_line, re.IGNORECASE)
    recipient = to_match.group(1) if to_match else None

    # Extract reason
    reason_match = re.search(reason_pattern, input_line, re.IGNORECASE)
    reason = reason_match.group() if reason_match else None

    return {
        'amount': amount,
        'date': transaction_date,
        'to': recipient,
        'reason': reason
    }

# Test the function with sample inputs
inputs = [
    "Today 100rs rent hdfc acc to kumar by gpay claimable",
    "3 days ago 1000rs bike repair  by cash to senthil not claimable",
    "Yesterday 10rs chat shop by card citi bank acc no claimable",
    "2 days ago 20000rs to revi for washing machine repair"
]

for input_line in inputs:
    details = extract_transaction_details(input_line)
    print("Amount:", details['amount'])
    print("Date:", details['date'])
    print("To:", details['to'])
    print("Description:", details['reason'])
    print()


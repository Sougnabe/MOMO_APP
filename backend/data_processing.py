import xml.etree.ElementTree as ET
import re
import logging
import json
from datetime import datetime
from database import create_database, insert_transaction, get_transactions as fetch_transactions

# Set up logging for general logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create a separate logger for unprocessed messages
unprocessed_logger = logging.getLogger('unprocessed')
unprocessed_logger.setLevel(logging.WARNING)
file_handler = logging.FileHandler('logs/unprocessed_messages.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
unprocessed_logger.addHandler(file_handler)

# Define transaction categories
TRANSACTION_CATEGORIES = {
    "received": "Incoming Money",
    "transferred": "Transfers to Mobile Numbers",
    "deposit": "Bank Deposits",
    "airtime": "Airtime Bill Payments",
    "cash power": "Cash Power Bill Payments",
    "third party": "Transactions Initiated by Third Parties",
    "withdrawn": "Withdrawals from Agents",
    "bank transfer": "Bank Transfers",
    "internet bundle": "Internet and Voice Bundle Purchases",
    "voice bundle": "Internet and Voice Bundle Purchases"
}

def parse_xml(file_path):
    """
    Parses an XML file containing SMS data and extracts transaction details.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        transactions = []
        skipped_messages = 0
        for sms in root.findall('sms'):
            body = sms.attrib.get('body')
            if body is None:
                skipped_messages += 1
                unprocessed_logger.warning(f"Skipping SMS: No 'body' attribute found.")
                continue
            # Skip OTP messages
            if "one-time password" in body.lower():
                skipped_messages += 1
                unprocessed_logger.warning(f"Skipping OTP message.")
                continue
            try:
                category, amount, fee, date = categorize_sms(body)
                transaction = {
                    'category': category,
                    'amount': amount,
                    'fee': fee,
                    'date': date,
                    'body': body
                }
                transactions.append(transaction)
                insert_transaction(transaction)  # Insert into the database
                update_json_from_db()  # Update JSON file
            except ValueError as ve:
                skipped_messages += 1
                unprocessed_logger.warning(f"Unprocessed message: {body}. Reason: {ve}")
            except Exception as e:
                skipped_messages += 1
                unprocessed_logger.error(f"Unexpected error processing SMS: {body}. Error: {e}")
        logging.info(f"Processed {len(transactions)} transactions. Skipped {skipped_messages} messages.")
    
    except ET.ParseError:
        unprocessed_logger.error("Error parsing XML file.")
    except FileNotFoundError:
        unprocessed_logger.error("File not found.")
    except Exception as e:
        unprocessed_logger.error(f"An unexpected error occurred: {e}")

def categorize_sms(body):
    """
    Categorizes an SMS message into predefined transaction types or marks it as 'Other'.
    """
    body_lower = body.lower().strip()  # This seems to be what you were trying to start with
    category = "Other"
    
    # Handle Bank Transfers first to prevent them from being caught by bundle conditions
    if "imbank.bank" in body_lower:
        category = "Bank Transfers"    

    # Handle Internet and Voice Bundle Purchases (excluding imbank.bank)
    elif any(keyword in body_lower for keyword in ["bundle", "bundles and packs", "data bundle", "internet bundle", "voice bundle", "mb", "gb", "mins", "sms", "mtn internet"]):
        category = "Internet and Voice Bundle Purchases"
    
    # Handle Airtime Bill Payments
    elif "to airtime with token" in body_lower:
        category = "Airtime Bill Payments"
    
    # Handle Cash Power Bill Payments
    elif "cash power with token" in body_lower:
        category = "Cash Power Bill Payments"
    
    # Handle Payments to Code Holders, excluding failed/unsuccessful transactions
    elif "payment of" in body_lower and "to" in body_lower and "completed" in body_lower:
        if "failed" not in body_lower and "unsuccessful" not in body_lower and "transaction failed" not in body_lower:
            if "airtime with token" not in body_lower and "mtn cash power with token" not in body_lower and "bundles and packs with token" not in body_lower:
                category = "Payments to Code Holders"
    
    # Handle Transactions Initiated by Third Parties
    elif "message from debit receiver" in body_lower or "ltd" in body_lower:
        category = "Transactions Initiated by Third Parties"
    
    # Handle Transfers to Mobile Numbers
    elif "transferred to" in body_lower or "sent to" in body_lower or "transfer to" in body_lower or "onafriq mauritius" in body_lower:
        category = "Transfers to Mobile Numbers"
 
    # Match keywords to categories
    else:
        for keyword, cat in TRANSACTION_CATEGORIES.items():
            if re.search(rf'\b{keyword}\b', body_lower):
                category = cat
                break
    
    # Extract amount
    amount_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) rwf', body_lower)
    if not amount_match:
        raise ValueError("Amount not found")
    amount = int(amount_match.group(1).replace(",", ""))
    
    # Extract fee
    fee_match = re.search(r'(fee|charges)[: ]*(\d{1,3}(?:,\d{3})*|\d+) rwf', body_lower)
    fee = int(fee_match.group(2).replace(",", "")) if fee_match else 0
    
    # Extract date
    date_match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', body_lower)
    if not date_match:
        date_match = re.search(r'\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2}', body_lower)
        if date_match:
            date = datetime.strptime(date_match.group(), "%d/%m/%Y, %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
        else:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        date = date_match.group()
    
    return category, amount, fee, date

def get_all_transactions():
    """
    Fetches all transactions from the database.
    """
    return fetch_transactions()

def save_transactions_to_json(transactions):
    """
    Saves processed transactions to a JSON file.
    """
    with open("frontend/transactions.json", "w", encoding="utf-8") as json_file:
        json.dump(transactions, json_file, indent=4, ensure_ascii=False)
    logging.info("Transactions saved to frontend/transactions.json")

def update_json_from_db():
    """
    Fetch transactions from the database and update the JSON file.
    """
    transactions = get_all_transactions()
    save_transactions_to_json(transactions)

if __name__ == "__main__":
    create_database()
    parse_xml("sms_data.xml")

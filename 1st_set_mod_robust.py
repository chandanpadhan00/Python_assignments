import csv
import io
import chardet
import re

def clean_attribute_value(text):
    # First, remove all non-alphanumeric characters except spaces, hyphens, underscores, 
    # parentheses, pipes, square brackets, and commas
    clean_text = re.sub(r'[^a-zA-Z0-9\s\-_()|\[\],]', '', text)
    
    # Then, remove any leading commas and spaces
    clean_text = re.sub(r'^[,\s]+', '', clean_text)
    
    # Finally, remove any trailing commas and spaces
    clean_text = re.sub(r'[,\s]+$', '', clean_text)
    
    return clean_text.strip()

def process_row(row):
    # ... [rest of the function remains the same]

# ... [rest of the script remains the same]

import re

def mask_entity(text, pattern, entity_type, replacement, entities_list):
    for match in re.finditer(pattern, text):
        start, end = match.span()
        original = match.group()
        text = text[:start] + replacement + text[end:]
        entities_list.append({
            "position": [start, start + len(replacement)],
            "classification": entity_type,
            "entity": original
        })
    return text, entities_list

def mask_pii(email_text):
    masked_entities = []

    # Email Address
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_text, masked_entities = mask_entity(email_text, email_regex, 'email', '[email]', masked_entities)

    # Phone Number
    phone_regex = r'\b\d{10}\b'
    email_text, masked_entities = mask_entity(email_text, phone_regex, 'phone_number', '[phone_number]', masked_entities)

    # Aadhaar
    aadhaar_regex = r'\b\d{4}\s\d{4}\s\d{4}\b'
    email_text, masked_entities = mask_entity(email_text, aadhaar_regex, 'aadhar_num', '[aadhar_num]', masked_entities)

    # Card Number
    card_regex = r'\b(?:\d[ -]*?){13,16}\b'
    email_text, masked_entities = mask_entity(email_text, card_regex, 'credit_debit_no', '[credit_debit_no]', masked_entities)

    # CVV
    cvv_regex = r'\b\d{3}\b'
    email_text, masked_entities = mask_entity(email_text, cvv_regex, 'cvv_no', '[cvv_no]', masked_entities)

    # Expiry Date
    expiry_regex = r'\b(0[1-9]|1[0-2])\/\d{2}\b'
    email_text, masked_entities = mask_entity(email_text, expiry_regex, 'expiry_no', '[expiry_no]', masked_entities)

    # Date of Birth
    dob_regex = r'\b(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[012])\/\d{4}\b'
    email_text, masked_entities = mask_entity(email_text, dob_regex, 'dob', '[dob]', masked_entities)

    # Full Name detection (simple method)
    name_regex = r'\bmy name is ([A-Za-z\s]+)\b'
    matches = re.finditer(name_regex, email_text, re.IGNORECASE)
    for match in matches:
        start, end = match.span(1)
        original = match.group(1)
        email_text = email_text[:start] + '[full_name]' + email_text[end:]
        masked_entities.append({
            "position": [start, start + len('[full_name]')],
            "classification": "full_name",
            "entity": original
        })

    return email_text, masked_entities

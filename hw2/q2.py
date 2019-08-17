from q2_atm import ATM, ServerResponse


def extract_PIN(encrypted_PIN):
    """Extracts the original PIN string from an encrypted PIN."""
    # Return an integer.
    #raise NotImplementedError()
    atm_try=ATM()
    for i in range(0,11000):
    	pin=getattr(atm_try,'encrypt_PIN')
    	if pin(i)==encrypted_PIN:
    		return i
    return -1


def extract_credit_card(encrypted_credit_card):
    """Extracts a credit card number string from its ciphertext."""
    # Return an integer.
    #raise NotImplementedError()
    atm_try = ATM()
    credit_num = getattr(atm_try,'encrypt_credit_card')
    pin = int(round(encrypted_credit_card**(1.0/3)))
    pinT = pin**3
    encr_credit_num = credit_num(pin)
    if(pinT == encrypted_credit_card) and encr_credit_num == encrypted_credit_card:
    	real_creadit_card = pin
    	return real_creadit_card



def forge_signature():
	atm_try = ATM()
	number = getattr(atm_try,'encrypt_number')
	approval = atm_try.CODE_APPROVAL
	rsa_card = atm_try.rsa_card
	return ServerResponse(approval,number(rsa_card,approval))
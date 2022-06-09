# int()

def validate_ipv4_address(address):
    for s in address.split("."):
        if int(s) < 0 or int(s) > 255:
            return False
    return True

import re
import string

def create_password_checker(uppercase, lowercase, punctuation, digits):
    cmpdic = {'uppercase': uppercase,
              'lowercase': lowercase,
              'punctuation': punctuation,
              'digits': digits}

    def pass_check(passwd):
        pdic = {
            'uppercase':   len(re.findall('[A-Z]', passwd)),
            'lowercase':   len(re.findall('[a-z]', passwd)),
            'punctuation': len(re.findall(f'[{string.punctuation}]', passwd)),
            'digits':      len(re.findall('[0-9]', passwd))
        }
        return all([pdic[k] >= cmpdic[k] for k in cmpdic]), { k:pdic[k]-cmpdic[k] for k in cmpdic}
    return pass_check

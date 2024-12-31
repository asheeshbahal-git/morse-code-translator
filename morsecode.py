class MorseCode:
    
    DICT_MORSE_CODE = { 
                        'A':'.-', 
                        'B':'-...',
                        'C':'-.-.', 
                        'D':'-..', 
                        'E':'.',
                        'F':'..-.', 
                        'G':'--.', 
                        'H':'....',
                        'I':'..', 
                        'J':'.---', 
                        'K':'-.-',
                        'L':'.-..', 
                        'M':'--', 
                        'N':'-.',
                        'O':'---', 
                        'P':'.--.', 
                        'Q':'--.-',
                        'R':'.-.', 
                        'S':'...', 
                        'T':'-',
                        'U':'..-', 
                        'V':'...-', 
                        'W':'.--',
                        'X':'-..-', 
                        'Y':'-.--', 
                        'Z':'--..',
                        '1':'.----', 
                        '2':'..---', 
                        '3':'...--',
                        '4':'....-', 
                        '5':'.....', 
                        '6':'-....',
                        '7':'--...', 
                        '8':'---..', 
                        '9':'----.',
                        '0':'-----'
                    }
    ##
    # Retrieve letter corresponding to supplied morse code
    ##
    def GetKeyByValue(self, morse_code: str) -> str:
        
        key_by_value = ''
        # for key,value in self.DICT_MORSE_CODE.items():
        #     if value == morse_code:
        #         key_by_value = key
        #         break
        
        key_list = list(self.DICT_MORSE_CODE.keys())
        value_list = list(self.DICT_MORSE_CODE.values())
        key_by_value = key_list[value_list.index(morse_code)]
        
        # key_by_value = list(filter(lambda x: self.DICT_MORSE_CODE[x] == morse_code, self.DICT_MORSE_CODE))[0]

        return key_by_value
    
    # ###############################################
    # Encode the input english message to morse code
    # ###############################################
    def Encrypt(self, message: str) -> str:
        
        str_encrypted = ''
        if message == '':
            print("Message to encrpyt cannot be empty")
            str_encrypted = 'Value Error'
            return str_encrypted
        
        for letter in message:
            if letter.isspace():
                str_encrypted += ' '
            else:
                if letter.isalpha(): letter = letter.upper()
                str_encrypted += self.DICT_MORSE_CODE[letter] + ' '
               
        return str_encrypted.rstrip()
    
    # #######################################
    # Decode the passed morse code to english
    # #######################################
    def Decrypt(self, message: str) -> str:

        str_decrypted = ''
        if message == '':
            print("Message to dencrpyt cannot be empty")
            str_decrypted = 'Value Error'
            return str_decrypted
        
        morse_message_letter = message.split(' ')    
        for morse_code in morse_message_letter:
            if morse_code != '':
                str_decrypted += self.GetKeyByValue(morse_code)
            else:
                str_decrypted += ' '
        
        return str_decrypted
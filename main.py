from morsecode import MorseCode 

def main():
    obj_mc = MorseCode()

    str_input_message = ''
    while str_input_message != 'exit':
        str_input_message = input('Enter the message to convert t0 Morse code, type exit to close: ')

        str_encoded_message = obj_mc.Encrypt(str_input_message)
        str_decoded_message = obj_mc.Decrypt(str_encoded_message)

        print (f'Encoded message: {str_decoded_message} Decoded message: {str_decoded_message}')

if __name__ == '__main__':
    main()

########################################################################################################################
#   author:     Richard Hohensinner
#   created:    31.07.2020
#   modified:   31.07.2020
########################################################################################################################

# project files
import error_messages

# external libraries
import pyAesCrypt
import sys
import configparser


########################################################################################################################
# exp: main function for file encr/decr
# params: file, config file
# output: encr/decr file
########################################################################################################################
def main():
    # check if args are fitting
    if len(sys.argv) < 3:
        print(error_messages.ERR_USAGE)
        pass

    # verify args are correct
    if len(sys.argv) == 3:
        # variable init
        file = None
        cp = None
        mode = None
        buffersize = None
        password = None

        # try opening file
        try:
            file = open(sys.argv[1], "rb")
        except FileExistsError:
            print(error_messages.ERR_TARGET)
            pass

        # check if config is valid
        try:
            cp = configparser.ConfigParser()
            cp.read(sys.argv[2])
        except FileNotFoundError:
            print(error_messages.ERR_CONFIG)
            pass

        # read mode
        try:
            mode = cp["CONF"]["mode"]
        except KeyError:
            print(error_messages.ERR_CONFIG_MODE)
            pass
        # read buffer size
        try:
            buffersize = cp["CONF"]["buffersize"]
            buffersize = eval(buffersize)
        except KeyError:
            print(error_messages.ERR_CONFIG_BUFFER)
            pass
        # read password
        try:
            password = cp["CONF"]["password"]
        except KeyError:
            print(error_messages.ERR_CONFIG_PASSWORD)
            pass

        print(file.name, mode, buffersize, password)

        if mode == "encrypt":
            encrypt_file(file, buffersize, password)
        elif mode == "decrypt":
            decrypt_file(file, buffersize, password)
        else:
            print(error_messages.ERR_INVMODE)


# -------------------------------------------------------------------------------------------------------------------- #


########################################################################################################################
# exp: main function for file encr/decr
# params: file, buffersize, password
# output: encr/decr file
########################################################################################################################
def encrypt_file(file, buffersize, password):
    print("encrypt_file called!")
    out_file_name = file.name + ".aes"
    try:
        pyAesCrypt.encryptFile(file.name, out_file_name, password, buffersize)
    except FileExistsError:
        "error"

# -------------------------------------------------------------------------------------------------------------------- #


########################################################################################################################
# exp: main function for file encr/decr
# params: file, config file
# output: encr/decr file
########################################################################################################################
def decrypt_file(file, buffersize, password):
    print("decrypt_file called!")
    out_file_name = file.name[:-4]
    try:
        pyAesCrypt.decryptFile(file.name, out_file_name, password, buffersize)
    except FileExistsError:
        "error"
# -------------------------------------------------------------------------------------------------------------------- #


if __name__ == "__main__":
    main()

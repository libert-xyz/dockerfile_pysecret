
import sys
secret = 's3cr3t'
secret_loop = True

while secret_loop:
    try:
        secret_in = input('Enter the secret: ')
        if secret_in == secret:
           print ('################')
           print ('#You are hacker#')
           print ('################')
           secret_loop = False
        else:
            print ('Invalid Secret')
    except KeyboardInterrupt:
        print (' Bye')
        sys.exit()

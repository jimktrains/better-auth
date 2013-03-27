#!/usr/bin/env python3
import hmac
import hashlib
import binascii
import test_auth_rsa
import random 
######### DONE IN BROWSER ##############
email = "jim@jimkeener.com"
emailb = bytes(email, 'ascii')
password = "this_is_a_test"
passwb = bytes(password, 'ascii')

h = hmac.new(passwb, None, hashlib.sha512)

######## SITE SENDS SALT  ############
######## Would be random. Being cheap here ###########
######## So that I get the same random for each user. this would be in a db#######

rand = hashlib.sha512(passwb).digest()
######################################################
############ DONE IN BROWSER #########################
h.update(rand)
h.update(emailb)

random.seed(int(h.hexdigest(), 16))

pubkey,privkey = test_auth_rsa.keygen(2**1024)

##################### During Registration pubkey is set to server #############

####################################
######### Login ####################
####################################
random.seed()

###############Server Sends Challenge encoded by public key################

challenge1 = hex(random.randrange(1111111111111111111111111111111111111111))
challenge = test_auth_rsa.encode(challenge1, pubkey)
challenge2 = hex(random.randrange(1111111111111111111111111111111111111111))


###############Client then sends encode(challenge2, privkey)####################

challenge = test_auth_rsa.decode(challenge, privkey, pubkey)
if challenge != challenge1:
    print("Challenge doesn't matchup")
    exit()
resp = test_auth_rsa.encode(challenge2, privkey)

######################Server checks response#######################

check_resp = test_auth_rsa.decode(resp, pubkey, pubkey)
if challenge2 != check_resp:
    print("Response doesn't match")
    exit()

print("All's well!")

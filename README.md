better-auth
===========

This is a test/proof-of-concept for a password-based client-server authentication that provides mutual authentication and no secrets being stored on the server.

To run the test ``python3 test_auth.py``

Login:

         Client                   |     Server
     POST /login username=blah ------->
                              <------- salt, challenge1, challenge2, encrypted(challenge1, public_key)
    Generate public and private
       keys based on salt,
       username, and password
    
    Validates challenge1 vs 
       decrypt(
         encrypted(challenge1, 
                   public_key), 
         private_key)
    
    Generates 
       encrypted(
         challenge2, 
         private_key)          -------->
                                          Validates encrypted-challenge2
    
                              <---------   Generates Session identifier

Register:

         Client                   |     Server
    POST /register
        username=blah
        public_key=blah        --------> Validates that name is unique and key makes sense
                              <--------- Confirms registration

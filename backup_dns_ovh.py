'''
First, install the latest release of Python wrapper: $ pip install ovh
'''
import json
import ovh

# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page
client = ovh.Client(
    endpoint='ovh-eu',               # Endpoint of API OVH Europe (List of available endpoints)
    application_key='****',    # Application Key
    application_secret='***', # Application Secret
    consumer_key='***',       # Consumer Key
)

result = client.get('/domain/zone')

text_file = open("Output_final.txt", "w")
for i in result:
    print "backup domain zone", i
    backup =  client.get('/domain/zone/'+i+'/export')
    text_file.write( "\n" + i + "\n" )
    text_file.write("%s\n" % backup )

text_file.close()

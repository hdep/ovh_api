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
    application_key='***',    # Application Key
    application_secret='***', # Application Secret
    consumer_key='***',       # Consumer Key
)

result = client.get('/domain/zone')

for i in result:
  print "modify domain zone", i
  client.post('/domain/zone/'+i+'/record',
      fieldType='TXT', # Resource record Name (type: zone.NamedResolutionFieldTypeEnum)
      subDomain='_dmarc', # Resource record subdomain (type: string)
      target='"TOTO"', # Resource record target (type: string)
      ttl=400, # Resource record ttl (type: long)
  )

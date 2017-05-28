from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

randomGenerator = Random.new().read
private_key = RSA.generate(1024, randomGenerator)
public_key = self.private_key.publickey().exportKey("PEM")

string = 'hello world'
enc = public_key.encrypt(encoded_packet, 32)[0]
dec = private_key.decrypt(enc)

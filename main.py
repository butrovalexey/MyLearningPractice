import rsa
pubA, privA = rsa.newkeys(512)
pubB, privB = rsa.newkeys(512)
message = "Hello, world".encode()
soob = "Hi there".encode()
#rsa.encrypt()
#rsa.decrypt()
S = rsa.sign(message, privA, 'SHA-256')
V = rsa.sign(message, privB, 'SHA-256')
rsa.verify(message, S, pubA)
rsa.verify(message, S, pubB)
rsa.verify("nice", S, pubA)
rsa.verify(message, V, pubA)
rsa.verify(message, S, privA)
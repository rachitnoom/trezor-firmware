# Automatically generated by pb2py
from protobuf import protobuf as p
t = p.MessageType('PassphraseAck')
t.wire_type = 42
t.add_field(1, 'passphrase', p.UnicodeType, flags=p.FLAG_REQUIRED)
PassphraseAck = t
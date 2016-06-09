# Automatically generated by pb2py
from protobuf import protobuf as p
from .MultisigRedeemScriptType import MultisigRedeemScriptType
t = p.MessageType('TxOutputType')
t.add_field(1, 'address', p.UnicodeType)
t.add_field(2, 'address_n', p.UVarintType, flags=p.FLAG_REPEATED)
t.add_field(3, 'amount', p.UVarintType, flags=p.FLAG_REQUIRED)
t.add_field(4, 'script_type', p.UVarintType, flags=p.FLAG_REQUIRED)
t.add_field(5, 'multisig', p.EmbeddedMessage(MultisigRedeemScriptType))
t.add_field(6, 'op_return_data', p.BytesType)
TxOutputType = t
from Message import Message
import json
from compression import *

d = Message('socketConnector', 'PoolTrue', 'Data')
# d = json.dumps(d)
d = jsonpickle.encode(d, unpicklable=True)
d = d.encode("utf-8")
d = compress(d)

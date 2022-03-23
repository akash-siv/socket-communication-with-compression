import json
import jsonpickle
import zlib
import pickle


def dataencode(objectToEncode):
    data_out = jsonpickle.encode(objectToEncode, unpicklable=True)
    data_out = data_out.encode("utf-8")
    # compressed_data = compress(data_out)
    # return jsonpickle.encode(compressed_data, unpicklable=True)
    return data_out

def datadecode(encodedObject):
    data_in = jsonpickle.decode(encodedObject)
    # data_in = decompress(data_in)
    data_in = data_in.decode("utf-8")
    # data_in = json.dumps(data_in)
    # return jsonpickle.decode(data_in)
    return data_in

def compress(data):
    """ it gets the encoded bytes data as input and returns the compressed data. compression amount can be varied
    based on your needs. """
    return zlib.compress(data)


def decompress(data):
    """ it gets the compressed bytes data as input and returns the decompressed data. """
    return zlib.decompress(data)

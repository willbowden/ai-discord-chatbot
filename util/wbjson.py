import json
import os
from types import SimpleNamespace
import config

def ReadFile(filename):
    filename = config.DATA_FILEPATH + filename
    f = open(filename, "r")
    obj = json.loads(f.read(), object_hook=lambda d: SimpleNamespace(**d))
    return obj

def WriteFile(filename, data):
    filename = config.DATA_FILEPATH + filename
    f = open(filename, "w")
    d = vars(data)
    encoded = json.dumps(d)
    f.write(encoded)
    f.close()

def ReadToRaw(filename):
    filename = config.DATA_FILEPATH + filename
    f = open(filename, "r")
    decoded = json.loads(f.read())
    f.close()
    return decoded

def WriteRaw(filename, data):
    filename = config.DATA_FILEPATH + filename
    f = open(filename, "w")
    decoded = json.dumps(data)
    f.close()
import tensorflow as tf
import tensorflow_hub as hub

__module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
__model = hub.load(__module_url)
print ("module %s loaded" % __module_url)
def embed(input):
  return __model(input)
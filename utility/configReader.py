import yaml

class configReader:

  def __init__(self):
   stream = open("../config.yaml","r")
   self.configs = yaml.load_all(stream)



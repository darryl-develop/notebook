import uuid, yaml, random


# config.yml
# template:
#   value: null


class YamlPython:
    def __init__(self):
        self.dictionary_a={}
        self.list_a = ['a','b']

        with open('config.yml') as yml:
            yamlFile = yaml.load(yml)

            self.temp = yamlFile['template']

    def create_index(self):
        ID = str(uuid.uuid4())
        value=random.choice(self.list_a)
        print value

        # Mutability Issue
        self.dictionary_a[ID]=self.temp
      # self.dictionary_a[ID]=self.temp.copy()

        self.dictionary_a[ID]['value']=value


if __name__ == '__main__':
    YP=YamlPython()

    for r in range(10):
        YP.create_index()

    for index in YP.dictionary_a:
        print index, YP.dictionary_a[index]

    for k,v in YP.dictionary_a.items():
     print k, id(v)

class audi:
    def __init__(self):
        self.models['a8','a6','q7','q3']
    def outmodels(self):
        print('These are the available models for audi')
        for model in self.models:
            print('\t%s'%model)
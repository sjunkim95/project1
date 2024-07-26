class NamespaceManager:
    def __init__(self):
        self.namespace = {}

    def set_variable(self, name, value):
        self.namespace[name] = value

    def get_variable(self, name):
        if self.namespace.get(name) is None:
            raise KeyError('There is no given name')
        else:
            return self.namespace[name]

    def delete_variable(self, name):
        if self.namespace.get(name) is None:
            raise KeyError('There is no given name')
        else:
            del self.namespace[name]

    def list_variables(self):
        # {a:1, b:1, c:1}
        #return [a,b,c] -> return the "list" of keys
        return list(self.namespace.keys())

    def execute_function(self, code):
        exec(code, {}, self.namespace)
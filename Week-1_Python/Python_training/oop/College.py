class College:
    def __init__(self,c_code,c_name):
        self._c_code=c_code
        self._c_name=c_name

    def display(self):
        return self._c_code,self._c_name
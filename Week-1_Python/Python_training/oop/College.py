
class College:
    def __init__(self,c_code,c_name):
        self._c_code=c_code
        self._c_name=c_name

    def col_display(self):
        return self._c_code,self._c_name

    @property
    def c_code(self):
        return self._c_code

    @property
    def c_name(self):
        return self._c_name
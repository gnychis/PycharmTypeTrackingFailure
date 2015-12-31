class A(object):

    def __init__(self):
        pass


class B(object):

    def __init__(self):
        self._a = A()


class C(B):

    def __init__(self):
        super(C, self).__init__()

    def test_method(self, i: int):
        pass

    def download_image(self):
        self.test_method(2)         # Correctly identified as OK.
        self.test_method(A())       # Correctly identified as NOT OK.

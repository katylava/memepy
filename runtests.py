import unittest
from meme.tests import test_meme


def runtests():
    suite = unittest.TestLoader().loadTestsFromModule(test_meme)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    runtests()

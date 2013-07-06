import unittest
import meme


def runtests():
    suite = unittest.TestLoader().loadTestsFromModule(meme.tests)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    runtests()

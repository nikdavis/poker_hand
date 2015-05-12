from distutils.core import setup

setup(
    name='poker_hand',
    version='1.0.0',
    url='http://github.com/nikdavis/poker_hand',
    license='MIT',
    author='Nik Davis',
    tests_require=['pytest'],
    author_email='nik@newrelic.com',
    description='Basic poker hand reader.',
    packages=['poker_hand',
              'poker_hand.parsers']
)
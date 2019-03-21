from setuptools import setup

setup(
    name='realtimeasm',
    version='1.0.0',
    packages=['realtimeasm'],
    install_requires=[
        'watchdog',
        'hexdump'
    ],
    entry_points={
        'console_scripts': [
            'realtimeasm = realtimeasm.__main__:main'
        ]
    }
)

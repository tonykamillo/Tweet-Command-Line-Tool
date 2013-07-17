"""
Tweet-Command-Line-Tool
-------------

Simple python script to send tweets. It can be ease integrated to another app, such as media player, to send Now Playing status.
"""
from setuptools import setup


setup(
    name='Tweet-Command-Line-Tool',
    version='0.6',
    url='https://github.com/sacanix/Tweet-Command-Line-Tool',
    license='BSD',
    author='Tony Kamillo (Sacanix)',
    author_email='tonysacanix@gmail.com',
    description='''Simple python script to send tweets. It can be ease integrated to another app, such as media player, to send Now Playing status.''',
    long_description=__doc__,
    # if you would be using a package instead use packages instead
    # of py_modules:
    py_modules=['tweet-tool'],
    #packages=[],
    #zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['python-twitter'],
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
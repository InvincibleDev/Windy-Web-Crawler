from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Windy-Web-Crawler',
    version="v0.20",
    packages=['windy_web_crawler',],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=['pyppeteer==0.0.25', "beautifulsoup4==4.8.2", "lxml==4.5.0", "geopy==1.20.0", "prettytable==0.7.2"],
    extras_require={
        'libcloud': ['apache-libcloud'],
        'sftp': ['paramiko'],
    },
    author='Ganesh Prasad B G',
    author_email='gnshprasad402@gmail.com',
    license='Mozilla Public License Version 2.0',
    description="Windy-Web-Crawler is a command line web crawler that crawls 'www.windy.com' and displays the Temperature and wind speed for next 5 days ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    zip_safe=False
)

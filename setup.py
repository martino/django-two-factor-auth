from setuptools import find_packages, setup

setup(
    name='django-two-factor-auth',
    version='1.10.1',
    description='Complete Two-Factor Authentication for Django',
    long_description=open('README.rst').read(),
    author='Bouke Haarsma',
    author_email='bouke@haarsma.eu',
    url='https://github.com/Bouke/django-two-factor-auth',
    download_url='https://pypi.python.org/pypi/django-two-factor-auth',
    license='MIT',
    packages=find_packages(exclude=('example', 'tests')),
    install_requires=[
        'Django>=1.11',
        'django_otp>=0.6.0,<0.99',
        'qrcode>=4.0.0,<6.99',
        'django-phonenumber-field>=1.1.0,<3.99',
        'django-formtools',
        'webauthn>=0.4.5',
    ],
    extras_require={
        'Call': ['twilio>=6.0'],
        'SMS': ['twilio>=6.0'],
        'YubiKey': ['django-otp-yubikey'],
        'phonenumbers': ['phonenumbers>=7.0.9,<8.99',],
        'phonenumberslite': ['phonenumberslite>=7.0.9,<8.99',],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Security',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ],
)

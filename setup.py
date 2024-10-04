from setuptools import setup, find_packages

setup(
    name='au_sheets',
    version='0.1.0',
    author='Andrey Pshenitsyn',
    description='Google sheets automatization library',
    packages=find_packages(),
    install_requires=[
        'requests',
        'cachetools',
        'python-dotenv',
        'oauth2client',
        'pandas',
        'gspread'
    ],
)
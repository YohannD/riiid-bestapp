from setuptools import setup, find_packages

REQUIRED_PACKAGES = [
'pytz',
'gcsfs==0.6.0',
'pandas==0.24.2',
'scikit-learn==0.23.2',
'google-cloud-storage==1.26.0',
'numpy==1.18.4',
'xgboost==1.1.1',
'scipy== 1.2.2',
'flask==1.1.1',
'flask-cors',
'pickleshare==0.7.5',
's3fs',
'streamlit==0.72.0']


setup(
    name='Riiid challenge',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Riiid challenge Pipeline',
    install_requires=requirements
)

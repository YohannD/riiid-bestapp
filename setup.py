from setuptools import setup, find_packages

REQUIRED_PACKAGES = [
'pytz',
'gcsfs==0.6.0',
'pandas==0.24.2',
'scikit-learn==0.23.2',
'sklearn==0.0',
'seaborn==0.11.0',
'google-cloud-storage==1.26.0',
'mlflow==1.8.0',
'joblib==0.14.1',
'numpy==1.18.4',
'psutil==5.7.0',
'pygeohash==1.2.0',
'termcolor==1.1.0',
'xgboost==1.1.1',
'memoized-property==1.0.3',
'scipy== 1.2.2',
'category_encoders==2.2.2',
'flask==1.1.1',
'flask-cors',
'gunicorn',
's3fs',
'herepy==2.1.1',
'streamlit',
'pickleshare==0.7.5']


setup(
    name='Riiid challenge',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Riiid challenge Pipeline',
    install_requires=requirements
)

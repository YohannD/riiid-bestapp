PROJECT_ID=speedy-area-297510
BUCKET_NAME=riiid-project

# ----------------------------------
#         LOCAL SET UP
# ----------------------------------

run_locally:
	@python -W ignore -m ${PACKAGE_NAME}.${FILENAME}

install_requirements:
	@pip install -r requirements.txt

set_project:
	-@gcloud config set project ${PROJECT_ID}


# ----------------------------------
#         HEROKU COMMANDS
# ----------------------------------
APP_NAME=riiid-app
run_streamlit:
	-@streamlit run app_test.py

heroku_login:
	-@heroku login

heroku_create_app:
	-@heroku create ${APP_NAME}

deploy_heroku:
	-@git push heroku master
	-@heroku ps:scale web=1
# ----------------------------------
#    LOCAL INSTALL COMMANDS
# ----------------------------------
install:
	@pip install . -U


clean:
	@rm -fr */__pycache__
	@rm -fr __init__.py
	@rm -fr build
	@rm -fr dist
	@rm -fr ${PACKAGE_NAME}-*.dist-info
	@rm -fr ${PACKAGE_NAME}.egg-info
	-@rm model.joblib

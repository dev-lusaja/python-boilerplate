## VIRTUALENV VARS ##
VENV_DIR = venv

## VIRTUALENV TARGETS ##
venv-activate: ## Enable virtual environment (virtualenv): make venv-activate
	@docker container run --workdir "/${APP_DIR}" --rm -it \
		-v "${PWD}/${VENV_DIR}":/${VENV_DIR} \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
		-e VENV_DIR=/${VENV_DIR} \
		--entrypoint=/resources/venv.sh \
		${IMAGE_RUNTIME} bash

venv-create: ## Create the virtual environment (virtualenv): make venv-create
	@docker container run --workdir "/${APP_DIR}" --rm -it \
		-v "${PWD}/${VENV_DIR}":/${VENV_DIR} \
		--tty=false --entrypoint="" \
		${IMAGE_RUNTIME}  python3 -m virtualenv --python=/usr/bin/python3 /${VENV_DIR}

venv-install-lib: ## Install requirements for virtual environment (virtualenv): make venv-install-lib
	@docker container run --workdir "/${APP_DIR}" --rm -it \
		-v "${PWD}/${VENV_DIR}":/${VENV_DIR} \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
		--tty=false --entrypoint="" \
		${IMAGE_RUNTIME}  "/${VENV_DIR}/bin/pip3.5" install -r requirements.txt

venv-list-requirements: ## List all libs in virtual environment (virtualenv): make venv-list-requirements
	@docker container run --workdir "/${APP_DIR}" --rm -it \
		-v "${PWD}/${VENV_DIR}":/${VENV_DIR} \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
		-e VENV_DIR=/${VENV_DIR} \
		--entrypoint=/resources/venv.sh \
		${IMAGE_RUNTIME} pip3.5 freeze

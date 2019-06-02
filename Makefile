.DEFAULT_GOAL := help
.PHONY: venv
.EXPORT_ALL_VARIABLES:

## GENERAL VARS ##
PRODUCT_NAME 	 	= project
SERVICE_NAME 	    = owner
ENV				    = dev
PROJECT_NAME	    = $(PRODUCT_NAME)_$(ENV)_$(SERVICE_NAME)
APP_DIR  			= app

## MYSQL LOCAL VARS ##
MYSQL_PWD = 123456
MYSQL_DB_NAME = $(PROJECT_NAME)
MYSQL_PORT = 3306

## INCLUDE TARGETS ##
include makefiles/deploy.mk
include makefiles/container.mk
include makefiles/virtualenv.mk

## DEVELOPER TARGETS ##
development: build venv-create venv-install-lib up ## Prepare the project for development: make development
	@echo "The development environment is ready and running"

generate-requirements: ## Generate requirements.txt: make generate-requirements
	@docker container run --workdir "/${APP_DIR}" --rm -it \
		-v "${PWD}/${VENV_DIR}":/${VENV_DIR} \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
		-e VENV_DIR=/${VENV_DIR} \
		--entrypoint=/resources/venv.sh \
		${IMAGE_RUNTIME} pip3.5 freeze > ${APP_DIR}/requirements.txt

clean-cache: ## Remove python cache files: make clean-cache
	@sudo find . | grep -E "(__pycache__|\.pyc|\.pyo$|.pytest_cache)" | xargs rm -rf

test: ## Run the unit tests: make test
	@docker container run --workdir "/${APP_DIR}" --rm -it \
		-v "${PWD}/${VENV_DIR}":/${VENV_DIR} \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
		-e VENV_DIR=/${VENV_DIR} \
		--entrypoint=/resources/venv.sh \
		${IMAGE_RUNTIME} pytest

## HELP TARGET ##

help:
	@printf "\033[31m%-22s %-59s %s\033[0m\n" "Target" " Help" "Usage"; \
	printf "\033[31m%-22s %-59s %s\033[0m\n"  "------" " ----" "-----"; \
	grep -hE '^\S+:.*## .*$$' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' | sort | awk 'BEGIN {FS = ":"}; {printf "\033[32m%-22s\033[0m %-58s \033[34m%s\033[0m\n", $$1, $$2, $$3}'

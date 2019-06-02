## CONTAINER VARS ##
TAG_DEV			= dev
DOCKER_NETWORK 	= $(PRODUCT_NAME)_network
CONTAINER_NAME 	= $(PROJECT_NAME)_backend
IMAGE_RUNTIME	= $(PROJECT_NAME):$(TAG_DEV)

## CONTAINER TARGETS ##
build: ## Build docker image for development: make build
	@docker build -f docker/runtime/Dockerfile -t $(IMAGE_RUNTIME) docker/runtime/

up: verify_network ## Start the project: make up
	@docker-compose -p $(PROJECT_NAME) up -d

down: ## Destroy the project: make down
	@docker-compose -p $(PROJECT_NAME) down

log: ## Show project logs: make log
	@docker logs -f  $(CONTAINER_NAME)

ssh: ## Access the docker container: make ssh
	@docker container run -it --rm -v "${PWD}/${VENV_DIR}":/${VENV_DIR} -v "${PWD}/${APP_DIR}":/${APP_DIR} --entrypoint="" $(IMAGE_RUNTIME) bash

remove:
	@docker-compose rm -v

verify_network: ## Verify the local network was created in docker: make verify_network
	@if [ -z $$(docker network ls | grep $(DOCKER_NETWORK) | awk '{print $$2}') ]; then\
		(docker network create $(DOCKER_NETWORK));\
	fi
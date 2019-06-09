## CONTAINER VARS ##
TAG_DEV			= dev
DOCKER_NETWORK 	= $(PRODUCT_NAME)_network
CONTAINER_NAME 	= $(PROJECT_NAME)_backend
IMAGE_RUNTIME	= $(PROJECT_NAME):$(TAG_DEV)

## CONTAINER TARGETS ##
runtime-image: ## Build docker image for development: make runtime-image
	@docker build -f docker/runtime/Dockerfile -t $(IMAGE_RUNTIME) docker/runtime/

container-up: verify_network ## Start the project: make container-up
	@docker-compose -p $(PROJECT_NAME) up -d

container-down: ## Destroy the project: make container-down
	@docker-compose -p $(PROJECT_NAME) down

container-log: ## Show project logs: make container-log
	@docker logs -f  $(CONTAINER_NAME)

container-ssh: ## Access the docker container: make container-ssh
	@docker container run -it --rm \
	-v "${PWD}/${VENV_DIR}":/${VENV_DIR} -v "${PWD}/${APP_DIR}":/${APP_DIR} \
	-e VENV_DIR=/${VENV_DIR} \
	--entrypoint=/resources/venv.sh $(IMAGE_RUNTIME) bash

container-remove:
	@docker-compose rm -v

verify_network: ## Verify the local network was created in docker: make verify_network
	@if [ -z $$(docker network ls | grep $(DOCKER_NETWORK) | awk '{print $$2}') ]; then\
		(docker network create $(DOCKER_NETWORK));\
	fi
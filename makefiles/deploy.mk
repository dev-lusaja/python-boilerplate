## DEPLOY VARS ##
BUILD_NUMBER 	?= 000001
BUILD_TIMESTAMP ?= 1560121554
TAG_DEPLOY		= $(BUILD_TIMESTAMP).$(BUILD_NUMBER)
IMAGE_DEPLOY	= $(PROJECT_NAME):$(TAG_DEPLOY)

## DEPLOY TARGETS ##
deploy-image: runtime-image ## Create a Docker image with the dependencies packaged: make deploy-image
	@docker build -f docker/deploy/Dockerfile --no-cache --build-arg IMAGE=$(IMAGE_RUNTIME) -t $(IMAGE_DEPLOY) .

deploy-unit-test: ## Run the unit tests: make deploy-unit-test
	@docker container run --rm -it \
		--entrypoint=pytest \
		${IMAGE_DEPLOY} -v

## DEPLOY VARS ##
BUILD_NUMBER 	?= 000001
BUILD_TIMESTAMP ?= $(shell date +%s)
TAG_DEPLOY		= $(BUILD_TIMESTAMP).$(BUILD_NUMBER)
IMAGE_DEPLOY	= $(PROJECT_NAME):$(TAG_DEPLOY)

## DEPLOY TARGETS ##
install: build venv-create venv-install-lib ## Create a Docker image with the dependencies packaged: make install
	docker build -f docker/deploy/Dockerfile --no-cache --build-arg IMAGE=$(IMAGE_RUNTIME) -t $(IMAGE_DEPLOY) .

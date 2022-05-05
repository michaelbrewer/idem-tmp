build:
	sam validate
	sam build

deploy: build
	sam deploy

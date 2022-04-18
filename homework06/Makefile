deploy:
	cp deployment/deployment.yml deployment.yml
	bash repl.sh
	kubectl apply -f deployment/data-redis-volume.yml
	kubectl apply -f deployment.yml

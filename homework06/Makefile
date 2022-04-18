deploy:
	cp deployment/deployment.yml deployment.yml
	kubectl apply -f deployment/service-flask.yml
	kubectl apply -f deployment/service-redis.yml
	bash repl.sh
	kubectl apply -f deployment/data-redis-volume.yml
	kubectl apply -f deployment.yml

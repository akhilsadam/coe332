deploy:
	cp deployment/deployment.yml deployment.yml
	kubectl apply -f deployment/service-flask.yml
	kubectl apply -f deployment/service-redis.yml
	bash repl.sh
	kubectl apply -f deployment/data-redis-volume.yml
	kubectl apply -f deployment.yml

clean:
	- kubectl delete deployment flask-cube-redis
	- kubectl delete pvc data-redis-volume-as-tacc-test
	- kubectl delete services flask-cube-redis-flask-service
	- kubectl delete services flask-cube-redis-redis-service
name=positional-iss
path=../../
format=png
project=${path}${name}
imgdir=img


image:
	cd ${project} && pyreverse -ASmy  wsgi.py config.py testall.py app -o ${format}
	- mkdir -p ./${imgdir}
	- mv ${project}/*.${format} ./${imgdir}
	- mv ${project}/*.dot ./${imgdir}

mermaid:
	$$(cat src/register.mmd | python -c "import sys; import base64; import zlib; print(base64.urlsafe_b64encode(zlib.compress(sys.stdin.read().encode('utf-8'), 9)).decode('ascii'))" > tmp.key)
	curl -X GET https://kroki.io/mermaid/png/$$(cat tmp.key) --output img/register.png
	rm tmp.key

push:
	git add .
	- git commit -m "[auto] update README"
	git push
.PHONY: run
run: 
	poetry run python ask_academic_dates/__init__.py

.PHONY: python
python: 
	poetry run python

.PHONY: build
build: 
	poetry build


.PHONY: publish
publish: 
	poetry publish


.PHONY: push
push: 
	git push -u origin master



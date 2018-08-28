.PHONY: clean
clean:
	rm -rf build
	rm -rf src/*.egg-info

.PHONY: check
check:
	tox -e check

.PHONY: sdist
sdist:
	python setup.py clean --all sdist bdist_wheel

.PHONY: upload
upload:
	twine upload --skip-existing dist/*.whl dist/*.gz dist/*.zip

.PHONY: all
all: clean check sdist upload


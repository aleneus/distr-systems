.PHONY: test

PACKAGE_FOLDER="."

check: test fixme

test:
	@nose2 --with-coverage

fixme:
	@rgrep "TODO" -n \
		--include="*py" \
		--include="*rst" \
		--include="*md" \
		--exclude-dir=env \
		|| true

	@rgrep "# REF" -n \
		--include="*py" \
		|| true

lint:
	pylint $(PACKAGE_FOLDER) || true

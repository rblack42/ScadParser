MK := mk
PROJECT := scadparser

.PHONY: dirvenv
dirvenv:
	echo 'layout python3' > .envrc &&\
		direnv allow

-include $(MK)/help.mk
-include $(MK)/python.mk
-include $(MK)/pypi.mk
-include $(MK)/version.mk
-include $(MK)/sphinx.mk

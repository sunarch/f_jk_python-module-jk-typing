################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"License :: OSI Approved :: Apache Software License",
		"Programming Language :: Python :: 3",
	],
	description = "This module provides capabilities for type checking function arguments. (NOTE: A full type check with this module is not possible, since this is fundamentally not possible due to limitiations of Python itself.)",
	include_package_data = False,
	install_requires = [
	],
	keywords = [
		"typing",
		"type-checking",
	],
	license = "Apache2",
	name = "jk_typing",
	package_data = {
		"": [
		],
	},
	packages = [
		"jk_typing",
		"jk_typing.checking",
	],
	scripts = [
	],
	version = '0.2022.3.30',
	zip_safe = False,
	long_description = readme(),
	long_description_content_type = "text/markdown",
)

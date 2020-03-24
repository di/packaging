# Notes

## Tests
Run with `nox -s tests-3.8 -- tests/metadata`

Run a quick test with `python test.py`

## TODO
* Figure out how Multifield should be implemented
* Separate Metadatas, Fields and Validators
* Get stuff out of __init__.py
* Make utilities for is_valid_uri?
* Think about how warehouse can reuse is_valid_uri
* Check for 1:1 parity with the latest version of the metadata form
* Regex validator
* The email validator needs to use either:
  * a giant regex from a ~4 year old version of wtforms
  * the new email_validator library

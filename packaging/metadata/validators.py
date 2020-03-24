def is_valid_uri(
    uri, require_scheme=True, allowed_schemes={"http", "https"}, require_authority=True
):
    uri = uri_reference(uri).normalize()
    validator = validators.Validator().allow_schemes(*allowed_schemes)
    if require_scheme:
        validator.require_presence_of("scheme")
    if require_authority:
        validator.require_presence_of("host")

    validator.check_validity_of("scheme", "host", "port", "path", "query")

    try:
        validator.validate(uri)
    except exceptions.ValidationError:
        return False

    return True


class ValidationError(Exception):
    pass

class StopValidation(Exception):
    pass


class FieldValidator(object):
    def __init__(self, message=None):
        self.message = message

    def validate(self, field):
        raise NotImplementedError(self)


class Required(FieldValidator):
    def validate(self, field):
        if not field.data:  # TODO: handle only whitespace
            if self.message is None:
                raise StopValidation("This field is required.")
            else:
                raise StopValidation(self.message)


class AnyOf(FieldValidator):
    def __init__(self, possible_values, **kwargs):
        super(AnyOf, self).__init__(**kwargs)
        self.possible_values = possible_values

    def validate(self, field):
        if field.data not in self.possible_values:
            if self.message is None:
                raise StopValidation(
                    "Invalid value, must be one of: %s.".format(self.possible_values)
                )
            else:
                raise StopValidation(self.message)



class Regexp(FieldValidator):
    def __init__(self, regex, flags=None, **kwargs):
        super(Regexp, self).__init__(**kwargs)
        self.regex = regex
        self.flags = flags


class Optional(FieldValidator):
    def validate(self, field):
        if not field.data:
            raise StopValidation()


class RFC822Email(FieldValidator):
    def validate(self, field):
        return # TODO use https://pypi.org/p/email_validator
        addresses = email.utils.getaddresses([field.data])

        for real_name, address in addresses:
            email_validator(form, type("field", (), {"data": address}))


class Length(FieldValidator):
    def __init__(self, min=-1, max=-1, **kwargs):
        super(Length, self).__init__(**kwargs)
        self.min = min
        self.max = max


class URI(FieldValidator):
    def __init__(
        self,
        require_scheme=True,
        allowed_schemes={"http", "https"},
        require_authority=True,
        **kwargs
    ):
        super(URI, self).__init__(**kwargs)
        self.require_scheme = require_scheme
        self.allowed_schemes = allowed_schemes
        self.require_authority = require_authority

    def validate(self, field):
        if not is_valid_uri(
            field.data,
            require_authority=self.require_authority,
            allowed_schemes=self.allowed_schemes,
            require_scheme=self.require_scheme,
        ):
            raise ValidationError("Invalid URI")


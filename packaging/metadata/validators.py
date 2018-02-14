class FieldValidator:
    def __init__(self, message=None):
        self.message = message

    def validate(self):
        raise NotImplementedError


class Required(FieldValidator):
    pass


class AnyOf(FieldValidator):
    def __init__(self, values, **kwargs):
        super(AnyOf, self).__init__(**kwargs)
        self.values = values


class Regexp(FieldValidator):
    def __init__(self, regex, flags=None, **kwargs):
        super(Regexp, self).__init__(**kwargs)
        self.regex = regex
        self.flags = flags


class Optional(FieldValidator):
    pass


class RFC822Email(FieldValidator):
    pass


class Length(FieldValidator):
    def __init__(self, min=-1, max=-1, **kwargs):
        super(Length, self).__init__(**kwargs)
        self.min = min
        self.max = max


class URI(FieldValidator):
    pass

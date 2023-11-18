class ModificationError(Exception):
    """Caused by duplicate key value or Wrong type of expected value"""

    def __init__(self, value):
        self.value = value
        self.message = f"Caused by duplicate key value or Wrong type of expected value ----->{value}"
        super().__init__(self.message)


class OptionInvalidError(Exception):
    def __init__(self, opts: list[str]):
        options = "|".join(opts)
        self.message = f"Only available options are -->{options}"
        super().__init__(self.message)

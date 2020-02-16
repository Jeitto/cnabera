from collections import namedtuple
from datetime import datetime


def return_the_same_entry(value, **kwargs):
    return value


def complete_with_space_the_right(value, **kwargs):
    return str(value).ljust(kwargs['length'])


def complete_with_space_the_left(value, **kwargs):
    return str(value).rjust(kwargs['length'])


def complete_with_zero_the_left(value, **kwargs):
    return str(value).zfill(kwargs['length'])


def get_date_as_dd_mm_aa(date: datetime.date, **kwargs):
    return f'{date.day}{date.month}{str(date.year)[:2]}'


def get_string_space_by_length(value, **kwargs):
    return ' ' * kwargs['length']


def transform_float_to_int_with_zero_left(value, **kwargs):
    convert_result = int(value * 100)
    return complete_with_zero_the_left(convert_result, **kwargs)


Rules = namedtuple('Rules', 'position_init position_end length method_formatter')


class BaseFormatRules:
    """
    Example data:
        id_registry = Rules(0, 0, 1, return_the_same_entry)

    """
    ...


class FormatRulesHeaders(BaseFormatRules):
    ...


class FormatRulesTransaction(BaseFormatRules):
    ...


class FormatRulesFooter(BaseFormatRules):
    ...


class GenFile:
    LENGTH = 444
    formatter = FormatRulesHeaders

    def do_header(self, data):
        basestring = " " * self.LENGTH
        for key, value in data.items():
            rules = getattr(self.formatter, key)
            current_value = str(rules.method_formatter(value, **rules._asdict()))

            before_pointer_cut = basestring[:rules.position_init]
            after_pointer_cut = basestring[rules.position_end + 1:]

            basestring = f'{before_pointer_cut}{current_value}{after_pointer_cut}'
        return basestring

    def do_transaction(self, data):
        basestring = " " * self.LENGTH
        ...

    def do_footer(self, data):
        basestring = " " * self.LENGTH
        ...

    def execute(self, header_data, transaction_data):
        line_header = self.do_header(header_data)
        lines_transactions = self.do_transaction(transaction_data)
        line_footer = self.do_footer()
        return 'wip'

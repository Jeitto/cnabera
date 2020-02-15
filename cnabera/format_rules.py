from collections import namedtuple


Rules = namedtuple('Rules', 'position_init position_end length method_formatter')
class FormatRulesHeaders:
    """
    Example data:
        id_registry = Rules(0, 0, 1, return_the_same_entry)

    """
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

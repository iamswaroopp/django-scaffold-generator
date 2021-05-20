import re

from django.core.management.base import BaseCommand

from scaffold_generator.scaffold import ScaffoldGenerator

REFERENCE_REQUIRED_FIELDS = ('ForeignKey', 'OneToOneField', 'ManyToManyField')
BORDER_ARGS_REGEX = re.compile(r'^(?P<field_type>[A-Za-z0-9.]+)\((?P<field_args>.*)\)$')


class Command(BaseCommand):

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            'app_label',
            help='App label of an application to synchronize the state.',
        )
        parser.add_argument(
            'model_name',
            help='Model Name',
        )
        parser.add_argument('model_fields', nargs='+', help='Model Fields in format : fieldname[?]:fieldtype(args)')

    @staticmethod
    def parse_args(arg_string):
        field_name, field_type = arg_string.split(':')
        if field_name[-1] == '?':
            field_name = field_name[:-1]
            field_optional = True
        else:
            field_optional = False

        positional_args = []
        keyword_args = {}

        if BORDER_ARGS_REGEX.match(field_type):
            attrs = list(BORDER_ARGS_REGEX.finditer(field_type))[0]  # We are expecting only 1 group here.
            field_type = attrs['field_type']
            field_args = attrs['field_args']
            for arg in field_args.split(','):
                if '=' in arg:
                    key, value = arg.split('=')
                    keyword_args[key] = value
                elif arg:
                    positional_args.append(arg)
        if field_type in REFERENCE_REQUIRED_FIELDS and 'to' not in keyword_args and not positional_args:
            raise ValueError('Reference required for {}'.format(field_type))
        return {
            'name': field_name,
            'type': field_type,
            'optional': field_optional,
            'arguments': [positional_args, keyword_args],
        }

    def handle(self, *args, app_label, model_name, model_fields, **options):
        model_fields = [self.parse_args(args) for args in model_fields]
        import pprint
        pprint.pprint(model_name)
        scaffold_generator = ScaffoldGenerator(app_label, model_name, model_fields)
        scaffold_generator.generate()

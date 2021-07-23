import logging
import os
import re

from django.apps import apps
from django.template.loader import render_to_string

from .settings import ScaffoldGeneratorConfig
from .utils import FileTransaction

LOGGER = logging.getLogger(__name__)


def clean_model_fields(model_fields, scaffold_generator_settings):
    fields = []
    for model_field in model_fields:
        type = model_field['type']
        if type not in scaffold_generator_settings.FIELDS:
            raise ValueError('Unknown field type : {}'.format(type))
        field_config = scaffold_generator_settings.FIELDS[type]

        pos_args, kw_args = model_field['arguments']
        if field_config.get('default_kwargs'):
            kw_args = {**field_config['default_kwargs'], **kw_args}
        if model_field['optional']:
            kw_args['blank'] = 'True'
            if field_config.get('nullable', True):
                kw_args['null'] = 'True'
        fields.append(
            {
                'name': model_field['name'],
                'class_name': field_config['class_name'],
                'pos_args': pos_args,
                'kw_args': kw_args,
            }
        )
    return fields


class ScaffoldGenerator:

    def __init__(self, app_label, model_name, model_fields):
        config = ScaffoldGeneratorConfig()
        self.config = config
        self.app_label = app_label
        self.model_name = re.sub(r'\W+', '', model_name[0].upper() + model_name[1:])
        self.model_fields = clean_model_fields(model_fields, config)

    def get_context(self):
        return {
            'app_label': self.app_label,
            'model_name': self.model_name,
            'model_code': self.model_name.lower(),
            'model_fields': self.model_fields,
            'config': self.config,
        }

    def generate(self):
        app_path = apps.get_app_config(self.app_label).path
        context = self.get_context()
        LOGGER.debug('Using context : %s', context)
        with FileTransaction() as ft:
            with ft.open(
                path=os.path.join(app_path, 'urls.py'),
                mode='a',
                default_file_content=render_to_string('scaffolding/urls.py.default.template', context=context)
            ) as fp:
                fp.write(render_to_string('scaffolding/urls.py.template', context=context))
            with ft.open(path=os.path.join(app_path, 'models.py'), mode='a') as fp:
                fp.write(render_to_string('scaffolding/models.py.template', context=context))
            with ft.open(path=os.path.join(app_path, 'forms.py'), mode='a') as fp:
                fp.write(render_to_string('scaffolding/forms.py.template', context=context))
            with ft.open(path=os.path.join(app_path, 'views.py'), mode='a') as fp:
                fp.write(render_to_string('scaffolding/views.py.template', context=context))
            with ft.open(path=os.path.join(app_path, 'admin.py'), mode='a') as fp:
                fp.write(render_to_string('scaffolding/admin.py.template', context=context))
            import pprint
            pprint.pprint(context)
            if self.config['SCAFFOLD_REST_FRAMEWORK']:
                api_path = os.path.join(app_path, 'api')
                if not os.path.exists(api_path):
                    os.mkdir(api_path)
                    with ft.open(os.path.join(app_path,'__init__.py'), mode='w') as fp:
                        fp.write('')
                with ft.open(
                        path=os.path.join(api_path, 'urls.py'),
                        mode='r+',
                        default_file_content=render_to_string('scaffolding/api/urls.py.default.template', context=context)
                ) as fp:
                    buf = []
                    for line in fp.readlines():
                        if 'router.urls' in line:
                            buf.append(render_to_string('scaffolding/api/urls.py.template', context=context))
                        buf.append(line)
                    fp.seek(0)
                    fp.writelines(buf)
                with ft.open(path=os.path.join(api_path, 'serializers.py'), mode='a') as fp:
                    fp.write(render_to_string('scaffolding/api/serializers.py.template', context=context))
                with ft.open(path=os.path.join(api_path, 'views.py'), mode='a') as fp:
                    fp.write(render_to_string('scaffolding/api/views.py.template', context=context))
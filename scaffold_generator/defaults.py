DEFAULT_SETTINGS = {
    'CREATE_HTML_VIEW_RESOURCES': True,
    'CREATE_REST_VIEW_RESOURCES': True,
    'DEFAULT_MODEL_IMPORTS': [],
    'DEFAULT_FORM_IMPORTS': [
        'django.forms',
    ],
    'FIELDS': {},
    'MODEL_EXTRA_IMPORT_CLASSES': [
        'django.db.models',
    ],
    'MODEL_PARENT_CLASSES': ['django.db.models.Model'],
    'FORM_EXTRA_IMPORT_CLASSES': ['django.forms'],
    'FORM_PARENT_CLASSES': ['django.forms.ModelForm'],
    'VIEW_EXTRA_IMPORT_CLASSES': [],
    'VIEW_PERMISSION_CLASSES': [
        'django.contrib.auth.mixins.PermissionRequiredMixin',
    ],
    'VIEW_PERMISSION_CODES': [
        'view',
    ],
    'LIST_VIEW_PARENT_CLASSES': ['django.views.generic.list.ListView'],
    'DETAIL_VIEW_PARENT_CLASSES': ['django.views.generic.detail.DetailView'],
    'ADD_PERMISSION_CLASSES': [
        'django.contrib.auth.mixins.PermissionRequiredMixin',
    ],
    'ADD_PERMISSION_CODES': [
        'add',
    ],
    'CREATE_VIEW_PARENT_CLASSES': ['django.views.generic.edit.CreateView'],
    'CREATE_URL_PATH': 'create',
    'CHANGE_PERMISSION_CLASSES': [
        'django.contrib.auth.mixins.PermissionRequiredMixin',
    ],
    'CHANGE_PERMISSION_CODES': [
        'change',
    ],
    'UPDATE_VIEW_PARENT_CLASSES': ['django.views.generic.edit.UpdateView'],
    'UPDATE_URL_PATH': 'update',
    'DELETE_PERMISSION_CLASSES': [
        'django.contrib.auth.mixins.PermissionRequiredMixin',
    ],
    'DELETE_PERMISSION_CODES': [
        'delete',
    ],
    'DELETE_VIEW_PARENT_CLASSES': ['django.views.generic.edit.DeleteView'],
    'DELETE_URL_PATH': 'delete',
    'ADMIN_EXTRA_IMPORT_CLASSES': ['django.contrib.admin'],
    'ADMIN_PARENT_CLASSES': ['django.contrib.admin.ModelAdmin'],
    'URL_EXTRA_IMPORT_CLASSES': ['django.urls.path'],
}

DEFAULT_FIELDS = {
    'ForeignKey': {
        'class_name': 'models.ForeignKey',
        'default_kwargs': {
            'on_delete': 'models.CASCADE',
        }
    },
    'CharField': {
        'class_name': 'models.CharField',
        'default_kwargs': {
            'max_length': '128',
        },
        'nullable': False,
    },
    'TextField': {
        'class_name': 'models.TextField'
    }
}

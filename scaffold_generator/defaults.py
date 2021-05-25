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
    'AutoField': {
        'class_name': 'models.AutoField',
    },
    'BigAutoField': {
        'class_name': 'models.BigAutoField',
    },
    'BigIntegerField': {
        'class_name': 'models.BigIntegerField',
    },
    'BinaryField': {
        'class_name': 'models.BinaryField',
    },
    'BooleanField': {
        'class_name': 'models.BooleanField',
    },
    'CharField': {
        'class_name': 'models.CharField',
        'default_kwargs': {
            'max_length': '128',
        },
        'nullable': False,
    },
    'CommaSeparatedIntegerField': {
        'class_name': 'models.CommaSeparatedIntegerField',
        'nullable': False,
    },
    'DateField': {
        'class_name': 'models.DateField',
    },
    'DateTimeField': {
        'class_name': 'models.DateTimeField',
    },
    'DecimalField': {
        'class_name': 'models.DecimalField',
    },
    'DurationField': {
        'class_name': 'models.DurationField',
    },
    'EmailField': {
        'class_name': 'models.EmailField',
        'nullable': False,
    },
    'FileField': {
        'class_name': 'models.FileField',
        'nullable': False,
    },
    'FilePathField': {
        'class_name': 'models.FilePathField',
    },
    'FloatField': {
        'class_name': 'models.FloatField',
    },
    'ForeignKey': {
        'class_name': 'models.ForeignKey',
        'default_kwargs': {
            'on_delete': 'models.CASCADE',
        },
    },
    'GenericIPAddressField': {
        'class_name': 'models.GenericIPAddressField',
    },
    'IPAddressField': {
        'class_name': 'models.IPAddressField',
    },
    'ImageField': {
        'class_name': 'models.ImageField',
        'nullable': False,
    },
    'IntegerField': {
        'class_name': 'models.IntegerField',
    },
    'JSONField': {
        'class_name': 'models.JSONField',
    },
    'ManyToManyField': {
        'class_name': 'models.ManyToManyField',
        'nullable': False,
    },
    'NullBooleanField': {
        'class_name': 'models.NullBooleanField',
    },
    'OneToOneField': {
        'class_name': 'models.OneToOneField',
        'default_kwargs': {
            'on_delete': 'models.CASCADE',
        },
    },
    'PositiveBigIntegerField': {
        'class_name': 'models.PositiveBigIntegerField',
    },
    'PositiveIntegerField': {
        'class_name': 'models.PositiveIntegerField',
    },
    'PositiveSmallIntegerField': {
        'class_name': 'models.PositiveSmallIntegerField',
    },
    'SlugField': {
        'class_name': 'models.SlugField',
        'nullable': False,
    },
    'SmallAutoField': {
        'class_name': 'models.SmallAutoField',
    },
    'SmallIntegerField': {
        'class_name': 'models.SmallIntegerField',
    },
    'TextField': {
        'class_name': 'models.TextField',
        'nullable': False,
    },
    'TimeField': {
        'class_name': 'models.TimeField',
    },
    'URLField': {
        'class_name': 'models.URLField',
        'nullable': False,
    },
    'UUIDField': {
        'class_name': 'models.UUIDField',
    },
}

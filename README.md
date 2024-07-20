# Django Scaffold Generator

This projects aim to provide Ruby on Rails like scaffolding on Django framework.

### Usage

```

python manage.py generatescaffold <app_name> <ModelName> "<field1>:<Field1Type>" "<field2>:<Field2Type>"

```



### Example:

```

python manage.py generatescaffold test_app TestModel "name:CharField" "description:TextField"

```

### Supported Fields

Refer `scaffold_generator/defaults.py:DEFAULT_FIELDS`

### License

This project is licensed under the MIT License - see the [License File](License.txt) file for details

### Credits

- https://github.com/modocache/django-generate-scaffold
- https://github.com/tokyodevs/django3scaffold

import crispy_forms.helper


class FormHelper(crispy_forms.helper.FormHelper):
    render_hidden_fields = True
    render_required_fields = True
    render_unmentioned_fields = True
    html5_required = True

    def __init__(self, form=None, layout=None, **kwargs):
        super().__init__(form=form)
        if layout:
            self.layout = layout
        for k, v in kwargs.items():
            setattr(self, k, v)

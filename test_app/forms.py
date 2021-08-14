

from django import forms

from crispy_forms import layout

from crispy_forms.bootstrap import FormActions

from test_base.helpers import FormHelper


from django.forms import ModelForm

from .models import Blog
class BlogForm(ModelForm):
    helper = FormHelper(
        layout=layout.Layout(
            layout.Fieldset(
                'Blog Details',
                layout.Row(
                 layout.Column('name', css_class='col-lg-4'),
                 layout.Column('user', css_class='col-lg-4'),
                 layout.Column('amount', css_class='col-lg-4'),
                 layout.Column('description', css_class='col-lg-4'),
                
                ),
                layout.Row(
                    layout.Column(
                        FormActions(layout.Submit('submit', 'Save', css_class='btn btn-block')),
                        css_class='offset-lg-10 col-lg-2'
                    ),
                ),
            )
        )
    )

    class Meta:
        model = Blog
        fields = ['name' , 'user' , 'amount' , 'description'  ]



from django import forms

from crispy_forms import layout

from crispy_forms.bootstrap import FormActions

from test_base.helpers import FormHelper


from django.forms import ModelForm

from .models import Comment
class CommentForm(ModelForm):
    helper = FormHelper(
        layout=layout.Layout(
            layout.Fieldset(
                'Comment Details',
                layout.Row(
                 layout.Column('user', css_class='col-lg-4'),
                 layout.Column('blog', css_class='col-lg-4'),
                 layout.Column('date', css_class='col-lg-4'),
                 layout.Column('description', css_class='col-lg-4'),
                
                ),
                layout.Row(
                    layout.Column(
                        FormActions(layout.Submit('submit', 'Save', css_class='btn btn-block')),
                        css_class='offset-lg-10 col-lg-2'
                    ),
                ),
            )
        )
    )

    class Meta:
        model = Comment
        fields = ['user' , 'blog' , 'date' , 'description'  ]


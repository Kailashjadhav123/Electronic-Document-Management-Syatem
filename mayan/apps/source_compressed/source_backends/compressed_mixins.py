from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

from .literals import (
    SOURCE_UNCOMPRESS_CHOICE_ALWAYS, SOURCE_UNCOMPRESS_CHOICE_ASK,
    SOURCE_UNCOMPRESS_INTERACTIVE_CHOICES
)


class SourceBackendMixinCompressed:
    uncompress_choices = SOURCE_UNCOMPRESS_INTERACTIVE_CHOICES

    @classmethod
    def get_form_field_widgets(cls):
        widgets = super().get_form_field_widgets()

        widgets.update(
            {
                'uncompress': {
                    'class': 'django.forms.widgets.Select', 'kwargs': {
                        'attrs': {'class': 'select2'}
                    }
                }
            }
        )
        return widgets

    @classmethod
    def get_form_fields(cls):
        fields = super().get_form_fields()

        fields.update(
            {
                'uncompress': {
                    'label': _('Uncompress'),
                    'class': 'django.forms.ChoiceField',
                    'default': SOURCE_UNCOMPRESS_CHOICE_ASK,
                    'help_text': _(
                        'Whether to expand or not compressed archives.'
                    ),
                    'kwargs': {
                        'choices': cls.uncompress_choices
                    },
                    'required': True
                }
            }
        )

        return fields

    @classmethod
    def get_form_fieldsets(cls):
        fieldsets = super().get_form_fieldsets()

        fieldsets += (
            (
                _('Decompression'), {
                    'fields': ('uncompress',)
                },
            ),
        )

        return fieldsets

    @classmethod
    def get_upload_form_class(cls):
        class CompressedSourceUploadForm(
            super().get_upload_form_class()
        ):
            expand = forms.BooleanField(
                label=_('Expand compressed files'), required=False,
                help_text=ugettext(
                    'Upload a compressed file\'s contained files as '
                    'individual documents.'
                )
            )

            def __init__(self, *args, **kwargs):
                self.field_order = ['expand']
                super().__init__(*args, **kwargs)

        return CompressedSourceUploadForm

    def get_expand(self):
        if self.kwargs['uncompress'] == SOURCE_UNCOMPRESS_CHOICE_ASK:
            return self.process_kwargs['forms']['source_form'].cleaned_data.get('expand')
        else:
            if self.kwargs['uncompress'] == SOURCE_UNCOMPRESS_CHOICE_ALWAYS:
                return True
            else:
                return False

    def get_task_extra_kwargs(self):
        results = super().get_task_extra_kwargs()

        results.update(
            {
                'expand': self.get_expand()
            }
        )

        return results

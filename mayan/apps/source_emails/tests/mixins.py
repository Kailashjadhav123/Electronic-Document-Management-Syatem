from django.utils.encoding import force_text

from mayan.apps.credentials.tests.mixins import StoredCredentialPasswordUsernameTestMixin
from mayan.apps.source_compressed.source_backends.literals import SOURCE_UNCOMPRESS_CHOICE_NEVER
from mayan.apps.source_periodic.source_backends.literals import DEFAULT_PERIOD_INTERVAL
from mayan.apps.sources.tests.literals import (
    TEST_CASE_ACTION_NAME_SOURCE_CREATE, TEST_CASE_INTERFACE_NAME_VIEW
)
from mayan.apps.sources.tests.mixins.base_mixins import SourceTestMixin

from ..source_backends.literals import (
    DEFAULT_EMAIL_IMAP_MAILBOX, DEFAULT_EMAIL_IMAP_SEARCH_CRITERIA,
    DEFAULT_EMAIL_IMAP_STORE_COMMANDS, DEFAULT_EMAIL_POP3_TIMEOUT
)

from .literals import (
    TEST_EMAIL_ATTACHMENT_AND_INLINE, TEST_EMAIL_SOURCE_PASSWORD,
    TEST_EMAIL_SOURCE_USERNAME
)
from .source_backends import (
    SourceBackendTestEmail, SourceBackendTestIMAPEmail,
    SourceBackendTestPOP3Email
)


class CredentialSourceTestMixin(StoredCredentialPasswordUsernameTestMixin):
    _test_stored_credential_backend_data = {
        'password': TEST_EMAIL_SOURCE_PASSWORD,
        'username': TEST_EMAIL_SOURCE_USERNAME
    }


class EmailSourceTestMixin(SourceTestMixin, CredentialSourceTestMixin):
    _test_email_source_content = None
    _test_source_backend = SourceBackendTestEmail
    _test_source_content = TEST_EMAIL_ATTACHMENT_AND_INLINE

    def _get_test_source_backend_data(self, action_name, interface_name):
        result = super()._get_test_source_backend_data(
            action_name=action_name, interface_name=interface_name
        )

        result['_test_content'] = force_text(self._test_source_content)

        if action_name == TEST_CASE_ACTION_NAME_SOURCE_CREATE:
            result.update(
                {
                    'document_type_id': self._test_document_type.pk,
                    'host': '',
                    'interval': DEFAULT_PERIOD_INTERVAL,
                    'port': '',
                    'ssl': False,
                    'store_body': False,
                    'stored_credential_id': self._test_stored_credential.pk,
                    'uncompress': SOURCE_UNCOMPRESS_CHOICE_NEVER
                }
            )

            if interface_name == TEST_CASE_INTERFACE_NAME_VIEW:
                result.update(
                    {
                        'enabled': True,
                        'host': 'fake-host',
                        'port': 0,
                        'stored_credential_id': self._test_stored_credential.pk
                    }
                )

        return result


class IMAPEmailSourceTestMixin(EmailSourceTestMixin):
    _test_source_backend = SourceBackendTestIMAPEmail

    def _get_test_source_backend_data(self, action_name, interface_name):
        result = super()._get_test_source_backend_data(
            action_name=action_name, interface_name=interface_name
        )

        if action_name == TEST_CASE_ACTION_NAME_SOURCE_CREATE:
            result.update(
                {
                    'execute_expunge': True,
                    'mailbox': DEFAULT_EMAIL_IMAP_MAILBOX,
                    'mailbox_destination': '',
                    'port': 143,
                    'search_criteria': DEFAULT_EMAIL_IMAP_SEARCH_CRITERIA,
                    'store_commands': DEFAULT_EMAIL_IMAP_STORE_COMMANDS,
                }
            )

        return result


class POP3EmailSourceTestMixin(EmailSourceTestMixin):
    _test_source_backend = SourceBackendTestPOP3Email

    def _get_test_source_backend_data(self, action_name, interface_name):
        result = super()._get_test_source_backend_data(
            action_name=action_name, interface_name=interface_name
        )

        if action_name == TEST_CASE_ACTION_NAME_SOURCE_CREATE:
            result.update(
                {
                    'port': 110,
                    'timeout': DEFAULT_EMAIL_POP3_TIMEOUT,
                }
            )

        return result

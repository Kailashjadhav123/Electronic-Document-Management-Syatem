from mayan.apps.sources.permissions import permission_sources_edit

from mayan.apps.source_compressed.source_backend_actions.compressed_mixins import SourceBackendActionMixinCompressedNonInteractive
from mayan.apps.source_stored_files.source_backend_actions.file_mixins import SourceBackendActionMixinFileStoredNonInteractive
from mayan.apps.sources.source_backend_actions.base import SourceBackendAction
from mayan.apps.sources.source_backend_actions.mixins.callback_mixins import SourceBackendActionMixinCallbackPostDocumentUpload
from mayan.apps.sources.source_backend_actions.mixins.document_mixins import SourceBackendActionMixinDocumentUploadBase
from mayan.apps.sources.source_backend_actions.mixins.document_type_mixins import SourceBackendActionMixinDocumentTypeNonInteractive
from mayan.apps.sources.source_backend_actions.mixins.user_mixins import SourceBackendActionMixinUserInteractive

from .periodic_mixins import SourceBackendActionMixinPeriodic


class SourceBackendActionPeriodicDocumentUpload(
    SourceBackendActionMixinDocumentUploadBase,
    SourceBackendActionMixinDocumentTypeNonInteractive,
    SourceBackendActionMixinCompressedNonInteractive,
    SourceBackendActionMixinFileStoredNonInteractive,
    SourceBackendActionMixinUserInteractive,
    SourceBackendActionMixinPeriodic,
    SourceBackendActionMixinCallbackPostDocumentUpload,
    SourceBackendAction
):
    name = 'document_upload'
    permission = permission_sources_edit
    stored_file_identifier_name = 'encoded_filename'
    stored_method_name_file_cleanup = 'action_file_delete'
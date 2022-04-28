import operator

DEFAULT_RESULTS_LIMIT = 100
DEFAULT_SEARCH_BACKEND = 'mayan.apps.dynamic_search.backends.whoosh.WhooshSearchBackend'
DEFAULT_SEARCH_BACKEND_ARGUMENTS = {}
DEFAULT_SEARCH_DISABLE_SIMPLE_SEARCH = False
DEFAULT_SEARCH_INDEXING_CHUNK_SIZE = 25
DEFAULT_SEARCH_MATCH_ALL_DEFAULT_VALUE = 'false'
DEFAULT_SEARCH_RESULTS_LIMIT = 100

DEFAULT_SCOPE_ID = '0'

DELIMITER = '_'

MESSAGE_FEATURE_NO_STATUS = 'This backend does not provide status information.'

QUERY_PARAMETER_ANY_FIELD = 'q'

SEARCH_MODEL_NAME_KWARG = 'search_model_pk'

SCOPE_MARKER = '__'
SCOPE_MATCH_ALL = 'match_all'
SCOPE_OPERATOR_MARKER = 'operator'
SCOPE_RESULT_MAKER = 'result'

SCOPE_OPERATOR_AND = 'AND'
SCOPE_OPERATOR_OR = 'OR'
SCOPE_OPERATOR_NOT = 'NOT'

SCOPE_OPERATOR_CHOICES = {
    SCOPE_OPERATOR_AND: operator.and_,
    SCOPE_OPERATOR_OR: operator.or_,
    SCOPE_OPERATOR_NOT: operator.not_
}

TASK_DEINDEX_INSTANCE_MAX_RETRIES = 20
TASK_INDEX_INSTANCE_MAX_RETRIES = 20
TASK_INDEX_INSTANCES_MAX_RETRIES = 20

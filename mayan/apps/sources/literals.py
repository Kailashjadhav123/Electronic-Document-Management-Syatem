from django.utils.translation import ugettext_lazy as _

SOURCE_UNCOMPRESS_CHOICE_Y = 'y'
SOURCE_UNCOMPRESS_CHOICE_N = 'n'
SOURCE_UNCOMPRESS_CHOICE_ASK = 'a'

SOURCE_UNCOMPRESS_CHOICES = (
    (SOURCE_UNCOMPRESS_CHOICE_Y, _(u'Always')),
    (SOURCE_UNCOMPRESS_CHOICE_N, _(u'Never')),
)

SOURCE_INTERACTIVE_UNCOMPRESS_CHOICES = (
    (SOURCE_UNCOMPRESS_CHOICE_Y, _(u'Always')),
    (SOURCE_UNCOMPRESS_CHOICE_N, _(u'Never')),
    (SOURCE_UNCOMPRESS_CHOICE_ASK, _(u'Ask user'))
)

SOURCE_CHOICE_WEB_FORM = 'webform'
SOURCE_CHOICE_STAGING = 'staging'
SOURCE_CHOICE_WATCH = 'watch'
SOURCE_CHOICE_EMAIL_POP3 = 'pop3'
SOURCE_CHOICE_EMAIL_IMAP = 'imap'

SOURCE_CHOICES = (
    (SOURCE_CHOICE_WEB_FORM, _(u'Web form')),
    (SOURCE_CHOICE_STAGING, _(u'Server staging folder')),
    (SOURCE_CHOICE_WATCH, _(u'Server watch folder')),
    (SOURCE_CHOICE_EMAIL_POP3, _(u'POP3 email')),
    (SOURCE_CHOICE_EMAIL_IMAP, _(u'IMAP email')),
)

# TODO: remove PLURALS
SOURCE_CHOICES_PLURAL = (
    (SOURCE_CHOICE_WEB_FORM, _(u'Web forms')),
    (SOURCE_CHOICE_STAGING, _(u'Server staging folders')),
    (SOURCE_CHOICE_WATCH, _(u'Server watch folders')),
    (SOURCE_CHOICE_EMAIL_POP3, _(u'POP3 emails')),
    (SOURCE_CHOICE_EMAIL_IMAP, _(u'IMAP emails')),)

DEFAULT_INTERVAL = 60
DEFAULT_POP3_TIMEOUT = 60
DEFAULT_IMAP_MAILBOX = 'INBOX'

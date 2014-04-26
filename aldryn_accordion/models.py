from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


class Accordion(CMSPlugin):
    custom_classes = models.CharField(_('custom classes'), max_length=200, blank=True)
    index = models.PositiveIntegerField(_('index'), null=True, blank=True,
        help_text=_('index of element that should be opened on page load '
                    '(leave it empty if none of itemes should be opened), zero is the first item'))
    grouping = models.BooleanField(_('grouping'), default=True,
        help_text=_('only one can be opened at a time (true) or every '
                    'entry can be opened individually (false)'))

    def __unicode__(self):
        return _(u"%s items") % self.cmsplugin_set.all().count()


class AccordionItem(CMSPlugin):
    title = models.CharField(_('title'), max_length=255, null=True)
    custom_classes = models.CharField(_('custom classes'), max_length=200, blank=True)

    def __unicode__(self):
        return u"%s" % self.title

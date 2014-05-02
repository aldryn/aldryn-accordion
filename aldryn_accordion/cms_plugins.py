# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from aldryn_accordion.models import Accordion, AccordionItem
from aldryn_accordion.forms import AccordionPluginForm


class AccordionPlugin(CMSPluginBase):
    model = Accordion
    name = _('Accordion')
    module = _('Accordion')
    render_template = 'aldryn_accordion/accordion.html'
    allow_children = True
    child_classes = ['AccordionItemPlugin']
    form = AccordionPluginForm

    fieldsets = [
        # (None, {
        #     'fields': [],
        # }),
        (_('Advanced options'), {
            'classes': ('collapse', ),
            'fields': [
                'custom_classes',
                'index',
                'grouping',
            ],
        })
    ]

    def render(self, context, instance, placeholder):
        context.update({
            'accordion': instance,
            'accordion_id': "plugin-accordion-%s" % instance.pk,
            'placeholder': placeholder
        })
        return context


class AccordionItemPlugin(CMSPluginBase):
    model = AccordionItem
    name = _('Accordion item')
    module = _('Accordion')
    render_template = 'aldryn_accordion/accordion_item.html'
    allow_children = True
    fieldsets = [
        (None, {
            'fields': [
                'title',
            ],
        }),
        (_('Advanced options'), {
            'classes': ('collapse', ),
            'fields': [
                'custom_classes',
            ],
        })
    ]

    def render(self, context, instance, placeholder):
        context.update({
            'item': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(AccordionPlugin)
plugin_pool.register_plugin(AccordionItemPlugin)

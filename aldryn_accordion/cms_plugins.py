# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import Accordion, AccordionItem
from .forms import AccordionPluginForm


class AccordionPlugin(CMSPluginBase):
    model = Accordion
    name = _('Accordion')
    module = _('Accordion')
    render_template = 'aldryn_accordion/accordion.html'
    allow_children = True
    child_classes = ['AccordionItemPlugin']
    form = AccordionPluginForm

    fieldsets = [
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
        context = super(AccordionPlugin, self).render(context, instance, placeholder)
        context['accordion'] = instance
        context['accordion_id'] = "plugin-accordion-%s" % instance.pk
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
        context = super(AccordionItemPlugin, self).render(context, instance, placeholder)
        context['item'] = instance
        return context


plugin_pool.register_plugin(AccordionPlugin)
plugin_pool.register_plugin(AccordionItemPlugin)

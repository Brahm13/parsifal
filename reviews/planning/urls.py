# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('reviews.planning.views',
    url(r'^save_source/$', 'save_source', name='save_source'),
    url(r'^remove_source/$', 'remove_source_from_review', name='remove_source_from_review'),
    url(r'^suggested_sources/$', 'suggested_sources', name='suggested_sources'),
    url(r'^add_suggested_sources/$', 'add_suggested_sources', name='add_suggested_sources'),
    url(r'^save_question/$', 'save_question', name='save_question'),
    url(r'^add_question/$', 'add_question', name='add_question'),
    url(r'^remove_question/$', 'remove_question', name='remove_question'),
    url(r'^save_objective/$', 'save_objective', name='save_objective'),
    url(r'^add_criteria/$', 'add_criteria', name='add_criteria'),
    url(r'^remove_criteria/$', 'remove_criteria', name='remove_criteria'),
    url(r'^add_synonym/$', 'add_synonym', name='add_synonym'),
    url(r'^add_new_keyword/$', 'add_new_keyword', name='add_new_keyword'),
    url(r'^save_keyword/$', 'save_keyword', name='save_keyword'),
    url(r'^save_synonym/$', 'save_synonym', name='save_synonym'),
    url(r'^import_pico_keywords/$', 'import_pico_keywords', name='import_pico_keywords'),
    url(r'^remove_keyword/$', 'remove_keyword', name='remove_keyword'),
    url(r'^add_new_data_extraction_field/$', 'add_new_data_extraction_field', name='add_new_data_extraction_field'),
    url(r'^save_data_extraction_field/$', 'save_data_extraction_field', name='save_data_extraction_field'),
)
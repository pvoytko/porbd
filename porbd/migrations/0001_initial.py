# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'porbd_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('name_short', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('date_begin', self.gf('django.db.models.fields.DateField')()),
            ('date_end_plan', self.gf('django.db.models.fields.DateField')()),
            ('date_end_fact', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'porbd', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'porbd_project')


    models = {
        u'porbd.project': {
            'Meta': {'object_name': 'Project'},
            'date_begin': ('django.db.models.fields.DateField', [], {}),
            'date_end_fact': ('django.db.models.fields.DateField', [], {}),
            'date_end_plan': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name_short': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['porbd']
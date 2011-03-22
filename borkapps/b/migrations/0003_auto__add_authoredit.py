# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AuthorEdit'
        db.create_table('b_authoredit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['b.Author'])),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['a.Entry'])),
        ))
        db.send_create_signal('b', ['AuthorEdit'])


    def backwards(self, orm):
        
        # Deleting model 'AuthorEdit'
        db.delete_table('b_authoredit')


    models = {
        'a.blog': {
            'Meta': {'object_name': 'Blog'},
            'best_author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['b.Author']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'a.entry': {
            'Meta': {'object_name': 'Entry'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['a.Blog']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'b.author': {
            'Meta': {'object_name': 'Author'},
            'contributed_to': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['a.Blog']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'b.authoredit': {
            'Meta': {'object_name': 'AuthorEdit'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['b.Author']"}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['a.Entry']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['b']

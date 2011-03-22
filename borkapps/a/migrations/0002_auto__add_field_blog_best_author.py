# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Blog.best_author'
        db.add_column('a_blog', 'best_author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['b.Author'], null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Blog.best_author'
        db.delete_column('a_blog', 'best_author_id')


    models = {
        'a.blog': {
            'Meta': {'object_name': 'Blog'},
            'best_author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['b.Author']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'b.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['a']

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field contributed_to on 'Author'
        db.create_table('b_author_contributed_to', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('author', models.ForeignKey(orm['b.author'], null=False)),
            ('blog', models.ForeignKey(orm['a.blog'], null=False))
        ))
        db.create_unique('b_author_contributed_to', ['author_id', 'blog_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field contributed_to on 'Author'
        db.delete_table('b_author_contributed_to')


    models = {
        'a.blog': {
            'Meta': {'object_name': 'Blog'},
            'best_author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['b.Author']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'b.author': {
            'Meta': {'object_name': 'Author'},
            'contributed_to': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['a.Blog']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['b']

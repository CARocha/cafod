# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Documentos.tags'
        db.delete_column('foros_documentos', 'tags')

        # Adding field 'Documentos.tags_doc'
        db.add_column('foros_documentos', 'tags_doc',
                      self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True),
                      keep_default=False)

        # Deleting field 'Videos.tags'
        db.delete_column('foros_videos', 'tags')

        # Adding field 'Videos.tags_vid'
        db.add_column('foros_videos', 'tags_vid',
                      self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True),
                      keep_default=False)

        # Deleting field 'Audios.tags'
        db.delete_column('foros_audios', 'tags')

        # Adding field 'Audios.tags_aud'
        db.add_column('foros_audios', 'tags_aud',
                      self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True),
                      keep_default=False)

        # Deleting field 'Imagen.tags'
        db.delete_column('foros_imagen', 'tags')

        # Adding field 'Imagen.tags_img'
        db.add_column('foros_imagen', 'tags_img',
                      self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'Documentos.tags'
        db.add_column('foros_documentos', 'tags',
                      self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True),
                      keep_default=False)

        # Deleting field 'Documentos.tags_doc'
        db.delete_column('foros_documentos', 'tags_doc')

        # Adding field 'Videos.tags'
        db.add_column('foros_videos', 'tags',
                      self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True),
                      keep_default=False)

        # Deleting field 'Videos.tags_vid'
        db.delete_column('foros_videos', 'tags_vid')

        # Adding field 'Audios.tags'
        db.add_column('foros_audios', 'tags',
                      self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True),
                      keep_default=False)

        # Deleting field 'Audios.tags_aud'
        db.delete_column('foros_audios', 'tags_aud')

        # Adding field 'Imagen.tags'
        db.add_column('foros_imagen', 'tags',
                      self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True),
                      keep_default=False)

        # Deleting field 'Imagen.tags_img'
        db.delete_column('foros_imagen', 'tags_img')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'foros.aportes': {
            'Meta': {'object_name': 'Aportes'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 17, 0, 0)'}),
            'foro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foros.Foros']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'foros.audios': {
            'Meta': {'object_name': 'Audios'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_audio': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tags_aud': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'})
        },
        'foros.comentarios': {
            'Meta': {'object_name': 'Comentarios'},
            'aporte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foros.Aportes']"}),
            'comentario': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 17, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'foros.documentos': {
            'Meta': {'object_name': 'Documentos'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_doc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tags_doc': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'})
        },
        'foros.foros': {
            'Meta': {'object_name': 'Foros'},
            'apertura': ('django.db.models.fields.DateField', [], {}),
            'cierre': ('django.db.models.fields.DateField', [], {}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'creacion': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 17, 0, 0)'}),
            'fecha_skype': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memoria': ('django.db.models.fields.DateField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'foros.imagen': {
            'Meta': {'object_name': 'Imagen'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'foto': ('thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_img': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tags_img': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'})
        },
        'foros.videos': {
            'Meta': {'object_name': 'Videos'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_video': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tags_vid': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['foros']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Imagen'
        db.create_table('foros_imagen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('nombre_img', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('foto', self.gf('thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('tags', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
        ))
        db.send_create_signal('foros', ['Imagen'])

        # Adding model 'Documentos'
        db.create_table('foros_documentos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('nombre_doc', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tags', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
        ))
        db.send_create_signal('foros', ['Documentos'])

        # Adding model 'Videos'
        db.create_table('foros_videos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('nombre_video', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('tags', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
        ))
        db.send_create_signal('foros', ['Videos'])

        # Adding model 'Audios'
        db.create_table('foros_audios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('nombre_audio', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tags', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
        ))
        db.send_create_signal('foros', ['Audios'])

        # Adding model 'Foros'
        db.create_table('foros_foros', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('creacion', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 4, 12, 0, 0))),
            ('apertura', self.gf('django.db.models.fields.DateField')()),
            ('cierre', self.gf('django.db.models.fields.DateField')()),
            ('fecha_skype', self.gf('django.db.models.fields.DateField')()),
            ('memoria', self.gf('django.db.models.fields.DateField')()),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('contraparte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('foros', ['Foros'])

        # Adding model 'Aportes'
        db.create_table('foros_aportes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foros.Foros'])),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 4, 12, 0, 0))),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('foros', ['Aportes'])

        # Adding model 'Comentarios'
        db.create_table('foros_comentarios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 4, 12, 0, 0))),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('comentario', self.gf('django.db.models.fields.TextField')()),
            ('aporte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foros.Aportes'])),
        ))
        db.send_create_signal('foros', ['Comentarios'])

    def backwards(self, orm):
        # Deleting model 'Imagen'
        db.delete_table('foros_imagen')

        # Deleting model 'Documentos'
        db.delete_table('foros_documentos')

        # Deleting model 'Videos'
        db.delete_table('foros_videos')

        # Deleting model 'Audios'
        db.delete_table('foros_audios')

        # Deleting model 'Foros'
        db.delete_table('foros_foros')

        # Deleting model 'Aportes'
        db.delete_table('foros_aportes')

        # Deleting model 'Comentarios'
        db.delete_table('foros_comentarios')

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
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 12, 0, 0)'}),
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
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'})
        },
        'foros.comentarios': {
            'Meta': {'object_name': 'Comentarios'},
            'aporte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foros.Aportes']"}),
            'comentario': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 12, 0, 0)'}),
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
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'})
        },
        'foros.foros': {
            'Meta': {'object_name': 'Foros'},
            'apertura': ('django.db.models.fields.DateField', [], {}),
            'cierre': ('django.db.models.fields.DateField', [], {}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'creacion': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 12, 0, 0)'}),
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
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'})
        },
        'foros.videos': {
            'Meta': {'object_name': 'Videos'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_video': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['foros']
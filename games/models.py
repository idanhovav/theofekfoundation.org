from django.db import models
from django.db.models.fields import CharField, IntegerField, DecimalField, NullBooleanField

class GameSettings(models.Model):
	user_id = IntegerField()
	game_name = CharField(max_length=128)
	ai_turn = CharField(max_length=10)
	monte_carlo_trials = IntegerField(null=True)
	expansion_constant = DecimalField(decimal_places=10, max_digits=12, null=True)
	certainty_threshold = DecimalField(decimal_places=3, max_digits=5, null=True)
	time_to_think = DecimalField(decimal_places=4, max_digits=6, null=True)
	anti = NullBooleanField()
	ponder = NullBooleanField()
	smart_simulation = NullBooleanField()

	class Meta:
		unique_together = ('id', 'game_name')

	def get_settings(self):
		settings = {}
		for field in GameSettings._meta.fields:
			key = field.name
			val = field.value_to_string(self)
			if not (val is None) and not (val == 'None') and not (val == ''):
				settings[key] = val
		print settings
		return settings

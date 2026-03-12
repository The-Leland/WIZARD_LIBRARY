


from db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class WizardSpecialization(db.Model):
    __tablename__ = 'wizard_specializations'

    wizard_id = db.Column(UUID(as_uuid=True), db.ForeignKey('wizards.wizard_id'), primary_key=True)
    spell_id = db.Column(UUID(as_uuid=True), db.ForeignKey('spells.spell_id'), primary_key=True)
    proficiency_level = db.Column(db.Float)
    date_learned = db.Column(db.DateTime)

    wizard = db.relationship('Wizard', back_populates='specializations')
    spell = db.relationship('Spell', back_populates='specializations')

    def __init__(self, wizard_id, spell_id, proficiency_level, date_learned):
        self.wizard_id = wizard_id
        self.spell_id = spell_id
        self.proficiency_level = proficiency_level
        self.date_learned = date_learned
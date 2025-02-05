# In the BotConfig model
from utils.db import db

class BotConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    connection_id = db.Column(db.Integer, db.ForeignKey('connection.id'), nullable=False)  # Correct the table name here
    mail = db.Column(db.String(120), nullable=False)
    Inventory_Api_url = db.Column(db.String(255), nullable=False)
    method = db.Column(db.String(10), nullable=False)
    origin_folder = db.Column(db.String(255), nullable=False)
    headers = db.Column(db.JSON, nullable=False)
    destination_folder = db.Column(db.String(255), nullable=False)
    error_folder = db.Column(db.String(255), nullable=False)
    success_email_subjects = db.Column(db.String(255), nullable=True)
    success_email_content = db.Column(db.Text, nullable=True)
    error_email_subject = db.Column(db.String(255), nullable=True)
    error_email_Body = db.Column(db.Text, nullable=True)
    sample_json = db.Column(db.JSON, nullable=False)
    orchestrator_bot_id = db.Column(db.String(255), nullable=False)

    # Define the relationship with Connection using back_populates
    connection = db.relationship('Connection', back_populates='bot_configs')

    def __repr__(self):
        return f'<BotConfig {self.Inventory_Api_url}>'
from utils.db import db

class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    oauth_token = db.Column(db.String(512), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    company = db.relationship('Company', back_populates='Connections')

    # Define the relationship with BotConfig using back_populates
    bot_configs = db.relationship('BotConfig', back_populates='connection', lazy=True)

    def __repr__(self):
        return f"<Connection(id={self.id}, name='{self.name}', company_id={self.company_id}, email='{self.email}', oauth_token='{self.oauth_token}', created_at={self.created_at}, updated_at={self.updated_at})>"

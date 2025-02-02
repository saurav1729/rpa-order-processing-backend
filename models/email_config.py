from utils.db import db

class EmailConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subdomain_id = db.Column(db.Integer, db.ForeignKey('subdomain.id'), nullable=False)
    mail = db.Column(db.String(120), nullable=False)
    order_creation_url = db.Column(db.String(255), nullable=False)
    method = db.Column(db.String(10), nullable=False)
    origin_folder = db.Column(db.String(255), nullable=False)
    headers = db.Column(db.JSON, nullable=False)
    destination_folder = db.Column(db.String(255), nullable=False)
    error_folder = db.Column(db.String(255), nullable=False)
    success_email_recipients = db.Column(db.String(255), nullable=True)
    success_email_content = db.Column(db.Text, nullable=True)
    error_email_recipients = db.Column(db.String(255), nullable=True)
    error_email_content = db.Column(db.Text, nullable=True)
    
    subdomain = db.relationship('Subdomain', backref=db.backref('email_configs', lazy=True))

    def __repr__(self):
        return f'<EmailConfig {self.order_creation_url}>'

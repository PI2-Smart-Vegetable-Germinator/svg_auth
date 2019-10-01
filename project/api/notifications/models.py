from project import db


class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    irrigation_notifications_enabled = db.Column(db.Boolean)
    humidity_notifications_enabled = db.Column(db.Boolean)
    illumination_notifications_enabled = db.Column(db.Boolean)
    harvest_notifications_enabled = db.Column(db.Boolean)

    user = db.relationship("Users", back_populates="notifications_config")

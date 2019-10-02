from project import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    device_id = db.Column(db.String(200))
    machine_id = db.Column(db.Integer)

    notifications_id = db.Column(db.Integer, db.ForeignKey('notifications.id'))
    notifications_config = db.relationship(
        "Notifications",
        cascade="all, delete",
        uselist=False,
        back_populates="user"
    )

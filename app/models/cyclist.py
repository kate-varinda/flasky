from app import db

class Cyclist(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    bikes = db.relationship("Bike", back_populates="cyclist")


    def to_dict(self):
        bike_dict = {
            "id": self.id,
            "name": self. name,
        }
        return bike_dict
    
    @classmethod
    def from_dict(cls, data_dict):
        new_obj = cls(name=data_dict["name"])

        return new_obj


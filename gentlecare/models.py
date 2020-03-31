from gentlecare import app, db


class Service(db.Model):
    IdService = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(250), nullable=False)
    Price = db.Column(db.String(250), nullable=False)
    Enabled = db.Column(db.Integer, db.ForeignKey('situation.IdSituation'))
    CreatedAt = db.Column(db.DateTime, nullable=False) 
    situation = db.relationship('Situation', backref='Service')


    def __repr__(self) :
        return f"Service('{self.IdService}','{self.Name},'{self.Price}','{self.Enabled}','{self.CreatedAt}')"

class ExtraService(db.Model):
    IdService = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(250), nullable=False)
    Price = db.Column(db.String(250), nullable=False)
    Enabled = db.Column(db.Integer, db.ForeignKey('situation.IdSituation'))
    CreatedAt = db.Column(db.DateTime, nullable=False) 
    situation = db.relationship('Situation', backref='ExtraService')


    def __repr__(self) :
        return f"ExtraService('{self.IdService}','{self.Name},'{self.Price}','{self.Enabled}','{self.CreatedAt}')"

class Farmer(db.Model):
    Idfarmer = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(250), nullable=True)
    LastName = db.Column(db.String(250), nullable=True)
    PhoneNumber = db.Column(db.String(250), nullable=True)
    Address = db.Column(db.String(250), nullable=True)
    # IdCrop = db.Column(db.Integer , db.ForeignKey('crop.IdCrop'))
    Harvestime = db.Column(db.String(250), nullable=True)
    CreatedAt = db.Column(db.DateTime, nullable=False) 

    def __repr__(self) :
        return f"Farmer('{self.Idfarmer}',{self.FirstName}','{self.LastName}','{self.PhoneNumber}','{self.Address}','{self.Harvestime}','{self.CreatedAt}')"        



class Business(db.Model):
    IdBusines = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(250), nullable=True)
    LastName = db.Column(db.String(250), nullable=True)
    Email = db.Column(db.String(250), nullable=True)
    PhoneNumber = db.Column(db.String(250), nullable=True)
    Address = db.Column(db.String(250), nullable=True)
    BusinesName = db.Column(db.String(250), nullable=True)
    CreatedAt = db.Column(db.DateTime, nullable=False) 

    def __repr__(self) :
        return f"Business('{self.IdBusines}',{self.FirstName}','{self.LastName}','{self.Email}','{self.PhoneNumber}','{self.Address}','{self.BusinesName}','{self.CreatedAt}')"        

class Price(db.Model):
    IdPrice = db.Column(db.Integer, primary_key=True)
    # IdCrop = db.Column(db.Integer, db.ForeignKey('crop.IdCrop'))
    IdService = db.Column(db.Integer, db.ForeignKey('Service.IdService'))
    IdQty = db.Column(db.Integer, db.ForeignKey('quantity.IdQty'))
    IdUser  = db.Column(db.Integer, db.ForeignKey('users.IdUser'))
    Price  = db.Column(db.String(250), nullable=True)
    CreatedAt = db.Column(db.DateTime, nullable=False)
    # crop = db.relationship("Crop", backref="Price") 
    # Service = db.relationship("Service", backref="Price")
    # qty = db.relationship("Quantity", backref="Price")


    def __repr__(self) :
        return f"Price('{self.IdPrice}',{self.IdCrop}','{self.IdService}','{self.IdQty}','{self.IdUser}','{self.Price}','{self.CreatedAt}')"        


class Situation(db.Model):
    IdSituation = db.Column(db.Integer, primary_key=True)
    Situation  = db.Column(db.String(250), nullable=False)
    CreatedAt  = db.Column(db.DateTime, nullable=False) 

    def __repr__(self) :
        return f"Situation('{self.IdSituation}','{self.Situation}','{self.CreatedAt}')"

class Priority(db.Model):
    IdPriority = db.Column(db.Integer, primary_key=True)
    PriorityName  = db.Column(db.String(250), nullable=False)
    CreatedAt  = db.Column(db.DateTime, nullable=False) 

    def __repr__(self) :
        return f"Priority('{self.IdPriority}','{self.PriorityName}','{self.CreatedAt}')"


class OrdersMaintenance(db.Model):
    IdOrder = db.Column(db.Integer, primary_key=True)
    OrderNumber = db.Column(db.String(250), nullable=True)
    FirstName  = db.Column(db.String(250), nullable=True)
    LastName   = db.Column(db.String(250), nullable=True)
    PhoneNumber = db.Column(db.String(250), nullable=True)
    Email = db.Column(db.String(250), nullable=True)
    Address  = db.Column(db.String(250), nullable=True)
    IdService  = db.Column(db.Integer, db.ForeignKey('service.IdService'))
    Price  = db.Column(db.String(250), nullable=True)
    IdPriority  = db.Column(db.Integer, db.ForeignKey('priority.IdPriority'))
    IdOrderStatus  = db.Column(db.Integer, db.ForeignKey('order_status.IdOrderStatus'))
    Ordertime = db.Column(db.String(250), nullable=True) 
    Time = db.Column(db.String(250), nullable=True) 
    Comment = db.Column(db.String(250), nullable=True) 
    CreatedAt = db.Column(db.DateTime, nullable=False)

    service = db.relationship("Service", backref="OrdersMaintenance")
    priority = db.relationship("Priority", backref="OrdersMaintenance") 

    def __repr__(self) :
        return f"OrdersMaintenance('{self.IdOrder}',{self.OrderNumber}','{self.FirstName}','{self.LastName}','{self.PhoneNumber}','{self.Email}','{self.IdService}','{self.Price}','{self.IdPriority}','{self.IdOrderStatus}','{self.Ordertime}','{self.Time}','{self.Comment}')"        

class OrderStatus(db.Model):
    IdOrderStatus = db.Column(db.Integer, primary_key=True)
    OrderStatus  = db.Column(db.String(250), nullable=False)
    CreatedAt  = db.Column(db.DateTime, nullable=False) 

    def __repr__(self) :
        return f"OrderStatus('{self.IdOrderStatus}','{self.OrderStatus}','{self.CreatedAt}')"



from prueba.config2 import Base, engine
import sqlalchemy as sa


class Sale(Base):
    __tablename__ = 'sale_history'
    order_id = sa.Column(sa.Integer, primary_key=True)
    customer_id = sa.Column(sa.Integer)
    item_id = sa.Column(sa.Integer)       # foreign key with product list
    cartFinalize_dateTime = sa.Column(sa.DATETIME)
    amount_ordrered = sa.Column(sa.Integer)
    city_name = sa.Column(sa.String(191))
    quantity_ordered = sa.Column(sa.Integer)

    def __repr__(self):
        return "<Sale(city_name='%s')>" % (self.city_name)


Base.metadata.create_all(engine)
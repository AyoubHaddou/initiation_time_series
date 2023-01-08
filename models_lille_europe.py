from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, DateTime 
from sqlalchemy.orm import sessionmaker
import datetime 
import json 
import requests 

engine = create_engine("sqlite:///lost_objects.db")
Base = declarative_base()

class LostObject(Base):
    __tablename__ = "LostObject"
    id = Column(String(), primary_key=True)
    date = Column(DateTime(), nullable=False)
    type = Column(String(length=90), nullable=False)
    nature = Column(String(length=90), nullable=False)

def conn():
    DatabaseSession = sessionmaker(bind=engine) 
    database = DatabaseSession()
    return database 

def create_db():
    db = conn()
    for year in range(2016, 2024):
        response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&q=&rows=-1&sort=date&facet=date&facet=gc_obo_date_heure_restitution_c&facet=gc_obo_gare_origine_r_name&facet=gc_obo_nature_c&facet=gc_obo_type_c&facet=gc_obo_nom_recordtype_sc_c&refine.gc_obo_gare_origine_r_name=Lille+Europe&refine.date={year}")
        data = json.loads(response.text)
        for item in data["records"]:
            date_found = datetime.datetime.strptime(item["fields"]["date"], "%Y-%m-%dT%H:%M:%S+00:00")
            record = LostObject(
                id=item["recordid"], 
                date=date_found,
                type=item["fields"]["gc_obo_type_c"],
                nature=item["fields"]["gc_obo_nature_c"],
            )
            db.add(record)
    db.commit()
    db.close()
    
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    create_db()
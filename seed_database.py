import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb trip_itinerary')
os.system('createdb trip_itinerary')

model.connect_to_db(server.app)
model.db.create_all()


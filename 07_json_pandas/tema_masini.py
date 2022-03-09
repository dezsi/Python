import json
import pandas as pd



data = {
  "id": {
    "id": 1,2
  },
  "brand": {
    "bmw": 1,
    "audi": 2
  },
  "model": {
    "bmw": "seria 1",
    "audi": "TT"
  },
  "hp": {
        "slow_cars": "< 120",
        "fast_cars": "≥ 120, dar < 180",
        "sport_cars": ">=180"
  },
  "price": {
        "cheap": "< 1000",
        "medium": " ≥ 1000, dar < 5000",
        "expensive": " ≥ 5000"

  },


variabila1 = pd.DataFrame(data)
fisier = variabila1.to_csv("data.cs")

pritn("hello")
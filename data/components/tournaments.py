from .prizes import BiggestFish, BiggestTotal, BiggestSpecies, BiggestTotalSpecies



# 8 hours = 4 minutes = 14400
# 6 hours = 3 minutes = 10800
# 4 hours = 2 minutes = 7200
# 2 hours = 1 minute = 3600


TOURNAMENTS = [
        {"name": "Crappie Lake Crappie-Off",
          "num_competitors": 50,
          "catch_limits": [("Black Crappie", 10), ("White Crappie", 10), ("Yellow Perch", 10),
                                 ("White Perch", 10), ("Pickerel", 10), ("Bass", 3),
                                 ("Brook Trout", 0), ("Salmon", 0), ("Lake Trout", 0), ("Pike", 0)],
          "fish_mins": [("Black Crappie", 4), ("White Crappie", 4), ("Yellow Perch", 3),
                                 ("White Perch", 3), ("Pickerel", 2), ("Bass", 2),
                                 ("Brook Trout", 1), ("Salmon", 1), ("Lake Trout", 1), ("Pike", 1)],                                  
          "sturgeons": [(-1, 1.2, 200)],
          "prizes": [BiggestTotal([100, 50, 25]), BiggestSpecies("Black Crappie", [50, 25, 10]),
                         BiggestSpecies("White Crappie", [50, 25, 10]), 
                         BiggestTotalSpecies("Black Crappie", [100, 50, 25]), 
                         BiggestTotalSpecies("White Crappie", [100, 50, 25])],
                         
          "entry_fee": 15,
          "time_limit": 10800
        },
        {"name": "Crystal Lake Open",
          "num_competitors": 40,
          "catch_limits": [("Black Crappie", 5), ("White Crappie", 5), ("Yellow Perch", 0),
                                 ("White Perch", 5), ("Pickerel", 5), ("Bass", 3),
                                 ("Brook Trout", 3), ("Salmon", 2), ("Lake Trout", 2), ("Pike", 2)],
          "fish_mins": [("Black Crappie", 3), ("White Crappie", 2), ("Yellow Perch", 3),
                                 ("White Perch", 2), ("Pickerel", 2), ("Bass", 2),
                                 ("Brook Trout", 4), ("Salmon", 4), ("Lake Trout", 2), ("Pike", 1)],                                  
          "sturgeons": [(-1, 1.2, 200)],
          "prizes": [BiggestFish([250, 100, 50, 25, 10]), BiggestTotal([100, 50, 25]),
                         BiggestSpecies("Salmon", [500, 250, 100]), BiggestSpecies("Brook Trout", [500, 250, 100]),
                         BiggestSpecies("Pickerel", [10])],
                         
          "entry_fee": 15,
          "time_limit":  14400
        },
        {"name": "Perch Pond Panfish Derby",
          "num_competitors": 50,
          "catch_limits": [("Black Crappie", 10), ("White Crappie", 10), ("Yellow Perch", 10),
                                 ("White Perch", 10), ("Pickerel", 10), ("Bass", 10),
                                 ("Brook Trout", 0), ("Salmon", 0), ("Lake Trout", 0), ("Pike", 0)],
          "fish_mins": [("Black Crappie", 4), ("White Crappie", 4), ("Yellow Perch", 3),
                                 ("White Perch", 3), ("Pickerel", 2), ("Bass", 2),
                                 ("Brook Trout", 2), ("Salmon", 1), ("Lake Trout", 1), ("Pike", 1)],                                  
          "sturgeons": [(-1, 1.2, 500)],
          "prizes": [BiggestTotal([500, 250, 100, 50]), 
                         BiggestSpecies("Black Crappie", [250, 100, 50, 25]),
                         BiggestSpecies("White Crappie", [250, 100, 50, 25]), 
                         BiggestSpecies("Yellow Perch", [250, 100, 50, 25]),
                         BiggestSpecies("White Perch", [250, 100, 50, 25])],
                         
          "entry_fee": 15,
          "time_limit": 14400
       },
        
        {"name": "Rotary International Pro-Am",
          "num_competitors": 100,
          "catch_limits": [("Black Crappie", 10), ("White Crappie", 10), ("Yellow Perch", 10),
                                 ("White Perch", 10), ("Pickerel", 10), ("Bass", 10),
                                 ("Brook Trout", 2), ("Salmon", 2), ("Lake Trout", 2), ("Pike", 2)],
          "fish_mins": [("Black Crappie", 4), ("White Crappie", 4), ("Yellow Perch", 3),
                                 ("White Perch", 3), ("Pickerel", 2), ("Bass", 2),
                                 ("Brook Trout", 2), ("Salmon", 1), ("Lake Trout", 1), ("Pike", 1)],                                  
          "sturgeons": [(-1, 1.2, 200)],
          "prizes": [BiggestSpecies("Pike", [1000, 500, 250]),
                         BiggestSpecies("Lake Trout", [1000, 500, 250]),
                         BiggestSpecies("Salmon", [1000, 500, 250]),
                         BiggestSpecies("Brook Trout", [1000, 500, 250]),
                         BiggestSpecies("Bass", [1000, 500, 250]),
                         BiggestSpecies("Pickerel", [500, 250, 100])],
                         
          "entry_fee": 15,
          "time_limit": 14400
       },
        {"name": "Winter Bass Classic",
          "num_competitors": 50,
          "catch_limits": [("Black Crappie", 0), ("White Crappie", 0), ("Yellow Perch", 0),
                                 ("White Perch", 0), ("Pickerel", 3), ("Bass", 10),
                                 ("Brook Trout", 0), ("Salmon", 0), ("Lake Trout", 0), ("Pike", 0)],
          "fish_mins": [("Black Crappie", 4), ("White Crappie", 4), ("Yellow Perch", 3),
                                 ("White Perch", 3), ("Pickerel", 2), ("Bass", 4),
                                 ("Brook Trout", 2), ("Salmon", 1), ("Lake Trout", 1), ("Pike", 1)],                                  
          "sturgeons": [(-1, 1.2, 300)],
          "prizes": [BiggestSpecies("Bass", [1000, 500, 250, 100]),
                         BiggestTotalSpecies("Bass", [500, 250, 100]),
                         BiggestSpecies("Pickerel", [100, 50, 25, 10])],
                         
          "entry_fee": 15,
          "time_limit": 14400
        },
        
        {"name": "Great North Trout Derby",
          "num_competitors": 50,
          "catch_limits": [("Black Crappie", 0), ("White Crappie", 0), ("Yellow Perch", 0),
                                 ("White Perch", 0), ("Pickerel", 0), ("Bass", 0),
                                 ("Brook Trout", 5), ("Salmon", 0), ("Lake Trout", 5), ("Pike", 0)],
          "fish_mins": [("Black Crappie", 4), ("White Crappie", 4), ("Yellow Perch", 3),
                              ("White Perch", 3), ("Pickerel", 2), ("Bass", 2),
                              ("Brook Trout", 4), ("Salmon", 2), ("Lake Trout", 3), ("Pike", 2)],
          "sturgeons": [(-1, 1.2, 250)],
          "prizes": [BiggestTotal([1000, 500, 250, 100]), 
                         BiggestSpecies("Brook Trout", [500, 300, 200, 100, 50]),
                         BiggestSpecies("Lake Trout", [500, 300, 200, 100, 50])],
          "entry_fee": 20,
          "time_limit": 10800
        },
        {"name": "Polar Pro-Am",
          "num_competitors": 100,
          "catch_limits": [("Black Crappie", 5), ("White Crappie", 5), ("Yellow Perch", 5),
                                 ("White Perch", 5), ("Pickerel", 3), ("Bass", 3),
                                 ("Brook Trout", 2), ("Salmon", 2), ("Lake Trout", 2), ("Pike", 3)],
          "fish_mins": [("Black Crappie", 4), ("White Crappie", 4), ("Yellow Perch", 4),
                                 ("White Perch", 4), ("Pickerel", 3), ("Bass", 2),
                                 ("Brook Trout", 3), ("Salmon", 2), ("Lake Trout", 2), ("Pike", 2)],                                  
          "sturgeons": [(-1, 1.2, 200), (1, 1.3, 400)],
          "prizes": [BiggestFish([2500, 1000, 500, 250, 100]), BiggestTotal([2500, 1000, 500, 250, 100])],
                         
          "entry_fee": 15,
          "time_limit": 14400
        },
        {"name": "Brewers Assoc. $100,000 Classic",
          "num_competitors": 100,
          "catch_limits": [("Black Crappie", 5), ("White Crappie", 5), ("Yellow Perch", 5),
                                 ("White Perch", 5), ("Pickerel", 3), ("Bass", 3),
                                 ("Brook Trout", 3), ("Salmon", 2), ("Lake Trout", 2), ("Pike", 1)],
          "fish_mins": [("Black Crappie", 4), ("White Crappie", 4), ("Yellow Perch", 4),
                                 ("White Perch", 4), ("Pickerel", 3), ("Bass", 3),
                                 ("Brook Trout", 3), ("Salmon", 2), ("Lake Trout", 2), ("Pike", 2)],                                  
          "sturgeons": [(-1, 1.2, 200), (1, 1.3, 400)],
          "prizes": [BiggestTotal([20000]),
                         BiggestSpecies("Pike", [10000]),
                         BiggestSpecies("Lake Trout", [10000]),
                         BiggestSpecies("Salmon", [10000]),
                         BiggestSpecies("Brook Trout", [10000]),
                         BiggestSpecies("Bass", [10000]),
                         BiggestSpecies("Pickerel", [10000]),
                         BiggestSpecies("Black Crappie", [5000]),
                         BiggestSpecies("White Crappie", [5000]),
                         BiggestSpecies("Yellow Perch", [5000]),
                         BiggestSpecies("White Perch", [5000])],
                         
          "entry_fee": 15,
          "time_limit": 21600
        }
    ]              
                  
                  

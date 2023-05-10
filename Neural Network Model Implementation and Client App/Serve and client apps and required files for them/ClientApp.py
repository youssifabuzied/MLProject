import tkinter
from tkinter import ttk
import requests
import pandas as pd
import urllib.parse
import numpy as np
import math
import warnings
import json

warnings.filterwarnings("ignore")
from tkinter import messagebox
import tkinter as tk
window = tkinter.Tk()
# window.configure(bg="#D8BFD8")
window.title("Data Entry Form")
# Set the window size
window.geometry("2000x2000")
frame = tkinter.Frame(window)
frame.pack()
city =""
df = pd.read_csv("PreProcessing.csv")
data = pd.read_csv("Cols.csv")
data = data.loc[:,~data.columns.str.match("Unnamed: 0")]
inFrame = pd.DataFrame()
def relu(x):
    """
    Computes the element-wise ReLU (rectified linear unit) function on a NumPy array.
    """
    return np.maximum(0, x)
def enter_data():
    # Course info

    # 1. Body Type
    lis = df["body_type"].unique()
    body_type = body_type_entry.get()
    new_cols = {}
    for val in lis:
        new_cols[val] = []
    target_col = body_type
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 2. Back legroom
    back_legroom = float(back_legroom_entry.get())
    des = df.describe()["back_legroom"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["back_legroom"] = [(back_legroom - m) / std]
    inFrame["back_legroom"] = dic["back_legroom"]
    print(inFrame)
    # 3. Front Legroom
    front_legroom = float(front_legroom_entry.get())
    des = df.describe()["front_legroom"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["front_legroom"] = [(front_legroom - m) / std]
    inFrame["front_legroom"] = dic["front_legroom"]
    # 4. Fuel tank volume
    fuel_tank_volume = float(fuel_tank_volume_entry.get())
    des = df.describe()["fuel_tank_volume"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["fuel_tank_volume"] = [(fuel_tank_volume - m) / std]
    inFrame["fuel_tank_volume"] = dic["fuel_tank_volume"]
    # 5. Height
    height = float(height_entry.get())
    des = df.describe()["height"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["height"] = [(height - m) / std]
    inFrame["height"] = dic["height"]
    # 6. Length
    length = float(length_entry.get())
    des = df.describe()["length"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["length"] = [(length - m) / std]
    inFrame["length"] = dic["length"]
    # 7. Maximum Seating
    maximum_seating = int(maximum_seating_entry.get())
    lis = df["maximum_seating"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []
    target_col = maximum_seating
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[str(val) + " seats"] = new_cols[val]
    # 8. Wheelbase
    wheelbase = float(wheelbase_entry.get())
    des = df.describe()["wheelbase"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["wheelbase"] = [(wheelbase - m) / std]
    inFrame["wheelbase"] = dic["wheelbase"]
    # 9. Width
    width = float(width_entry.get())
    des = df.describe()["width"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["width"] = [(width - m) / std]
    inFrame["width"] = dic["width"]
    # 10. City fuel economy
    city_fuel_economy = float(city_fuel_economy_entry.get())
    des = df.describe()["city_fuel_economy"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["city_fuel_economy"] = [(city_fuel_economy - m) / std]
    inFrame["city_fuel_economy"] = dic["city_fuel_economy"]
    # 11. Days on market
    days_on_market = float(days_on_market_entry.get())
    des = df.describe()["daysonmarket"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["daysonmarket"] = [(days_on_market - m) / std]
    inFrame["daysonmarket"] = dic["daysonmarket"]
    #print(inFrame)
    # 12. Engine Displacement
    engine_displacement = float(engine_displacement_entry.get())
    des = df.describe()["engine_displacement"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["engine_displacement"] = [(engine_displacement - m) / std]
    inFrame["engine_displacement"] = dic["engine_displacement"]
    # 13. Highway fuel economy
    highway_fuel_economy = float(highway_fuel_economy_entry.get())
    des = df.describe()["highway_fuel_economy"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["highway_fuel_economy"] = [(highway_fuel_economy - m) / std]
    inFrame["highway_fuel_economy"] = dic["highway_fuel_economy"]
    # 14. Horsepower
    horsepower = float(horsepower_entry.get())
    des = df.describe()["horsepower"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["horsepower"] = [(horsepower - m) / std]
    inFrame["horsepower"] = dic["horsepower"]
    inFrame["power_in_horses"] = dic["horsepower"]
    # 15. Mileage
    mileage = float(mileage_entry.get())
    des = df.describe()["mileage"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["mileage"] = [(mileage - m) / std]
    inFrame["mileage"] = dic["mileage"]
    # 16. Power in RPM
    power_in_rpm = float(power_in_rpm_entry.get())
    des = df.describe()["RPM"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["RPM"] = [(power_in_rpm - m) / std]
    inFrame["RPM"] = dic["RPM"]
    # 17. Torque_ib_ft
    torque_ib_ft = float(torque_ib_ft_entry.get())
    des = df.describe()["torque_ib_ft"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["torque_ib_ft"] = [(torque_ib_ft - m) / std]
    inFrame["torque_ib_ft"] = dic["torque_ib_ft"]
    # 18. Torque_RPM
    torque_rpm = float(torque_rpm_entry.get())
    des = df.describe()["torque_RPM"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["torque_RPM"] = [(torque_rpm - m) / std]
    inFrame["torque_RPM"] = dic["torque_RPM"]
    # 19. Selller_rating
    seller_rating = float(seller_rating_entry.get())
    des = df.describe()["seller_rating"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["seller_rating"] = [(seller_rating - m) / std]
    inFrame["seller_rating"] = dic["seller_rating"]
    # 20. City
    cit = city_entry.get()
    ex = df["city"].value_counts().keys()
    lis = []
    for i in range(0, 100):
        lis.append(ex[i])
    new_cols = {}
    for city in lis:
        new_cols[city] = []
    new_cols["others"] = []
    target_col = cit
    if (target_col in lis):
        new_cols["others"].append(0)
        for city in lis:
            if city == target_col:
                new_cols[city].append(1)
            else:
                new_cols[city].append(0)
    else:
        new_cols["others"].append(1)
        for city in lis:
            new_cols[city].append(0)
    for i in range(0, 100):
        inFrame[lis[i]] = new_cols[lis[i]]
    inFrame["others"] = new_cols["others"]
    # 21. Fleet
    fleet = int(fleet_entry.get())
    lis = df["fleet"].unique()
    lis2 = []
    for val in lis:
        lis2.append("fleet " + str(val))
    # print(lis2)
    new_cols = {}
    for val in lis2:
        new_cols[val] = []

    target_col = fleet

    if (target_col == True):
        new_cols['fleet True'].append(1)
        new_cols['fleet False'].append(0)
        new_cols['fleet nan'].append(0)
    elif (target_col == False):
        new_cols['fleet True'].append(0)
        new_cols['fleet False'].append(1)
        new_cols['fleet nan'].append(0)
    else:
        new_cols['fleet True'].append(0)
        new_cols['fleet False'].append(0)
        new_cols['fleet nan'].append(1)
    for val in lis2:
        inFrame[val] = new_cols[val]
    # 22. Engine Type
    engine_type = engine_type_entry.get()
    new_cols = {}
    lis = df["engine_type"].unique()
    for val in lis:
        new_cols[val] = []
    target_col = engine_type
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 23 . Listing Color
    excolor = listing_color_entry.get().upper()
    lis = df["listing_color"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []
    target_col = excolor
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 24. Franchise Dealer
    franchise_dealer = int(franchise_dealer_entry.get())
    if (franchise_dealer):
        new_cols["franchise_dealer"] = [True]
    else:
        new_cols["franchise_dealer"] = [False]
    inFrame["franchise_dealer"] = new_cols["franchise_dealer"]
    # 25. Car Make name
    make = car_make_name_entry.get()
    lis = df["make_name"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []
    target_col = make
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 26. Car Model
    model = car_model_entry.get()
    lis = df["model_name"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []
    target_col = model
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 27. Franchise Make
    fmake = franchise_make_entry.get()
    lis = df["franchise_make"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []
    target_col = fmake
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 28. Transmission
    transmission = transmission_entry.get()
    lis = df["transmission"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []

    target_col = transmission
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 29. Transmission Display
    transmission_display = transmission_display_entry.get()
    lis = df["transmission_display"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []
    target_col = transmission_display
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 30. Wheel system
    ws = wheel_system_entry.get()
    lis = df["wheel_system"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []
    target_col = ws
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 31. Wheel system display
    wsd = wheel_system_display_entry.get()
    lis = df["wheel_system_display"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []
    target_col = wsd
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 32. Model year
    year = float(model_year_entry.get())
    des = df.describe()["year"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["year"] = [(year - m) / std]
    inFrame["year"] = dic["year"]
    # 33.Savings amount
    savings_amount = float(savings_amount_entry.get())
    des = df.describe()["savings_amount"]
    m = des["mean"]
    std = des["std"]
    dic = {}
    dic["savings_amount"] = [(savings_amount - m) / std]
    inFrame["savings_amount"] = dic["savings_amount"]
    # 34. Listed_date
    arr = []
    for i in range(0, len(df)):
        temp = df.at[i, "listed_date"]
        count = 0
        for i in range(0, len(temp)):
            count += 1
            if (temp[i] == '/'):
                break
        arr.append(temp[count:])
    df["listed_date"] = arr
    date = listed_date_entry.get()
    new_cols = {}
    lis = df["listed_date"].unique()
    for val in lis:
        new_cols[val] = []
    target_col = date
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 35 .Longitude

    Errors = []
    longs = {}
    lats = {}

    try:
        address = 'US, ' + cit
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) + '?format=json'
        response = requests.get(url).json()
        lats[cit] = response[0]["lat"]
        longs[cit] = response[0]["lon"]
    except:
        Errors.append(cit)
    lats["Lima"] = 40.7426
    longs["Lima"] = -84.1052
    lats["Peru"] = 41.3275
    longs["Peru"] = -89.1290
    lats["Merrit Island"] = 28.3181
    longs["Merrit Island"] = -80.6660
    lats["Angola"] = 41.6348
    longs["Angola"] = -84.9994
    lats["Sharpburg"] = 38.2020
    longs["Sharpburg"] = -83.9294
    lats["Mc Connellsburg"] = 39.9326
    longs["Mc Connellsburg"] = -77.9989
    lo = float(longitude_entry.get())
    # 36. Latitude
    la = float(latitude_entry.get())
    des = df.describe()["Distances"]
    m = des["mean"]
    std = des["std"]
    print(longs[cit])
    print(lats[cit])
    dist = math.sqrt((lo - float(longs[cit])) ** 2 + (la - float(lats[cit])) ** 2)
    dist = (dist - m) / std
    #new_cols["Distances"] = [dist]
    inFrame["Distances"] = [dist]
    # 37. Is new
    is_new = int(is_new_entry.get())
    if (is_new):
        new_cols["is_new"] = [True]
    else:
        new_cols["is_new"] = [False]
    inFrame["is_new"] = new_cols["is_new"]
    # 38. Frame Damaged
    frame_damage = int(frame_damage_entry.get())
    lis = df["frame_damaged"].unique()
    lis2 = []
    for val in lis:
        lis2.append("frame_damaged " + str(val))
    new_cols = {}
    for val in lis2:
        new_cols[val] = []
    target_col = frame_damage
    if (target_col == True):
        new_cols['frame_damaged True'].append(1)
        new_cols['frame_damaged False'].append(0)
        new_cols['frame_damaged nan'].append(0)
    elif (target_col == False):
        new_cols['frame_damaged True'].append(0)
        new_cols['frame_damaged False'].append(1)
        new_cols['frame_damaged nan'].append(0)
    else:
        new_cols['frame_damaged True'].append(0)
        new_cols['frame_damaged False'].append(0)
        new_cols['frame_damaged nan'].append(1)
    for val in lis2:
        inFrame[val] = new_cols[val]
    # 39. Is cab
    lis = df["isCab"].unique()
    iscab = int(iscab_entry.get())
    lis2 = []
    for val in lis:
        lis2.append("isCab " + str(val))
    new_cols = {}
    for val in lis2:
        new_cols[val] = []
    target_col = iscab
    if (target_col == True):
        new_cols['isCab True'].append(1)
        new_cols['isCab False'].append(0)
        new_cols['isCab nan'].append(0)
    elif (target_col == False):
        new_cols['isCab True'].append(0)
        new_cols['isCab False'].append(1)
        new_cols['isCab nan'].append(0)
    else:
        new_cols['isCab True'].append(0)
        new_cols['isCab False'].append(0)
        new_cols['isCab nan'].append(1)
    for val in lis2:
        inFrame[val] = new_cols[val]
    # 40. Has Accidents
    lis = df["has_accidents"].unique()
    has_accidents = int(has_accidents_entry.get())
    lis2 = []
    for val in lis:
        lis2.append("has_accidents " + str(val))
    new_cols = {}
    for val in lis2:
        new_cols[val] = []
    target_col = has_accidents
    if (target_col == True):
        new_cols['has_accidents True'].append(1)
        new_cols['has_accidents False'].append(0)
        new_cols['has_accidents nan'].append(0)
    elif (target_col == False):
        new_cols['has_accidents True'].append(0)
        new_cols['has_accidents False'].append(1)
        new_cols['has_accidents nan'].append(0)
    else:
        new_cols['has_accidents True'].append(0)
        new_cols['has_accidents False'].append(0)
        new_cols['has_accidents nan'].append(1)
    for val in lis2:
        inFrame[val] = new_cols[val]
    # 41. Fuel Type
    fuel_type = fuel_type_entry.get()
    lis = df["fuel_type"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []

    target_col = fuel_type
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 42. Owner Counts
    owner_counts = int(owner_counts_entry.get())
    lis = df["owner_count"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []
    target_col = owner_counts
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[str(val) + " owners"] = new_cols[val]
    # 43. Salvage
    salvage = int(salvage_entry.get())
    lis = df["salvage"].unique()
    lis2 = []
    for val in lis:
        lis2.append("salvage " + str(val))
    new_cols = {}
    for val in lis2:
        new_cols[val] = []
    target_col = salvage
    if (target_col == True):
        new_cols['salvage True'].append(1)
        new_cols['salvage False'].append(0)
        new_cols['salvage nan'].append(0)
    elif (target_col == False):
        new_cols['salvage True'].append(0)
        new_cols['salvage False'].append(1)
        new_cols['salvage nan'].append(0)
    else:
        new_cols['salvage True'].append(0)
        new_cols['salvage False'].append(0)
        new_cols['salvage nan'].append(1)
    for val in lis2:
        inFrame[val] = new_cols[val]
    # 44. Theft Title(bool)
    theft_title = int(theft_title_entry.get())
    lis = df["theft_title"].unique()
    lis2 = []
    for val in lis:
        lis2.append("theft_title " + str(val))
    new_cols = {}
    for val in lis2:
        new_cols[val] = []
    target_col = theft_title
    if (target_col == True):
        new_cols['theft_title True'].append(1)
        new_cols['theft_title False'].append(0)
        new_cols['theft_title nan'].append(0)
    elif (target_col == False):
        new_cols['theft_title True'].append(0)
        new_cols['theft_title False'].append(1)
        new_cols['theft_title nan'].append(0)
    else:
        new_cols['theft_title True'].append(0)
        new_cols['theft_title False'].append(0)
        new_cols['theft_title nan'].append(1)
    for val in lis2:
        inFrame[val] = new_cols[val]
    # 45. TrimId
    trimid = trim_id_entry.get()
    ex = list(df["trimId"].value_counts().keys())
    lis = []
    for i in range(0, 100):
        lis.append(ex[i])
    new_cols = {}
    for trim in lis:
        new_cols[trim] = []
    new_cols["others"] = []
    target_col = trimid
    if (target_col in lis):
        new_cols["others"].append(0)
        for trim in lis:
            if trim == target_col:
                new_cols[trim].append(1)
            else:
                new_cols[trim].append(0)
    else:
        new_cols["others"].append(1)
        for trim in lis:
            new_cols[trim].append(0)
    for i in range(0, 100):
        inFrame[lis[i]] = new_cols[lis[i]]
    inFrame["others"] = new_cols["others"]
    # 46. Trim Name
    trim_name = trim_name_entry.get()
    ex = list(df["trim_name"].value_counts().keys())
    lis = []
    for i in range(0, 100):
        lis.append(ex[i])
    new_cols = {}
    for trim in lis:
        new_cols[trim] = []
    new_cols["others"] = []
    target_col = trim_name
    if (target_col in lis):
        new_cols["others"].append(0)
        for trim in lis:
            if trim == target_col:
                new_cols[trim].append(1)
            else:
                new_cols[trim].append(0)
    else:
        new_cols["others"].append(1)
        for trim in lis:
            new_cols[trim].append(0)
    for i in range(0, 100):
        inFrame[lis[i]] = new_cols[lis[i]]
    inFrame["others"] = new_cols["others"]
    # 47. Sp Id
    sp_id = sp_id_entry.get()
    ex = list(df["sp_id"].value_counts().keys())
    lis = []
    for i in range(0, 100):
        lis.append(str(int(ex[i])))
        # print(lis[i])
    new_cols = {}
    for trim in lis:
        new_cols[trim] = []
    new_cols["others"] = []

    target_col = sp_id
    if (target_col in lis):
        new_cols["others"].append(0)
        for trim in lis:
            if trim == target_col:
                new_cols[trim].append(1)
            else:
                new_cols[trim].append(0)
    else:
        new_cols["others"].append(1)
        for trim in lis:
            new_cols[trim].append(0)
    for i in range(0, 100):
        inFrame[lis[i]] = new_cols[lis[i]]
    inFrame["others"] = new_cols["others"]
    # 48. Sp name
    sp_name = sp_name_entry.get()
    ex = list(df["sp_name"].value_counts().keys())
    lis = []
    for i in range(0, 100):
        lis.append(ex[i])
    new_cols = {}
    for trim in lis:
        new_cols[trim] = []
    new_cols["others"] = []

    target_col = sp_name
    if (target_col in lis):
        new_cols["others"].append(0)
        for trim in lis:
            if trim == target_col:
                new_cols[trim].append(1)
            else:
                new_cols[trim].append(0)
    else:
        new_cols["others"].append(1)
        for trim in lis:
            new_cols[trim].append(0)
    for i in range(0, 100):
        inFrame[lis[i]] = new_cols[lis[i]]
    inFrame["others"] = new_cols["others"]
    # 49. Interior color
    color = interior_color_entry.get().lower()
    lis = df["interior_color"].unique()
    new_cols = {}
    for val in lis:
        new_cols[val] = []
    target_col = color
    for val in lis:
        if (target_col == val):
            new_cols[val].append(1)
        else:
            new_cols[val].append(0)
    for val in lis:
        inFrame[val] = new_cols[val]
    # 50. Extra Features
    features = {}
    for i in range(0, len(df)):
        x = type("lkm")
        # print(df.at[i, "major_options"])
        if (type(df.at[i, "major_options"]) == x):
            # print(df.at[i, "major_options"])
            l = len(df.at[i, "major_options"])
            temp = df.at[i, "major_options"][1: len(df.at[i, "major_options"]) - 1]
            tmp = temp.split(", ")
            for item in tmp:
                features[item] = 1
    feats = extra_features_entry.get()
    new_cols = {}
    for feature in features:
        new_cols[feature] = []
    for feature in features:
        # print(feature)
        for i in range(0, 1):
            if (type(feats) == type("vghbj")):

                tmp = feats.split(",")
                if (feature in tmp):
                    new_cols[feature].append(1)
                else:
                    new_cols[feature].append(0)
            else:
                new_cols[feature].append(0)
    for feature in features:
        inFrame[feature] = new_cols[feature]

    print(inFrame)
    c1 = data.columns
    c2 = inFrame.columns
    count = 0
    rFrame = pd.DataFrame()
    for c11 in c1:
        if (c11 in c2):
            rFrame[c11] = inFrame[c11]
        else:
            rFrame[c11] = [0]
    print(rFrame)

    rFrame = rFrame.to_numpy()
    d = rFrame.tolist()
    url = 'http://localhost:8000'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(d))

    result = json.loads(response.content)['result']
    print(result)  # Output: [5, 4, 3, 2, 1]


# Demographics & Selling Related Features
user_info_frame =tkinter.LabelFrame(frame, text="Demographics & Selling Related Features", bg="#D8BFD8",font=("Times New Roman", 15))
user_info_frame.grid(row= 0, column=0, padx=2, pady=2)

#City & Days on the Market

city_label = tkinter.Label(user_info_frame, text="City", bg="#D8BFD8", font=("Times New Roman", 10))
city_entry = ttk.Entry(user_info_frame)
city_label.grid(row=0, column=0)
city_entry.grid(row=1, column=0)

days_on_market_label = tkinter.Label(user_info_frame, text="Days on the Market", bg="#D8BFD8", font=("Times New Roman", 10))
days_on_market_entry = tkinter.Entry(user_info_frame)
days_on_market_label.grid(row=0, column=1)
days_on_market_entry.grid(row=1, column=1)

#Mileage

mileage_label = tkinter.Label(user_info_frame, text="Mileage", bg="#D8BFD8", font=("Times New Roman", 10))
mileage_entry = tkinter.Entry(user_info_frame)
mileage_label.grid(row=0, column=2)
mileage_entry.grid(row=1, column=2)


#Seller Rating
seller_rating_label = tkinter.Label(user_info_frame, text="Seller Rating", bg="#D8BFD8", font=("Times New Roman", 10))
seller_rating_entry = tkinter.Entry(user_info_frame)
seller_rating_label.grid(row=2, column=0)
seller_rating_entry.grid(row=3, column=0)

#Fleet
fleet_label = tkinter.Label(user_info_frame, text="Fleet", bg="#D8BFD8",font=("Times New Roman", 10))
fleet_entry = ttk.Entry(user_info_frame)
fleet_label.grid(row=2, column=1)
fleet_entry.grid(row=3, column=1)

#Franchise Dealer
franchise_dealer_label = tkinter.Label(user_info_frame, text="Franchise Dealer", bg="#D8BFD8",font=("Times New Roman", 10))
franchise_dealer_entry = ttk.Entry(user_info_frame)
franchise_dealer_label.grid(row=2, column=2)
franchise_dealer_entry.grid(row=3, column=2)

#Saving Amount
savings_amount_label = tkinter.Label(user_info_frame, text="Savings Amount", bg="#D8BFD8",font=("Times New Roman", 10))
savings_amount_entry = ttk.Entry(user_info_frame)
savings_amount_label.grid(row=4, column=0)
savings_amount_entry.grid(row=5, column=0)

#IsCab
iscab_label = tkinter.Label(user_info_frame, text="IsCab", bg="#D8BFD8",font=("Times New Roman", 10))
iscab_entry = ttk.Entry(user_info_frame)
iscab_label.grid(row=4, column=1)
iscab_entry.grid(row=5, column=1)

#Owner Counts
owner_counts_label = tkinter.Label(user_info_frame, text="Owner Counts", bg="#D8BFD8",font=("Times New Roman", 10))
owner_counts_entry = ttk.Entry(user_info_frame)
owner_counts_label.grid(row=4, column=2)
owner_counts_entry.grid(row=5, column=2)

#Salvage
salvage_label = tkinter.Label(user_info_frame, text="Salvage", bg="#D8BFD8",font=("Times New Roman", 10))
salvage_entry = ttk.Entry(user_info_frame)
salvage_label.grid(row=6, column=0)
salvage_entry.grid(row=7, column=0)



#Theft Title
theft_title_label = tkinter.Label(user_info_frame, text="Theft Title", bg="#D8BFD8",font=("Times New Roman", 10))
theft_title_entry = ttk.Entry(user_info_frame)
theft_title_label.grid(row=6, column=1)
theft_title_entry.grid(row=7, column=1)


#Sp name
sp_name_label = tkinter.Label(user_info_frame, text="Sp name", bg="#D8BFD8",font=("Times New Roman", 10))
sp_name_entry = ttk.Entry(user_info_frame)
sp_name_label.grid(row=6, column=2)
sp_name_entry.grid(row=7, column=2)

#Sp ID
sp_id_label = tkinter.Label(user_info_frame, text="Sp ID", bg="#D8BFD8",font=("Times New Roman", 10))
sp_id_entry = ttk.Entry(user_info_frame)
sp_id_label.grid(row=8, column=0)
sp_id_entry.grid(row=9, column=0)

#Listed date
listed_date_label = tkinter.Label(user_info_frame, text="Listed date", bg="#D8BFD8",font=("Times New Roman", 10))
listed_date_entry = ttk.Entry(user_info_frame)
listed_date_label.grid(row=8, column=1)
listed_date_entry.grid(row=9, column=1)

#Is new
is_new_label = tkinter.Label(user_info_frame, text="Is new", bg="#D8BFD8",font=("Times New Roman", 10))
is_new_entry = ttk.Entry(user_info_frame)
is_new_label.grid(row=8, column=2)
is_new_entry.grid(row=9, column=2)



for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
# Car Body & Amenities
body_amenities_frame = tkinter.LabelFrame(frame,text="Car Body & Amenities",  bg="#D8BFD8", font=("Times New Roman", 15))
body_amenities_frame.grid(row=0, column=1, sticky="news", padx=5, pady=2)

#Back legroom
back_legroom_label = tkinter.Label(body_amenities_frame, text="Back legroom", bg="#D8BFD8",  font=("Times New Roman", 10))
back_legroom_entry = ttk.Entry(body_amenities_frame)
back_legroom_label.grid(row=0, column=0)
back_legroom_entry.grid(row=1, column=0)

#Front legroom
front_legroom_label = tkinter.Label(body_amenities_frame, text="Front legroom",  bg="#D8BFD8", font=("Times New Roman", 10))
front_legroom_entry = ttk.Entry(body_amenities_frame)
front_legroom_label.grid(row=0, column=1)
front_legroom_entry.grid(row=1, column=1)

#Height
height_label = tkinter.Label(body_amenities_frame, text="Height",  bg="#D8BFD8", font=("Times New Roman", 10))
height_entry = ttk.Entry(body_amenities_frame)
height_label.grid(row=0, column=2)
height_entry.grid(row=1, column=2)

#Maximum Seating
maximum_seating_label = tkinter.Label(body_amenities_frame, text="Maximum Seating",  bg="#D8BFD8", font=("Times New Roman", 10))
maximum_seating_entry = ttk.Entry(body_amenities_frame)
maximum_seating_label.grid(row=0, column=2)
maximum_seating_entry.grid(row=1, column=2)

#Body Type
body_type_label = tkinter.Label(body_amenities_frame, text="Body Types",  bg="#D8BFD8", font=("Times New Roman", 10))
body_type_entry = ttk.Entry(body_amenities_frame)
body_type_label.grid(row=2, column=0)
body_type_entry.grid(row=3, column=0)

#Listing color
listing_color_label = tkinter.Label(body_amenities_frame, text="Listing color",  bg="#D8BFD8", font=("Times New Roman", 10))
listing_color_entry = ttk.Entry(body_amenities_frame)
listing_color_label.grid(row=2, column=1)
listing_color_entry.grid(row=3, column=1)

#Interior color
interior_color_label = tkinter.Label(body_amenities_frame, text="Interior color",  bg="#D8BFD8", font=("Times New Roman", 10))
interior_color_entry = ttk.Entry(body_amenities_frame)
interior_color_label.grid(row=2, column=2)
interior_color_entry.grid(row=3, column=2)

#Car Make Name
car_make_name_label = tkinter.Label(body_amenities_frame, text="Car Make Name",  bg="#D8BFD8", font=("Times New Roman", 10))
car_make_name_entry = ttk.Entry(body_amenities_frame)
car_make_name_label.grid(row=4, column=0)
car_make_name_entry.grid(row=5, column=0)

#Car Model
car_model_label = tkinter.Label(body_amenities_frame, text="Car Model",  bg="#D8BFD8", font=("Times New Roman", 10))
car_model_entry = ttk.Entry(body_amenities_frame)
car_model_label.grid(row=4, column=1)
car_model_entry.grid(row=5, column=1)

#Model year
model_year_label = tkinter.Label(body_amenities_frame, text="Model year", bg="#D8BFD8", font=("Times New Roman", 10))
model_year_entry = ttk.Entry(body_amenities_frame)
model_year_label.grid(row=4, column=2)
model_year_entry.grid(row=5, column=2)

#Frame damaged
frame_damage_label = tkinter.Label(body_amenities_frame, text="Frame damaged",  bg="#D8BFD8")
frame_damage_entry = ttk.Entry(body_amenities_frame)
frame_damage_label.grid(row=6, column=0)
frame_damage_entry.grid(row=7, column=0)

#Has accidents
has_accidents_label = tkinter.Label(body_amenities_frame, text="Has accidents",  bg="#D8BFD8", font=("Times New Roman", 10))
has_accidents_entry = ttk.Entry(body_amenities_frame)
has_accidents_label.grid(row=6, column=1)
has_accidents_entry.grid(row=7, column=1)

#Trim name(???)
trim_name_label = tkinter.Label(body_amenities_frame, text="Trim name",  bg="#D8BFD8", font=("Times New Roman", 10))
trim_name_entry = ttk.Entry(body_amenities_frame)
trim_name_label.grid(row=6, column=2)
trim_name_entry.grid(row=7, column=2)


#Trim ID(???)
trim_id_label = tkinter.Label(body_amenities_frame, text="Trim ID",  bg="#D8BFD8", font=("Times New Roman", 10))
trim_id_entry = ttk.Entry(body_amenities_frame)
trim_id_label.grid(row=8, column=0)
trim_id_entry.grid(row=9, column=0)

# #Major options(???)
# major_options_label = tkinter.Label(body_amenities_frame, text="Major options",  bg="#D8BFD8", font=("Times New Roman", 10))
# major_options_combobox = ttk.Combobox(body_amenities_frame, values = ["has_accidents nan", "has_accidents True", "has_accidents False"])
# major_options_label.grid(row=8, column=1)
# major_options_combobox.grid(row=9, column=1)

#Height
height_label = tkinter.Label(body_amenities_frame, text="Height",  bg="#D8BFD8", font=("Times New Roman", 10))
height_entry = ttk.Entry(body_amenities_frame)
height_label.grid(row=8, column=2)
height_entry.grid(row=9, column=2)

#Length
length_label = tkinter.Label(body_amenities_frame, text="Length",  bg="#D8BFD8", font=("Times New Roman", 10))
length_entry = ttk.Entry(body_amenities_frame)
length_label.grid(row=0, column=4)
length_entry.grid(row=1, column=4)

#width
width_label = tkinter.Label(body_amenities_frame, text="Width",  bg="#D8BFD8", font=("Times New Roman", 10))
width_entry = ttk.Entry(body_amenities_frame)
width_label.grid(row=2, column=4)
width_entry.grid(row=3, column=4)

#Franchise make; franchise_make
franchise_make_label = tkinter.Label(body_amenities_frame, text="Franchise Make",  bg="#D8BFD8", font=("Times New Roman", 10))
franchise_make_entry = ttk.Entry(body_amenities_frame)
franchise_make_label.grid(row=4, column=4)
franchise_make_entry.grid(row=5, column=4)


#Longitude
longitude_label = tkinter.Label(body_amenities_frame, text="Longitude", bg="#D8BFD8",font=("Times New Roman", 10))
longitude_entry = ttk.Entry(body_amenities_frame)
longitude_label.grid(row=6, column=4)
longitude_entry.grid(row=7, column=4)

#Latitude
latitude_label = tkinter.Label(body_amenities_frame, text="Latitude", bg="#D8BFD8",font=("Times New Roman", 10))
latitude_entry = ttk.Entry(body_amenities_frame)
latitude_label.grid(row=8, column=4)
latitude_entry.grid(row=9, column=4)

#Extra Features
extra_features_label = tkinter.Label(body_amenities_frame, text="Extra Features", bg="#D8BFD8", font=("Times New Roman", 10))
extra_features_entry = ttk.Entry(body_amenities_frame)
extra_features_label.grid(row=8, column=1)
extra_features_entry.grid(row=9, column=1)



for widget in body_amenities_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
# Fuel Related features
fuel_frame = tkinter.LabelFrame(frame, text="Fuel Related features", bg="#D8BFD8", font=("Times New Roman", 15))
fuel_frame.grid(row=1, column=0, sticky="news", padx=2, pady=2)

# Fuel tank volume
fuel_tank_volume_label = tkinter.Label(fuel_frame, text="Fuel tank volume", bg="#D8BFD8", font=("Times New Roman", 10))
fuel_tank_volume_entry = ttk.Entry(fuel_frame)
fuel_tank_volume_label.grid(row=0, column=0)
fuel_tank_volume_entry.grid(row=1, column=0)

# City Fuel economy
city_fuel_economy_label = tkinter.Label(fuel_frame, text="City Fuel Economy", bg="#D8BFD8", font=("Times New Roman", 10))
city_fuel_economy_entry = ttk.Entry(fuel_frame)
city_fuel_economy_label.grid(row=0, column=1)
city_fuel_economy_entry.grid(row=1, column=1)

# Highway Fuel Economy
highway_fuel_economy_label = tkinter.Label(fuel_frame, text="Highway Fuel Economy", bg="#D8BFD8", font=("Times New Roman", 10))
highway_fuel_economy_entry = ttk.Entry(fuel_frame)
highway_fuel_economy_label.grid(row=0, column=2)
highway_fuel_economy_entry.grid(row=1, column=2)

# Fuel type
fuel_type_label = tkinter.Label(fuel_frame, text="Fuel type", bg="#D8BFD8", font=("Times New Roman", 10))
fuel_type_entry = ttk.Entry(fuel_frame)
fuel_type_label.grid(row=2, column=0)
fuel_type_entry.grid(row=3, column=0)

for widget in fuel_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
#Engine Related features
engine_frame = tkinter.LabelFrame(frame, text="Engine Related features", bg="#D8BFD8", font=("Times New Roman", 15))
engine_frame.grid(row=1, column=1, sticky="news", padx=2, pady=2)

#Horsepower
horsepower_label = tkinter.Label(engine_frame, text="Horsepower", bg="#D8BFD8", font=("Times New Roman", 10))
horsepower_entry = ttk.Entry(engine_frame)
horsepower_label.grid(row=0, column=0)
horsepower_entry.grid(row=1, column=0)

# Engine Displacement
engine_displacement_label = tkinter.Label(engine_frame, text="Engine Displacement", bg="#D8BFD8", font=("Times New Roman", 10))
engine_displacement_entry = ttk.Entry(engine_frame)
engine_displacement_label.grid(row=0, column=1)
engine_displacement_entry.grid(row=1, column=1)

# Power in RPM
power_in_rpm_label = tkinter.Label(engine_frame, text="Power in RPM", bg="#D8BFD8", font=("Times New Roman", 10))
power_in_rpm_entry = ttk.Entry(engine_frame)
power_in_rpm_label.grid(row=0, column=2)
power_in_rpm_entry.grid(row=1, column=2)

# Torque_ib_ft
torque_ib_ft_label = tkinter.Label(engine_frame, text="Torque_ib_ft", bg="#D8BFD8", font=("Times New Roman", 10))
torque_ib_ft_entry = ttk.Entry(engine_frame)
torque_ib_ft_label.grid(row=2, column=0)
torque_ib_ft_entry.grid(row=3, column=0)

# Torque_RPM
torque_rpm_label = tkinter.Label(engine_frame, text="Torque_RPM", bg="#D8BFD8", font=("Times New Roman", 10))
torque_rpm_entry = ttk.Entry(engine_frame)
torque_rpm_label.grid(row=0,column=4)
torque_rpm_entry.grid(row=1,column=4)

# Engine Type
engine_type_label = tkinter.Label(engine_frame, text="Engine Type", bg="#D8BFD8", font=("Times New Roman", 10))
engine_type_entry = ttk.Entry(engine_frame)
engine_type_label.grid(row=2, column=1)
engine_type_entry.grid(row=3, column=1)

# Transmission
transmission_label = tkinter.Label(engine_frame, text="Transmission", bg="#D8BFD8", font=("Times New Roman", 10))
transmission_entry = ttk.Entry(engine_frame)
transmission_label.grid(row=2, column=2)
transmission_entry.grid(row=3, column=2)

# Transmission Display
transmission_display_label = tkinter.Label(engine_frame, text="Transmission Display", bg="#D8BFD8", font=("Times New Roman", 10))
transmission_display_entry = ttk.Entry(engine_frame)
transmission_display_label.grid(row=2, column=4)
transmission_display_entry.grid(row=3, column=4)




for widget in engine_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
#Wheel Related features
wheel_frame = tkinter.LabelFrame(frame, text="Wheel Related features", bg="#D8BFD8", font=("Times New Roman", 15))
wheel_frame.grid(row=2, column=0, sticky="news", padx=2, pady=2)


# Wheel base
wheelbase_label = tkinter.Label(wheel_frame, text="Wheel base Feature", bg="#D8BFD8", font=("Times New Roman", 10))
wheelbase_entry = ttk.Entry(wheel_frame)
wheelbase_label.grid(row=0, column=0)
wheelbase_entry.grid(row=1, column=0)


# Wheel system

wheel_system_label = tkinter.Label(wheel_frame, text="Wheel system", bg="#D8BFD8", font=("Times New Roman", 10))
wheel_system_entry = ttk.Entry(wheel_frame)
wheel_system_label.grid(row=0, column=1)
wheel_system_entry.grid(row=1, column=1)



# Wheel system Display
wheel_system_display_label = tkinter.Label(wheel_frame, text="Wheel system Display", bg="#D8BFD8", font=("Times New Roman", 10))
wheel_system_display_entry = ttk.Entry(wheel_frame)
wheel_system_display_label.grid(row=0, column=2)
wheel_system_display_entry.grid(row=1, column=2)

for widget in wheel_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data, bg="light blue", font=("Times New Roman", 30))
button.grid(row=2, column=1, sticky="news", padx=2, pady=5)
#print(city+"jkm")
window.mainloop()
#print("here1")
#print(city)
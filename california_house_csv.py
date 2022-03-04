import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('california_house_data.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS test')
print("table dropped successfully");
# create table again
conn.execute('CREATE TABLE test (longitude int, latitude REAL, housing_median_age INTEGER, total_rooms INTEGER, households INTEGER, median_income REAL, median_house_value INTEGER)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS train')
print("table dropped successfully");
# create the status table again  
conn.execute('CREATE TABLE train (train_id INTEGER PRIMARY KEY AUTOINCREMENT, Tlongitude , total_bedrooms INTEGER, population INTEGER, test_id INTEGER)')
print("table created successfully");

# open the file to read it into the database
with open('california_house/california_house_test.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        longitude = int(row[0])
        latitude = float(row[1])
        housing_median_age = int(row[2])
        total_rooms = int(row[3])
        households = int(row[6])
        median_income = float(row[7])
        median_house_value = int(row[8])

        cur.execute('INSERT INTO test VALUES (?,?,?,?,?,?,?)', (longitude, latitude, housing_median_age, total_rooms, households, median_income, median_house_value))
        conn.commit()
print("data parsed successfully");


# open the file to read it into the database
with open('california_house/california_house_train.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    print('start to work on the train table')
    for row in reader:
        print(row)
        # check if the row starts with empty string (avoid reading empty lines after the data)
        if row[0]: 
            try:
              Tlongitude = int(row[0])
              print('longitude', Tlongitude)
              # link between two tables
              cur.execute('SELECT * from test WHERE longitude=?', (Tlongitude,))
              temp_row = cur.fetchall() #temp_row is a tuple, and not an array, so need first item from first item
              test_id = int(temp_row[0][0])

              total_bedrooms = int(row[4])
              population = int(row[5])
             

              # print(population)
              cur.execute('INSERT INTO train (Tlongitude, total_bedrooms, population, test_id) VALUES ( ?,?,?,?)', (longitude, total_bedrooms, population, test_id))
              conn.commit()
            except Exception: # if there are missing values, go to the next row
              pass
        else: # stop reading when reaching empty lines.
            break


conn.close()
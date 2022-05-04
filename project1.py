import pandas as pd

# Step 1: Read the csv file 
df = pd.read_csv('ratings.csv')

# Step 2: Print out the data from the csv file 
print(df) 

# Step 3: Get the average of the column named "rating" 
rm = df["rating"].mean()

# Step 4: Convert the average so that there's only one number after the decimal
number = "{:.1f}".format(rm)

# Step 4: Retrieve the variable and print it out with the string
print("The average of the ratings column is", number)








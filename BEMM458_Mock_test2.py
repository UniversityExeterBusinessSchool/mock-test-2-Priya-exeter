#######################################################################################################################################################
# 
# Name: Priyanka Sharma
# SID:740098979
# Exam Date:26-03-2025
# Module:BEMM458
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/mock-test-2-Priya-exeter
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.

# Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax, 
#                but not to generate code. Clearly indicate how and where you used AI.

# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# Instruction 4. Commit to Git and upload to ELE once you finish.

#######################################################################################################################################################

# Question 1 - Loops and Lists
# You are given a list of numbers representing weekly sales in units.
weekly_sales = [120, 85, 100, 90, 110, 95, 130]

# Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
# Calculate and print the average sales.

weekly_sales = [120, 85, 100, 90, 110, 95, 130]
total_sales = 0
for sale in weekly_sales:
    total_sales = total_sales + sale
average_sales = total_sales / len(weekly_sales)
print("Average Sales:", average_sales)
for sale in weekly_sales:
    if sale > average_sales:
        print(str(sale) + " is above average")
    elif sale < average_sales:
        print(str(sale) + " is below average")
    else:
        print(str(sale) + " is equal to average")
#output - Average Sales: 104.28571428571429
120 is above average
85 is below average
100 is below average
90 is below average
110 is above average
95 is below average
130 is above average
#######################################################################################################################################################

# Question 2 - String Manipulation
# A customer feedback string is provided:
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# Store each position in a list as a tuple (start, end) for both words and print the list.

customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""
word1 = "good"
word2 = "improved"
first_good = customer_feedback.find(word1)
last_good = customer_feedback.rfind(word1)
tuple_good_first = (first_good, first_good + len(word1))
tuple_good_last = (last_good, last_good + len(word1))
first_improved = customer_feedback.find(word2)
last_improved = customer_feedback.rfind(word2)
tuple_improved_first = (first_improved, first_improved + len(word2))
tuple_improved_last = (last_improved, last_improved + len(word2))
positions = [tuple_good_first, tuple_good_last, tuple_improved_first, tuple_improved_last]
print(positions)
#output- [(16, 20), (16, 20), (34, 42), (34, 42)]
#######################################################################################################################################################

# Question 3 - Functions for Business Metrics
# Define functions to calculate the following metrics, and call each function with sample values (use your student ID digits for customization).

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.

def net_profit_margin(net_profit, revenue):
    return (net_profit / revenue) * 100

def customer_acquisition_cost(total_marketing_cost, new_customers):
    return total_marketing_cost / new_customers

def net_promoter_score(promoters, detractors, total_respondents):
    return ((promoters - detractors) / total_respondents) * 100

def return_on_investment(net_gain, investment_cost):
    return (net_gain / investment_cost) * 100

margin = net_profit_margin(740098979, 5000000000)
print("Net Profit Margin: " + str(round(margin, 2)) + "%")

cac = customer_acquisition_cost(740098979, 5000)
print("Customer Acquisition Cost: " + str(round(cac, 2)))

nps = net_promoter_score(740098979, 2345979, 150000000)
print("Net Promoter Score: " + str(round(nps, 2)) + "%")

roi = return_on_investment(740098979, 400000000)
print("Return on Investment: " + str(round(roi, 2)) + "%")

#output- Net Profit Margin: 14.8%
Customer Acquisition Cost: 148019.8
Net Promoter Score: 491.84%
Return on Investment: 185.02%
#######################################################################################################################################################

# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.
import pandas as pd

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}
import pandas as pd
sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
              'Sales': [200, 220, 210, 240, 250]}
df = pd.DataFrame(sales_data)
i = 0
total_sales = 0
print("Cumulative monthly sales:")
while i < len(df):
    total_sales += df.loc[i, 'Sales']
    print("total_sales upto ",df.loc[i,'Month'],":",total_sales)
    i += 1
#OUTPUT :Cumulative monthly sales:
total_sales upto  Jan : 200
total_sales upto  Feb : 420
total_sales upto  Mar : 630
total_sales upto  Apr : 870
total_sales upto  May : 1120

#######################################################################################################################################################

# Question 5 - Linear Regression for Forecasting
# Using the dataset below, create a linear regression model to predict the demand for given prices.
# Predict the demand if the company sets the price at £26. Show a scatter plot of the data points and plot the regression line.

# Price (£): 15, 18, 20, 22, 25, 27, 30
# Demand (Units): 200, 180, 170, 160, 150, 140, 130
import numpy as np
import matplotlib.pyplot as plt

prices = np.array([15, 18, 20, 22, 25, 27, 30])
demand = np.array([200, 180, 170, 160, 150, 140, 130])

coeff = np.polyfit(prices, demand, 1)
slope = coeff[0]
intercept = coeff[1]

predicted_demand = slope * 26 + intercept
print("Predicted demand at £26:", predicted_demand)

plt.scatter(prices, demand)
x_line = np.linspace(15, 30, 100)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, color='red')
plt.xlabel("Price (£)")
plt.ylabel("Demand (Units)")
plt.title("Linear Regression: Price vs Demand")
plt.show()

#######################################################################################################################################################

# Question 6 - Error Handling
# You are given a dictionary of prices for different products.
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# Write a function to calculate the total price of all items, handling any non-numeric values by skipping them.
# Include error handling in your function and explain where and why it’s needed.

prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}
def calculate_total(prices_dict):
    total_price = 0
    for item in prices_dict:
        price = prices_dict[item]
        # Check if price is a number
        if isinstance(price, (int, float)):
            total_price += price
        else:
            print(f"Skipping '{item}' because price '{price}' is not a number.")
    return total_price
total = calculate_total(prices)
print("Total price of valid items:", total)
#output- Skipping 'C' because price 'unknown' is not a number.
Total price of valid items: 155
#######################################################################################################################################################

# Question 7 - Plotting and Visualization
# Generate 50 random numbers between 1 and 500, then:
# Plot a histogram to visualize the distribution of these numbers.
# Add appropriate labels for the x-axis and y-axis, and include a title for the histogram.

import matplotlib.pyplot as plt
import random
numbers = []
for i in range(50):
    num = random.randint(1, 500) 
    numbers.append(num)           
plt.hist(numbers, edgecolor='black')  
plt.xlabel("Random Number")
plt.ylabel("Frequency")
plt.title("Histogram of 50 Random Numbers between 1 and 500")
plt.show()

#######################################################################################################################################################

# Question 8 - List Comprehensions
# Given a list of integers representing order quantities.
quantities = [5, 12, 9, 15, 7, 10]

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
# Print the original and the new lists.
quantities = [5, 12, 9, 15, 7, 10]
new_quantities = []
for q in quantities:
    if q >= 10:
        new_quantities.append(q * 2)
    else:
        new_quantities.append(q)
print("Original Quantities:", quantities)
print("New Quantities:", new_quantities)
#output - Original Quantities: [5, 12, 9, 15, 7, 10]
New Quantities: [5, 24, 9, 30, 7, 20]
#######################################################################################################################################################

# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}

ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}
filtered_ratings = {}
for product, rating in ratings.items():
    if rating >= 4:
        filtered_ratings[product] = rating
print(filtered_ratings)
#output : {'product_A': 4, 'product_B': 5, 'product_E': 5}
#######################################################################################################################################################

# Question 10 - Debugging and Correcting Code
# The following code intends to calculate the average of a list of numbers, but it contains errors:
values = [10, 20, 30, 40, 50]
total = 0
for i in values:
    total = total + i
average = total / len(values)
print("The average is" + average)

# Identify and correct the errors in the code.
# Comment on each error and explain your fixes.
print("The average is " + str(average))
#######################################################################################################################################################

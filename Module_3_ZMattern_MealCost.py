def calculate_food_cost():
    cost_of_food = float(input('Enter the cost of the food: '))
    tip_percentage = .18
    sales_tax = .07

    #Calculate the total cost of the food
    #The tip will be taken from the total after sales tax since restaurants typically do this
    total_cost_before_tip = (cost_of_food * (1 + sales_tax))
    total_cost_after_tip = (total_cost_before_tip * (1+ tip_percentage))
    #print Tip Percentage
    print('Tip Percentage: ',f"{tip_percentage:.2%}")
    #print the sales tax formated as a percentage
    print('Sales Tax: ',f"{sales_tax:.2%}")
    #print the total cost
    print('Total Cost: ','$',"%0.2f" % total_cost_after_tip)

calculate_food_cost()
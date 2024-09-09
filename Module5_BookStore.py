number_of_books_purchased = int(input('Enter number of books purchased:\n'))
points = 0
if number_of_books_purchased == 0:
    points = 0
elif 2 <= number_of_books_purchased < 4:
    points = 5
elif 4 <= number_of_books_purchased < 6:
    points = 15
elif 6 <= number_of_books_purchased < 8:
    points = 30
elif number_of_books_purchased >= 8:
    points = 60
print('Total Points:', points)
 
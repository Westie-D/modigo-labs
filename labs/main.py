def list_average(numbers):
    if len(numbers) == 0:
        return 0

    total = 0
    for num in numbers:
        total = total + num

        average = total / len(numbers)
    return round(average, 2)


        # TODO: use a for loop to calculate the average of `numbers`, rounded to 2 decimal places
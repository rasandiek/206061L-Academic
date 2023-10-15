def maximum_donation_amount(donation):
    d_list = list(map(int, donation.split()))

    n = len(d_list)

    if n == 0:
        return 0
    elif n == 1:
        return d_list[0]

    maximum_amount_with_currentval = d_list[0]
    maximum_amount_without_currentval = 0

    for i in range(1,n):
        new_maximum_amount_with_currentval = max(maximum_amount_without_currentval + d_list[i], maximum_amount_with_currentval)
        maximum_amount_without_currentval = maximum_amount_with_currentval
        maximum_amount_with_currentval = new_maximum_amount_with_currentval

    return max(maximum_amount_with_currentval, maximum_amount_without_currentval)

enter_donation_values = input()
maximum_amount = maximum_donation_amount(enter_donation_values)
print(maximum_amount)
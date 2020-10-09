import sys
import argparse
import math
from math import log


def monthly_payments(principal, monthly, interest):
    p = principal
    annuity_payment = monthly
    loan_interest = interest
    # calculates nominal interest rate Note: () need to be there
    i = loan_interest / (12 * 100)

    # calculates number of months
    n = math.ceil(log(annuity_payment / (annuity_payment - i * p), 1 + i))

    #  calculates years and months by taking total number of months and dividing by 12
    total_years = math.floor(n / 12)
    total_months = math.ceil(n - (total_years * 12))

    #  multiple years with no months
    if total_years > 1 and total_months == 0:
        print(f"It will take {total_years} years to repay the loan!")

    # multiple years and multiple months
    elif total_years > 1 and total_months > 1:
        print(f"It will take {total_years} years and {total_months} months to repay this loan!")

    #  1 year and no months
    elif total_years == 1 and total_months == 0:
        print(f"It will take {total_years} year to repay the loan!")

    #  1 year and one month
    elif total_years == 1 and total_months == 1:
        print(f"It will take {total_years} year and {total_months} month to repay this loan! ")

    #  1 year and several months
    elif total_years == 1 and total_months > 1:
        print(f"It will take  {total_years} year and {total_months} months to repay this loan!")

    #  0 years and Several months
    elif total_years == 0 and total_months > 1:
        print(f"It will take {total_months} months to repay this loan!")

    #  0 years and 1 month
    elif total_years == 0 and total_months == 1:
        print(f"It will take {total_months} month to repay this loan!")

    overpayment = annuity_payment * n - p
    print("Overpayment = {0}".format(overpayment))


def annuity(principal, periods, loan_interest):
    p = int(principal)
    n = periods
    interest_rate = loan_interest
    total = 0
    #  Gets nominal interest rate
    i = interest_rate / (12 * 100)

    #  Calculates annuity
    annuity_payment = math.ceil(p * ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1)))
    annuity_payment = int(annuity_payment)
    print("Your monthly payment = {}!".format(annuity_payment))
    overpayment = annuity_payment * n - p
    print("Overpayment = {0}".format(overpayment))


def loan_principal(payment, periods, interest):
    annuity_payment = payment
    n = periods
    interest_rate = interest
    i = interest_rate / (12 * 100)
    p = math.floor(annuity_payment / ((i * (pow((1 + i), n))) / ((pow((1 + i), n)) - 1)))
    p = int(p)
    print("Your loan principal = {0}!".format(p))
    overpayment = int(annuity_payment * n - p)
    print("Overpayment = {0}".format(overpayment))


def diff(principal, periods, interest):
    p = principal
    n = periods
    total = 0
    interest_rate = interest
    i = interest_rate / (12 * 100)
    for m in range(1, n + 1):
        diff_month = p / n + i * (p - ((p * (m - 1)) / n))
        diff_month = int(math.ceil(diff_month))
        print("Month {0}: payment is {1}".format(m, diff_month))
        total += diff_month
    overpayment = int(total - p)
    print("Overpayment = {0}".format(overpayment))


parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument("--type", type=str, help="type of calculation")
parser.add_argument("--principal", type=float, help="credit principal")
parser.add_argument("--periods", type=int, help="count of periods")
parser.add_argument("--interest", type=float, help="credit interest")
parser.add_argument("--payment", type=float, help="Monthly payments")
args = parser.parse_args()

if len(sys.argv) > 4:
    if args.type == "diff":
        if args.payment is None:
            diff(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters.")
    elif args.type == "annuity":
        if args.payment is None:
            annuity(args.principal, args.periods, args.interest)
        elif args.principal is None:
            loan_principal(args.payment, args.periods, args.interest)
        elif args.periods is None:
            monthly_payments(args.principal, args.payment, args.interest)
        else:
            print("Incorrect parameters.")
    else:
        print("Incorrect parameters.")
else:
    print("Incorrect parameters.")

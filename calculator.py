import pandas as pd
import random

VACANCY_RATE = 0.05 # vacancy rate expressed as a ratio, ex. 0.05 = 5%
MANAGEMENT_FEE = 0.1 # management fee as ratio of rent'
INSURANCE_RATIO = 0.01 # this varies by location, try to find a better way to calculate
TURNOVER_EXPENSE = 500 # how much it costs you anytime someone moves in/out
MAINTENANCE_RATIO = .02 # cost of yearly maintenance / value of house
UTILITIES_COST = 100 # monthly cost of utilities for property owner
INTEREST_RATE = 0.067 # mortgage interest rate
LOAN_TERM = 30 # loan term in years
CAP_EX = 2000 # yearly capital expeses

# get rent from rent-o-meter API
def getRent(addr: str):
    return random.randint(1000, 5000)

# market rent with no vacancy
def calcGrossPotentialRent(property):
    return getRent(property['full_street_line']) * 12

# gross potential rent - lost rent to vacancy, aka Gross Operating Income (GOI)
def calcRentLessLoss(property):
    return calcGrossPotentialRent(property) * (1 - VACANCY_RATE)

# calculate total yearly operating expenses
def calcOperatingExpenses(property):

    tax = property['tax'] # most recent year's property tax
    insurance = property['assessed_value'] * INSURANCE_RATIO # find a better way to do this
    management_fee = calcRentLessLoss(property) * MANAGEMENT_FEE
    turnOver = TURNOVER_EXPENSE
    maintenance = property['assessed_value'] * MAINTENANCE_RATIO
    utilities = UTILITIES_COST * 12

    return tax + insurance + management_fee + turnOver + maintenance + utilities


# calculate Net Operating Income (NOI) for property. NOI = Income - expenses (not including debt)
def calcNOI(property):

    income = calcRentLessLoss(property)
    expenses = calcOperatingExpenses(property)

    # print("Income: " + str(income))
    # print("Expenses: " + str(expenses))

    return income - expenses

# get monthly mortgage payment
# https://i.insider.com/617ad0d246a50c0018d40b41
def calcMonthlyMortgagePayment(property):
    r = INTEREST_RATE / 12
    n = 12 * LOAN_TERM
    return property['list_price'] * (r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)


# calculate cash flow, NOI - debt service - capital expenses
def calcCashFlow(property):
    # print("NOI: " + str(calcNOI(property)))
    # print("Yearly mortgage payment: " + str(12 * calcMonthlyMortgagePayment(property)))
    # print("Motgage payment: " + str(calcMonthlyMortgagePayment(property)))
    return calcNOI(property) - 12 * calcMonthlyMortgagePayment(property) - CAP_EX



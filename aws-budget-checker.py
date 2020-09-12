#!/usr/bin/env python

import boto3
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--accountid", help="The accountId that is associated with the budget.",  required=True)
parser.add_argument("--budgetname", help="The name of a budget. If the name has spaces must be between quotes. The : and \ characters aren't allowed in BudgetName .", required=True)
args = parser.parse_args()

account_id=(args.accountid)
budget_name=(args.budgetname)
client = boto3.client('budgets')

response = client.describe_budgets(
    AccountId=account_id
)

budgets=(response['Budgets'])
count=0
for budget in budgets:
	budgetname=(budget['BudgetName'])
	if budgetname == budget_name:
		print("Budget: " + budgetname)
		print(budget)
		BudgetLimit=(budget['BudgetLimit']['Amount'])
		ForecastedSpend=(budget['CalculatedSpend']['ForecastedSpend']['Amount'])
		count=count+1
if count == 0:
	print("Does not exist budget " + budget_name + " in account " + account_id)
	sys.exit(1)

if ForecastedSpend > BudgetLimit:
	print("CRITICAL: BudgetLimit " + BudgetLimit + " in risk to be supered this month. ForecastedSpend: " + ForecastedSpend)
else:
	percentage=(float(ForecastedSpend)/float(BudgetLimit))*100
	if percentage < 95:
		print("OK: BudgetLimit " + BudgetLimit + " || ForecastedSpend: " + ForecastedSpend + " || Percentage: " + str(percentage))
	else:
		print("WARNING: BudgetLimit " + BudgetLimit + " || ForecastedSpend: " + ForecastedSpend + " || Percentage: " + str(percentage))

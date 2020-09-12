# AWS Budget Checker

Sample implementation of automated budget checker using AWS Budgets.

## Environment tested
- Python 3.8.2

## Requirements
```
pip install -r requirements.txt
```
## Basic Configuration

You need to set up your AWS security credentials before the sample code is able
to connect to AWS. You can do this by creating a file named "credentials" at ~/.aws/ 
(`C:\Users\USER_NAME\.aws\` for Windows users) and saving the following lines in the file:

    [default]
    aws_access_key_id = <your access key id>
    aws_secret_access_key = <your secret key>

See the [Security Credentials](http://aws.amazon.com/security-credentials) page
for more information on getting your keys. For more information on configuring `boto3`,
check out the Quickstart section in the [developer guide](https://boto3.readthedocs.org/en/latest/guide/quickstart.html).

## Running the script
```
python aws-budget-check.py --accountid <ACCOUNTID> --budgetname <BUDGETNAME>
```

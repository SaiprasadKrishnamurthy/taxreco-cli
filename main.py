"""
    Main script that does the following:
      - Parses the Sales files and 26AS files in the respective directories.
      - For every GSTIN in the sales file, calls the GSTIN API to get the Legal Name.
      - Fuzzy Matches this Legal Name with the Legal Name in 26AS.
      - Establishes a Link between GSTIN - LegalName - TAN No.
      - Dumps this linked data into an output tab delimited text file
"""

import typer

from commands.delete_customer_linker import delete_customer_linker_command
from commands.jobs import list_jobs_command
from commands.trigger_customer_linker import trigger_customer_linker_command
from util.common_login import common_login

app = typer.Typer()


@app.command(short_help='Login to Taxreco with username and password')
def login():
    common_login()


@app.command(short_help='List all the jobs')
def list_jobs():
    list_jobs_command()


@app.command(
    short_help='Deletes the customer linker job if it is in progress. All the input/output data will be deleted')
def delete_customer_linker_job(jobid: str):
    delete_customer_linker_command(jobid)


@app.command(
    short_help='Submits a job to the server to link the customers from sales file to the 26as file')
def link_customers(sales_file, twentysix_as_file):
    trigger_customer_linker_command(sales_file, twentysix_as_file)


if __name__ == "__main__":
    app()

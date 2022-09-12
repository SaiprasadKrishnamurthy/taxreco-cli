"""
    Main cli app for taxreco
"""

__author__ = 'Sai Kris'

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

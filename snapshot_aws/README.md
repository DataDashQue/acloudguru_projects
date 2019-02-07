# Snapshot Anylyzer Python Project

Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots

## Configuring

shotty uses the configuration file created by AWS cli e.g

`aws configure --profile shotty`

#Required modules to run in pipenv

`pipenv install boto3`
`pipenv install click`
`pipenv lock`

## Running

`pipenv run pything shotty.py <command> <subcommand> <--project=PROJECT>:`

*command* is instances, volumes, snapshot list, start, or stop
*subcommand* depends on command
*project* is optional
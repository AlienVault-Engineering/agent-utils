FROM python:3.7
MAINTAINER AlienVault

ENV RUN_TYPE="tests"

RUN pip install -U --pre pybuilder


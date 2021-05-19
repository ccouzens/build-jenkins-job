#!/usr/bin/env python3

# use of https://python-jenkins.readthedocs.io/en/latest/index.html

import sys
import requests
import jenkins
import time
import json


def mandatory_arg(argv):
    if argv == "":
        raise ValueError("Only job_params can be empty. Required fields: url, token, user and path")
    return argv


# mandatory
JENKINS_URL = mandatory_arg(sys.argv[1])
JENKINS_TOKEN = mandatory_arg(sys.argv[2])
JENKINS_USER = mandatory_arg(sys.argv[3])
JOB_PATH = mandatory_arg(sys.argv[4])

# not mandatory
JOB_PARAMS = sys.argv[5] or '{}'

# create/connect jenkins server
server = jenkins.Jenkins(f"https://{JENKINS_URL}", username=JENKINS_USER, password=JENKINS_TOKEN)
user = server.get_whoami()
version = server.get_version()
print(f"Hello {user['fullName']} from Jenkins {version}")

# build job
split = JOB_PATH.split("job/")
job_name = "".join(split)

server.build_job(job_name, parameters=json.loads(JOB_PARAMS), token=JENKINS_TOKEN)

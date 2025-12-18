import subprocess
import os
from Results import Results

def small_get_test() -> Results:
    """ 2s/10 connections GET test """
    result = subprocess.run(
        ["siege", "-c10", "-b", "-t2s", f"http://{os.environ["webserv_host"]}:{os.environ["webserv_port"]}/"],
        capture_output = True,
        text=True,
        check=False)
    results = result.stderr.split("\n")
    retval = Results(float([result[len("Availability:\t\t"):-1].strip() for result in results if "Availability:" in result][0]))
    return (retval)

def medium_get_test() -> Results:
    """ 5s/200 connections GET test """
    result = subprocess.run(
        ["siege", "-c200", "-b", "-t5s", f"http://{os.environ["webserv_host"]}:{os.environ["webserv_port"]}/"],
        capture_output = True,
        text=True,
        check=False)
    results = result.stderr.split("\n")
    retval = Results(float([result[len("Availability:\t\t"):-1].strip() for result in results if "Availability:" in result][0]))
    return (retval)

def big_get_test() -> Results:
    """ 10s/1000 connections GET test """
    result = subprocess.run(
        ["siege", "-c1000", "-b", "-t10s", f"http://{os.environ["webserv_host"]}:{os.environ["webserv_port"]}/"],
        capture_output = True,
        text=True,
        check=False)
    results = result.stderr.split("\n")
    retval = Results(float([result[len("Availability:\t\t"):-1].strip() for result in results if "Availability:" in result][0]))
    return (retval)

def medium_internet_get_test() -> Results:
    """ 5s/500 connections simulating internet GET test """
    result = subprocess.run(
        ["siege", "-c500", "-i", "-b", "-t5s", f"http://{os.environ["webserv_host"]}:{os.environ["webserv_port"]}/"],
        capture_output = True,
        text=True,
        check=False)
    results = result.stderr.split("\n")
    retval = Results(float([result[len("Availability:\t\t"):-1].strip() for result in results if "Availability:" in result][0]))
    return (retval)

def big_internet_get_test() -> Results:
    """ 10s/1000 connections simulating internet GET test """
    result = subprocess.run(
        ["siege", "-c1000", "-i", "-b", "-t10s", f"http://{os.environ["webserv_host"]}:{os.environ["webserv_port"]}/"],
        capture_output = True,
        text=True,
        check=False)
    results = result.stderr.split("\n")
    retval = Results(float([result[len("Availability:\t\t"):-1].strip() for result in results if "Availability:" in result][0]))
    return (retval)

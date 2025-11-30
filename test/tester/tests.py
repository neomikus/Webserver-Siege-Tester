import subprocess
from Results import Results

def small_get_test() -> Results:
	result = subprocess.run(
		["siege", "-c10", "-b", "-t2s", "http://127.0.0.1:8080/"],
		capture_output = True,
		text=True)
	results = result.stderr.split("\n")
	retval = Results(float([result[len(f"Availability:\t\t"):-1].strip() for result in results if "Availability:" in result][0]))
	return (retval)

def medium_get_test() -> Results:
	result = subprocess.run(
		["siege", "-c200", "-b", "-t5s", "http://127.0.0.1:8080/"],
		capture_output = True,
		text=True)
	results = result.stderr.split("\n")
	retval = Results(float([result[len(f"Availability:\t\t"):-1].strip() for result in results if "Availability:" in result][0]))
	return (retval)

def big_get_test() -> Results:
	result = subprocess.run(
		["siege", "-c1000", "-b", "-t10s", "http://127.0.0.1:8080/"],
		capture_output = True,
		text=True)
	results = result.stderr.split("\n")
	retval = Results(float([result[len(f"Availability:\t\t"):-1].strip() for result in results if "Availability:" in result][0]))
	return (retval)

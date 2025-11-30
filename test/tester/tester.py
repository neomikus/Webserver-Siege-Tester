import subprocess
import os, signal
import tests
from Results import Results

colors = {
	"Red": "\x1b[31;5;1m",
	"Green": "\x1b[32;5;1m",
	"Reset": "\x1b[0m"
}

def print_results(results: Results):
	print("\tBasic: (Availability test only)")
	passed:bool = results.availability > 99.5
	print(colors[("Red", "Green")[passed]], f"\t\t — [{("✗", "✓")[passed]}]", f"(Availability: {results.availability}% vs 99.5%)", colors["Reset"])
	results.basic_total = 1
	results.basic_passed += passed

if __name__ == "__main__":
	""" Run Webserver first """
	print("Executing webserv...")
	webserv = subprocess.Popen(["./webserv", "default.conf"], 
								stdout=subprocess.DEVNULL,
								stderr=subprocess.DEVNULL)
	try:
		webserv.wait(timeout=3)
	except subprocess.TimeoutExpired:
		pass

	""" Webserv shouldn't have exited at this point yet """
	if (webserv.returncode):
		print("Webserver failed to execute")
		exit(2)
	
	print("\n")

	""" Execute each test in battery """
	basic_tests_passed = 0
	basic_tests_total = 0
	test_battery = [("Small GET test", "2s/10 connections"), ("Medium GET test", "5s/200 connections"), ("Big GET test", "10s/1000 connections")]
	for test in test_battery:
		print(f"Executing test {test[0]} ({test[1]})")
		match test[0]:
			case "Small GET test":
				result = tests.small_get_test()
			case "Medium GET test":
				result = tests.medium_get_test()
			case "Big GET test":
				result = tests.big_get_test()
			case _:
				pass
		if (webserv.returncode):
			print("Webserver crashed!!!")
			exit(2)
		print_results(result)
		basic_tests_passed += result.basic_passed
		basic_tests_total += result.basic_total

	""" Print amount of tests passed """
	print("Tests passed: ")
	print("\t Basic:" + colors[("Red", "Green")[basic_tests_passed == basic_tests_total]], f"{basic_tests_passed}/{basic_tests_total}")

	""" Kill webserv after finishing """
	os.kill(webserv.pid, signal.SIGSTOP)


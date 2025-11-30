import subprocess
import os, signal
import tests
import Results

def print_results(results: Results.Results):
	print("\tBasic: (Availability test only)")
	print(f"\t\t — [{("✗", "✓")[results.availability > 99.5]}]", f"(Availability: {results.availability}% vs 99.5%)")
	results.basic_total = 1
	results.basic_passed += (0, 1)[results.availability > 99.5]

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
	print(f"\t Basic: {basic_tests_passed}/{basic_tests_total}")

	""" Kill webserv after finishing """
	os.kill(webserv.pid, signal.SIGSTOP)


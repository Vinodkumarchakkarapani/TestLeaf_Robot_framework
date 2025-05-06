import os
from datetime import datetime
from robot import run

# Set path to your test cases folder
TESTS_DIR = "C:/Users/vinod/OneDrive/Desktop/TestLeaf/TestScripts/Login"  # <-- Replace with your actual path

# Create a timestamped results folder
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
RESULTS_DIR = os.path.join("results", f"run_{timestamp}")
os.makedirs(RESULTS_DIR, exist_ok=True)

# Run all tests in the folder and store outputs
run(
    TESTS_DIR,
    output=os.path.join(RESULTS_DIR, "output.xml"),
    log=os.path.join(RESULTS_DIR, "log.html"),
    report=os.path.join(RESULTS_DIR, "report.html")
)

print(f"Test results saved in: {RESULTS_DIR}")

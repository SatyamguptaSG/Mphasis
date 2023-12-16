# Quantum Computing Challenge : MPhasis

To run the code, follow the given steps

1. Clone this repo

2. `pip install -r requirements.txt`
This installs the required modules to run the code, mainly, it installs `dwave-ocean-sdk` which is required to interact with DWave Leap's API. Additonally, it also installs `ortools` which is Google's library to solve linear programming problems. It also installs `flask` which is required to run the GUI application

3. Generate a DWave Leap Solver API Token from the official [website](https://cloud.dwavesys.com/leap/)

4. `py app.py` to run the GUI

5. Follow the steps to upload the required files and choose the required business rules and solution constants. If you do not wish to do so, default values for the business rules and constants exist. The visual guide to the GUI can be found in the User Manual section of the attached documentation

6. Submitting all documents runs the code and calls the DWave Solver API. The outputs generated by the algorithm can be accessed via `output/` folder in the application repository.

7. There are $10$ generated solutions, and per flight per solution, the algorithm generates $2$ output files, `i_departureKey_default.csv` and `i_departureKey_exception.csv` corresponding to the $i^{th}$ solution.
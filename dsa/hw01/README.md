<h1>Unique Integers Project</h1>

<h1>Project Overview</h1>
<p>This project processes a list of integers from an input file and generates an output file containing unique integers. The integers in the output are sorted in increasing order. The project includes handling various edge cases, including invalid input, empty lines, non-integer values, and multiple integers on the same line.

The project follows strict memory and runtime efficiency requirements and avoids the use of built-in libraries for operations like sorting and list management.</p>

File Structure
===============

/dsa/hw01/ <br>
│<br><br>
├── code/<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   └── src/<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       └── UniqueInt.py        # The main Python file containing the implementation<br><br>
│
├── sample_inputs/              # Folder containing sample input files<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   └── small_sample_input_02.txt     # Example input file<br><br>
│
├── sample_results/             # Folder to store output files<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   └── small_sample_input_02.txt_results.txt  # Example output file for the corresponding input<br><br>
│
└── README.md                   # This README file<be>

<h2>Requirements</h2>
Python 3.4.3
The project is designed to run on Ubuntu 14.04 LTS.
<h2>Functionality</h2>
The main goal of the program is to:

Read a list of integers from an input file.
Eliminate duplicates.
Handle special cases like whitespaces, multiple integers on a line, and invalid entries.
Write the unique integers to an output file, sorted in increasing order.
<h2>Edge Case Handling</h2>
The program can handle the following variations in the input:

Whitespace: Lines with leading or trailing whitespaces around integers.
Empty lines: Lines with no content or whitespaces only.
Multiple integers on one line: These lines are skipped.
Non-integer inputs: Lines with non-integer values such as alphabetic characters or symbols are skipped.
Out-of-range integers: Only integers between -1023 and 1023 (inclusive) are processed.
<h2>How It Works</h2>
UniqueInt Class:

readNextItemFromFile(line): This method reads a line from the input file and extracts a valid integer if available. Invalid entries or lines with multiple integers are skipped.
processFile(inputFilePath, outputFilePath): Reads the entire input file, checks for unique integers, sorts them manually, and writes them to the output file.
run(inputFilePath, outputFilePath): Runs the processing while measuring execution time.
Boolean Array for Tracking: A boolean array (seen) of size 2047 is used to track whether an integer has been encountered before. The array indexes represent numbers from -1023 to 1023.

Manual Sorting: A simple comparison-based sorting algorithm is used to avoid built-in sort functions.

<h2>How to Run the Project</h2>
1. Clone the Repository: Provide instructions for cloning the project if applicable.

2. Running the Code:

You can just navigate to the code/src/ directory.
Run the Python script using the following command

*./UniqueInt.py*

Example usage:
*./UniqueInt.py /dsa/hw01/sample_inputs/sample_input_02.txt /dsa/hw01/sample_results/sample_input_02_results.txt*

3. Output: The output file will be located in the sample_results/ folder with the same name as the input file, followed by _results.txt.

<h2>Example</h2>
<h2>Sample Input File (sample_input_02.txt):</h2>
5<br>
14<br>
5<br>
-9<br>
62<br>
-1<br>
-9<br>
-9<be>
<h2>Expected Output File (sample_input_02_results.txt):</h2>

-9 <br>
-1<br>
5<br>
14<br>
62<be>


<h2>Performance and Efficiency</h2>
The program is designed to be efficient in terms of memory and runtime. It uses minimal space by keeping a boolean array and only stores unique integers.
Time taken for processing and memory usage is printed after running the program.
<h2>Limitations</h2>
The program assumes all inputs are within the range of -1023 to 1023. Any integers outside this range are ignored.


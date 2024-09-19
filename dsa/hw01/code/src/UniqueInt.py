#!/usr/bin/python3
import time  # Importing time to calculate the processing time of each input file

class UniqueInt:
    def __init__(self):
        """
        Constructor method that initializes a boolean array to track the integers 
        from -1023 to 1023. We use an array of size 2047 to represent this range.
        Each index in this array will be set to True if the corresponding integer 
        has been encountered, otherwise it remains False.
        """
        self.seen = [False] * 2047  # Boolean array for tracking unique integers
    
    def readNextItemFromFile(self, line):
        """
        Method to read the next valid integer from the file line. This method handles:
        - Stripping whitespaces around the number
        - Skipping lines that are empty or contain multiple numbers
        - Handling non-integer values
        Returns:
        - A valid integer within the range if present
        - None if the line is invalid or the integer is out of range
        """
        try:
            # Remove leading/trailing whitespaces
            line = line.strip()
            # Skip if line is empty or contains spaces (indicating multiple values)
            if line == "" or " " in line:
                return None
            # Attempt to convert the line into an integer
            number = int(line)
            # Skip if the number is out of the allowed range (-1023 to 1023)
            if number < -1023 or number > 1023:
                return None
            # Return the valid integer
            return number
        except ValueError:
            # If the line contains non-integer values, return None
            return None
    
    def processFile(self, inputFilePath, outputFilePath):
        """
        This method processes the input file and writes the result to the output file.
        It:
        - Reads each line from the input file
        - Checks if the line contains a valid unique integer
        - Keeps track of integers already seen using the boolean array
        - Sorts the unique integers manually
        - Writes the sorted unique integers to the output file
        """
        unique_numbers = []  # List to store unique integers found in the input file
        
        # Open the input file in read mode
        with open(inputFilePath, 'r') as input_file:
            for line in input_file:
                # Read and validate the next integer from the current line
                number = self.readNextItemFromFile(line)
                # If valid and not seen before, mark as seen and add to the list
                if number is not None and not self.seen[number + 1023]:
                    self.seen[number + 1023] = True  # Mark the integer as seen
                    unique_numbers.append(number)  # Add the valid integer to the list
        
        # Manually sort the unique numbers using a simple sorting algorithm (bubble sort)
        for i in range(len(unique_numbers)):
            for j in range(i + 1, len(unique_numbers)):
                if unique_numbers[i] > unique_numbers[j]:
                    # Swap the numbers to sort in ascending order
                    unique_numbers[i], unique_numbers[j] = unique_numbers[j], unique_numbers[i]
        
        # Open the output file in write mode
        with open(outputFilePath, 'w') as output_file:
            # Write each unique integer on a new line in the output file
            for number in unique_numbers:
                output_file.write(f"{number}\n")
    
    def run(self, inputFilePath, outputFilePath):
        """
        This method acts as the entry point for processing a file. It:
        - Starts a timer to track how long the processing takes
        - Calls the `processFile` method to process the input file
        - Stops the timer and prints the elapsed time for processing the file
        """
        start_time = time.time()  # Start time before processing the file
        self.processFile(inputFilePath, outputFilePath)  # Process the file
        end_time = time.time()  # End time after processing the file
        # Print the time taken to process the file
        print(f"Processed {inputFilePath} in {end_time - start_time:.2f} seconds")

# Example usage of the UniqueInt class
unique_int_processor = UniqueInt()
# Process the sample input file and generate the result file
unique_int_processor.run('../../sample_inputs/small_sample_input_02.txt', '../../sample_results/small_sample_input_02.txt_results.txt')

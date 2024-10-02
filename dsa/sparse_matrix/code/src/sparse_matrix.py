class SparseMatrix:
    def __init__(self, matrix_file_path=None, num_rows=0, num_cols=0):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.elements = {}

        if matrix_file_path:
            self.loadFromFile(matrix_file_path)

    def loadFromFile(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]

                if not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
                    raise ValueError("Invalid file format")

                self.num_rows = int(lines[0].split('=')[1])
                self.num_cols = int(lines[1].split('=')[1])

                for line in lines[2:]:
                    if not (line.startswith('(') and line.endswith(')')):
                        raise ValueError("Invalid entry format")

                    entry = line[1:-1].split(',')
                    if len(entry) != 3:
                        raise ValueError("Invalid entry format")

                    row, col, value = map(int, entry)
                    self.set_element(row, col, value)

        except (IOError, ValueError) as e:
            raise ValueError(f"Input file has wrong format: {str(e)}")

    def get_element(self, curr_row, curr_col):
        return self.elements.get((curr_row, curr_col), 0)

    def set_element(self, curr_row, curr_col, value):
        if value != 0:
            self.elements[(curr_row, curr_col)] = value
        elif (curr_row, curr_col) in self.elements:
            del self.elements[(curr_row, curr_col)]

    def __add__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for addition")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)

        for (row, col), value in self.elements.items():
            result.set_element(row, col, value)

        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) + value)

        return result

    def __sub__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for subtraction")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)

        for (row, col), value in self.elements.items():
            result.set_element(row, col, value)

        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) - value)

        return result

    def __mul__(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)

        for (i, k), a in self.elements.items():
            for (k2, j), b in other.elements.items():
                if k == k2:
                    result.set_element(i, j, result.get_element(i, j) + a * b)

        return result

    def __str__(self):
        output = f"rows={self.num_rows}\ncols={self.num_cols}\n"
        for (row, col), value in sorted(self.elements.items()):
            output += f"({row}, {col}, {value})\n"
        return output.strip()

def main():
    while True:
        print("\nSparse Matrix Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '4':
            break

        file1 = input("Enter the path for the first matrix file: ")
        file2 = input("Enter the path for the second matrix file: ")

        try:
            matrix1 = SparseMatrix(file1)
            matrix2 = SparseMatrix(file2)

            if choice == '1':
                result = matrix1 + matrix2
                operation = "addition"
            elif choice == '2':
                result = matrix1 - matrix2
                operation = "subtraction"
            elif choice == '3':
                result = matrix1 * matrix2
                operation = "multiplication"
            else:
                print("Invalid choice. Please try again.")
                continue

            print(f"\nResult of {operation}:")
            print(result)

        except ValueError as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
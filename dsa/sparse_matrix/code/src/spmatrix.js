const fs = require('fs');
const path = require('path');
const readline = require('readline');

class SparseMatrix {
  constructor(matrixFile = null, numRows = 0, numCols = 0) {
    this.matrix = {};
    this.numRows = numRows;
    this.numCols = numCols;

    if (matrixFile) {
      this.loadMatrix(matrixFile);
    }
  }

  loadMatrix(filePath) {
    try {
      const absolutePath = path.resolve(filePath);
      const fileContent = fs.readFileSync(absolutePath, 'utf-8');
      const lines = fileContent.trim().split('\n');

      this.numRows = parseInt(lines[0].split('=')[1]);
      this.numCols = parseInt(lines[1].split('=')[1]);

      lines.slice(2).forEach(line => {
        const [row, col, value] = this.parseEntry(line);
        this.setElement(row, col, value);
      });
    } catch (error) {
      throw new Error(`Error loading matrix: ${error.message}`);
    }
  }

  parseEntry(line) {
    const [row, col, value] = line.replace(/[()]/g, '').split(',').map(Number);
    return [row, col, value];
  }

  getElement(row, col) {
    return this.matrix[row]?.[col] || 0;
  }

  setElement(row, col, value) {
    if (value !== 0) {
      this.matrix[row] = this.matrix[row] || {};
      this.matrix[row][col] = value;
    }
  }

  operate(otherMatrix, operation) {
    const result = new SparseMatrix(null, this.numRows, this.numCols);

    for (let row = 0; row < this.numRows; row++) {
      for (let col = 0; col < this.numCols; col++) {
        const value = operation(this.getElement(row, col), otherMatrix.getElement(row, col));
        result.setElement(row, col, value);
      }
    }

    return result;
  }

  add(otherMatrix) {
    return this.operate(otherMatrix, (a, b) => a + b);
  }

  subtract(otherMatrix) {
    return this.operate(otherMatrix, (a, b) => a - b);
  }

  multiply(otherMatrix) {
    if (this.numCols !== otherMatrix.numRows) {
      throw new Error("Matrix multiplication not possible with incompatible sizes.");
    }

    const result = new SparseMatrix(null, this.numRows, otherMatrix.numCols);

    for (const row in this.matrix) {
      for (const col in otherMatrix.matrix) {
        const sum = Object.keys(this.matrix[row]).reduce((acc, k) => {
          return acc + (this.getElement(row, k) * otherMatrix.getElement(k, col));
        }, 0);
        result.setElement(row, col, sum);
      }
    }

    return result;
  }

  saveToFile(filePath) {
    if (!filePath || filePath.trim() === '') {
      throw new Error('File path cannot be empty.');
    }

    let content = `rows=${this.numRows}\ncols=${this.numCols}\n`;
    for (const row in this.matrix) {
      for (const col in this.matrix[row]) {
        content += `(${row}, ${col}, ${this.matrix[row][col]})\n`;
      }
    }

    try {
      fs.writeFileSync(filePath, content);
      console.log(`Matrix saved to ${filePath}`);
    } catch (error) {
      throw new Error(`Error saving file: ${error.message}`);
    }
  }
}

async function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  const question = (query) => new Promise((resolve) => rl.question(query, resolve));

  try {
    const matrix1 = new SparseMatrix('./easy_sample_01_3.txt');
    const matrix2 = new SparseMatrix('./easy_sample_03_1.txt');

    const operations = {
      '1': { name: 'Add', method: 'add' },
      '2': { name: 'Subtract', method: 'subtract' },
      '3': { name: 'Multiply', method: 'multiply' }
    };

    const operation = await question('Choose a matrix operation: 1. Add, 2. Subtract, 3. Multiply: ');

    if (!operations[operation]) {
      throw new Error('Invalid choice.');
    }

    const result = matrix1[operations[operation].method](matrix2);
    console.log(`Matrices ${operations[operation].name.toLowerCase()}ed successfully!`);

    const outputFile = await question('Enter the output file path: ');
    result.saveToFile(outputFile);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  } finally {
    rl.close();
  }
}

main();

console.log("This code cannot be executed in this environment due to file system operations.");
import csv
import os
import random
import sys

def generate_data(filename="data.csv", num_rows=10):
    """Generates sample data and writes it to a CSV file."""
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Name", "Value"])  # Write header

            for i in range(num_rows):
                name = f"Item_{i+1}"
                value = random.randint(1, 100)
                writer.writerow([i+1, name, value])

        print(f"Successfully generated {filename}")
        return True

    except Exception as e:
        print(f"Error generating data: {e}")
        return False

if __name__ == "__main__":
    # Simulate a possible error condition
    if random.random() < 0.2:  # 20% chance of "failure"
        print("Simulating an error...")
        sys.exit(1)  # Exit with a non-zero code to indicate failure

    success = generate_data()

    if success:
        print("Script completed successfully.")
        sys.exit(0)  # Exit with a zero code to indicate success
    else:
        print("Script failed.")
        sys.exit(1)  # Exit with a non-zero code to indicate failure

import numpy as np  # Import NumPy for calculations
import os  # For file handling

def read_marks_from_file(filename):
    """Reads marks from a file if it exists, otherwise asks for input."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            marks = file.read().split()
            return np.array([int(mark) for mark in marks])  # Convert to NumPy array
    else:
        print(f"⚠️ File '{filename}' not found. Switching to manual input.")
        return None

def save_analysis_to_file(filename, report):
    """Saves the analysis report to a file."""
    with open(filename, "w") as file:
        file.write(report)
    print(f"\n✅ Analysis saved to {filename}")

def analyze_marks():
    # Step 1: Ask user for file or manual input
    file_choice = input("📂 Enter filename to load marks (or press Enter to input manually): ").strip()
    
    if file_choice:
        marks = read_marks_from_file(file_choice)
    else:
        marks = input("✍️ Enter student marks separated by spaces: ").split()
        marks = np.array([int(mark) for mark in marks])  # Convert to NumPy array

    if len(marks) == 0:
        print("⚠️ No marks entered! Please enter valid numbers.")
        return
    
    # Step 2: Sorting and Analysis
    sorted_marks = np.sort(marks)
    highest = np.max(marks)
    lowest = np.min(marks)
    average = np.mean(marks)
    median = np.median(marks)
    std_dev = np.std(marks)

    # Step 3: Ranking Students
    ranked_indices = np.argsort(marks)[::-1]  # Get indices in descending order
    ranked_marks = marks[ranked_indices]

    # Step 4: Generate report
    report = "\n📊 **Marks Analysis Report** 📊\n"
    report += f"Sorted Marks: {sorted_marks}\n"
    report += f"Highest Score: {highest}\n"
    report += f"Lowest Score: {lowest}\n"
    report += f"Average Score: {average:.2f}\n"
    report += f"Median Score: {median}\n"
    report += f"Standard Deviation: {std_dev:.2f}\n\n"
    
    report += "🏆 **Ranked Students (Highest to Lowest)** 🏆\n"
    for rank, mark in enumerate(ranked_marks, start=1):
        report += f"#{rank} → {mark}\n"

    print(report)

    # Step 5: Ask to save results
    def save_analysis_to_file(filename, report):
        with open(filename + ".txt", "w", encoding="utf-8") as file:  # Add encoding="utf-8"
            file.write(report)
        print(f"\n✅ Report saved successfully as {filename}.txt")


if __name__ == "__main__":
    analyze_marks()

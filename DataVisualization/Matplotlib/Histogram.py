# import matplotlib.pyplot as plt
# marks = [50,60,70,80,90]

# plt.hist(marks)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# 1. Create a dummy dataset of student marks out of 100
# Setting a seed ensures the random marks are identical every time you run it
np.random.seed(42)
student_marks = np.random.normal(loc=72, scale=12, size=150)
student_marks = np.clip(student_marks, 0, 100)  # Keep scores strictly between 0 and 100

# 2. Define custom grade intervals (bins) for the x-axis
# This breaks the data into: 0-50, 50-60, 60-70, 70-80, 80-90, and 90-100
grade_bins = [0, 50, 60, 70, 80, 90, 100]

# 3. Create the histogram
plt.figure(figsize=(9, 6))
plt.hist(
    student_marks, 
    bins=grade_bins, 
    color='skyblue', 
    edgecolor='black', 
    linewidth=1.2
)

# 4. Add titles and labels for clarity
plt.title('Distribution of Student Performance (Final Exams)', fontsize=14, fontweight='bold')
plt.xlabel('Marks Ranges / Grade Bins', fontsize=11)
plt.ylabel('Number of Students', fontsize=11)

# 5. Align the X-axis markers exactly with our bin boundaries
plt.xticks(grade_bins)

# 6. Enable a clean grid layout for the background
plt.grid(axis='y', alpha=0.4, linestyle='--')

# 7. Render the final chart
plt.show()

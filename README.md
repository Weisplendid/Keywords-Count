## Function introduction
Count keywords of different levels from the C or C++ code files that are read in.

## Version introduction

### version_0.1
1. The most basic extraction keyword procedures.

### version_0.2
1. Eliminates the impact of strings, comments and macro definitions on the code.
2. Fixed some bugs.

### version_0.3
1. New functions added，now can:
	+  output "keyword" statistics.
	+  output the number of "switch case" structures, and output the number of "case" corresponding to each group.
	+  Uplifting requirement: output the number of "if else" structures.
	+  Ultimate requirement: output the number of "if, else if, else" structures.
	
	note: only "if" or "if-else if" are not counted.
	
	
	
2. Fixed some bugs.

### version_1.0
1. New functions added，now can choose the level:

	+  **level 1:**  Basic requirement: output "keyword" statistics.
	+  **level 2:**  Advanced requirement: output the number of "switch case" structures, and output  the number of "case" corresponding to each group.
	+  **level 3:**  Uplifting requirement: output the number of "if else" structures.
	+  **level 4:**  Ultimate requirement: output the number of "if, else if, else" structures.

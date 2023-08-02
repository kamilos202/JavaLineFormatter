# JavaLineFormatter

JavaLineFormatter is a tool designed to format Java source files by splitting lines that exceed 120 characters. It ensures that the lines are not broken in the middle of words and provides additional indentations for readability. It also takes care of special cases such as skipping comments, package or import declarations, text blocks, and ensuring that lines are not split within string literals.

## Features
Splits lines longer than 120 characters.
Preserves indentation and adds additional indentation as lines are split.
Skips comments, package and import statements, and text blocks introduced in Java 17.
Carefully handles splitting around dots and avoids breaking inside string literals.

## Installation
Clone this repository and run the script on your Java files (copy the python file to the root directory of your project).
```bash
git clone https://github.com/kamilos202/JavaLineFormatter.git
cd JavaLineFormatter
chmod +x java_line_formatter.py
python3 java_line_formatter.py
```
## Usage
You can use JavaLineFormatter by calling the function split_long_lines with the filename you want to format.

```python
from JavaLineFormatter import split_long_lines

split_long_lines('path/to/yourfile.java')
```
You can also integrate the script into a larger program or use it as a standalone tool to format all Java files in a directory.

## Requirements
Python 3.6 or higher

## Contribution
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
Thanks to all the contributors and users of JavaLineFormatter. Your feedback and support drive the success of this project.

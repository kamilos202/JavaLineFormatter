import textwrap
import glob
import os

def split_long_lines(file_name):
    in_multiline_comment = False
    in_text_block = False
    temp_file_name = file_name + '.tmp'

    with open(file_name, 'r') as file, open(temp_file_name, 'w') as temp_file:
        for line in file:
            line_strip = line.strip()

            # Skip single-line comments, multiline comments, package declarations, import statements
            if (line_strip.startswith('//') or 
                (line_strip.startswith('/*') and '*/' in line_strip) or 
                line_strip.startswith('package ') or 
                line_strip.startswith('import ')):
                temp_file.write(line)
                continue

            if line_strip.startswith('/*'):
                in_multiline_comment = True
            if in_multiline_comment:
                temp_file.write(line)
                if '*/' in line:
                    in_multiline_comment = False
                continue

            # Handle text blocks
            if '"""' in line_strip:
                in_text_block = not in_text_block

            # Skip processing if inside a text block
            if in_text_block:
                temp_file.write(line)
                continue

            if len(line) <= 120:
                temp_file.write(line)
                continue

            indent = 0
            while line[indent] in (' ', '\t'):
                indent += 1

            indentation = line[:indent]
            remaining_line = line[indent:].rstrip()

            while len(remaining_line) > 120:
                split_pos = 120
                while split_pos > 0 and remaining_line[split_pos] not in (' ', '\t', '.'):
                    split_pos -= 1

                # If there's no suitable split position, break the loop
                if split_pos == 0:
                    break

                wrapped_line = remaining_line[:split_pos]
                remaining_line = remaining_line[split_pos:].lstrip()

                if wrapped_line.endswith('.'):
                    remaining_line = '.' + remaining_line
                    wrapped_line = wrapped_line[:-1]

                temp_file.write(indentation + wrapped_line + '\n')
                indentation += '\t'

            temp_file.write(indentation + remaining_line + '\n')

    os.replace(temp_file_name, file_name)

def process_all_java_files_in_repository(repository_path):
    # Recursively find all Java files in the repository
    java_files = glob.glob(f"{repository_path}/**/*.java", recursive=True)
    
    for java_file in java_files:
        print(f"Processing {java_file}...")
        split_long_lines(java_file)
    print("Done processing all Java files.")

repository_path = "." # Replace with the root path of your repository
process_all_java_files_in_repository(repository_path)

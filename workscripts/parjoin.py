import argparse

parser = argparse.ArgumentParser(description='Join lines at paragraphs but ignore blank lines')
parser.add_argument('input_file', metavar='INPUT_FILE', help='path to input file')
parser.add_argument('output_file', metavar='OUTPUT_FILE', help='path to output file')
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    lines = f.readlines()

# Join paragraphs
i = 0
while i < len(lines) - 1:
    if lines[i] != '\n' and lines[i+1] != '\n':
        lines[i] = lines[i].rstrip() + ' ' + lines[i+1].lstrip()
        del lines[i+1]
    else:
        i += 1

with open(args.output_file, 'w') as f:
    f.writelines(lines)


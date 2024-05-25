def load_lookup(file_path):
    lookup_list = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by comma and strip any whitespace
            values = [value.strip() for value in line.strip().split(',')]
            lookup_list.append(values)
    
    return lookup_list

def check_substrings(given_string, lookup_list):
    matching_lines = []
    for values in lookup_list:
        if any(value.lower() in given_string.lower() for value in values):
            matching_lines.append(values)
    return matching_lines

def calculate_scores(matching_lines, file_path):
    scores = {}
    with open(file_path, 'r') as file:
        for line in file:
            score = 0
            for values in matching_lines:
                for value in values:
                    if value.lower() in line.lower():
                        score += 1
                        if line in scores:
                            scores[line] += 1
                        else:
                            scores[line] = 1
    return scores

def get_highest_score_lines(scores):
    highest_score = 0
    best_lines = []
    for line, score in scores.items():
        if score > highest_score:
            highest_score = score
            best_lines = [line]
        elif score == highest_score:
            best_lines.append(line)
    return best_lines, highest_score

# Load the lookup file
lookup_file_path = r'C:\Users\91700\Documents\levenstein distance\lookup.txt'
lookup_list = load_lookup(lookup_file_path)

source_file_path = r'C:\Users\91700\Documents\levenstein distance\source_file.txt'
check_file_path = r'C:\Users\91700\Documents\levenstein distance\check_file.txt'
output_file_path = r'C:\Users\91700\Documents\levenstein distance\output.txt'

s_file = open(source_file_path, 'r')
f=open(output_file_path, 'w')

for s_line in s_file:
    f.write('\n')
    matching_lines = check_substrings(s_line, lookup_list)

    if matching_lines:
        
        scores = calculate_scores(matching_lines, check_file_path)
        
        # Get the line with the highest score
        best_lines, highest_score = get_highest_score_lines(scores)

        
        if best_lines:
            f.write(s_line.strip() +': ')
            for i, line in enumerate(best_lines):
                f.write(line.strip())
                if i < len(best_lines) - 1:
                    f.write(', ')

        else:
            f.write(s_line.strip() +': no match')
    else:
        f.write(s_line.strip() +': no matching element in lookup')

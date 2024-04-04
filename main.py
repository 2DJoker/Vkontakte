import csv
from collections import defaultdict

def read_csv(read_and_print_values):

    data = []
    with open("variant1.csv", 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            data.append(row)
    return data


def find_best_days(filenames):
    best_days = defaultdict(lambda: {"timestamp": None, "value": float('-inf')})

    for filename in filenames:
        data = read_csv(filename)
        for row in data:
            if row['action'] in ('confirmation', 'checkout'):
                timestamp = row['timestamp'][:7]  
                value = float(row['value'])
                if value > best_days[timestamp]["value"]:
                    best_days[timestamp] = {"timestamp": row['timestamp'], "value": value}

    return best_days

def format_output(best_days):

    output = []
    for month, data in sorted(best_days.items()):
        if data["timestamp"] is not None:
            output.append(f"{data['timestamp'][:10]}\t{int(data['value'])}")
    return output

def main():
    filenames = ["variant1.csv"]  
    best_days = find_best_days(filenames)
    output = format_output(best_days)
    print("timestamp\tvalue")
    for line in output:
        print(line)

if __name__ == "__main__":
    main()

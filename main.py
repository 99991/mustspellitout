import csv

with open("ground_truth.csv") as f:
    reader = csv.reader(f)
    ground_truth = list(reader)

for filename in [
    "llama_70b_name_birth_year_odd.csv",
    "chatgpt_name_birth_year_odd.csv",
    "llama_70b_name_birth_year_birth_year_odd.csv",
    "chatgpt_name_birth_year_birth_year_odd.csv",
]:
    with open(filename) as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert len(rows) == 100

    num_correct = 0
    num_odd = 0

    for i, row in enumerate(rows):
        name = row[0]
        birth_year_odd = row[-1]

        true_name, true_birth_year = ground_truth[i]

        assert name == true_name

        correct = int(birth_year_odd.strip()) == int(true_birth_year) % 2

        num_correct += correct
        num_odd += int(birth_year_odd.strip())

    print(f"correct: {num_correct:3}, odd: {num_odd:3}, filename: {filename}")

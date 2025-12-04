import os

TESTS_DIR = "./tests"
OUTPUTS_DIR = "./results"

def main(input_file, output_file):

    with open(input_file, "r") as f:
        a, b = map(float, f.readline().split())

    answer = b + a

    with open(output_file, "w") as f:
        f.write(str(answer))

if __name__ == "__main__":

    for file in os.listdir(TESTS_DIR):
        if not file.endswith(".txt"):
            continue
        input_file = os.path.join(TESTS_DIR, file)
        output_file = os.path.join(OUTPUTS_DIR, file.replace(".txt","_out.txt"))
        main(input_file, output_file)

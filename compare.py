import os
import filecmp

class NotMatchException(Exception):
    def __init__(self, file_a, file_b):
        self.message = f'Files {file_a} and {file_b} not match'
        super().__init__(self.message)

def main():
    dir_a = "./program_a/results"
    dir_b = "./program_b/results"

    files = sorted(f for f in os.listdir(dir_a) if f.endswith("_out.txt"))
    
    for f in files:
        a_path = os.path.join(dir_a, f)
        b_path = os.path.join(dir_b, f)

        if not filecmp.cmp(a_path, b_path, shallow=False):
            raise NotMatchException(a_path, b_path)
        
    print("ALL TESTS PASSED!")

if __name__ == "__main__":
    main()
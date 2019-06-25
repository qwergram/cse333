import os
from subprocess import PIPE, Popen

BINARY_NAME = "ex0"

# Execute the binary with the given arguments and return the output strings
def execute(*args):
    args = " ".join([str(_) for _ in args])
    process = os.popen('./{} {}'.format(BINARY_NAME, args))
    preprocessed = process.read()
    process.close()
    return str(preprocessed.strip())

def executeAndReadErr(*args):
    args = " ".join([str(_) for _ in args])
    process = Popen('./{} {}'.format(BINARY_NAME, args), shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return str(stderr.strip().decode())

class Test:

    def __init__(self):
        pass

    def run(self):
        print("Starting tests.")
        for item in dir(self):
            if item.startswith("test_"):
                print("Testing:", item)
                getattr(self, item)()
        print("Testing complete.")

    def test_wrong_inputs(self):
        for i in [-1, "abc", 99999999999999999999999999999999999999999999999999999999999999]:
            assert executeAndReadErr(i) == "Usage: ./ex0 n, where n >= 0. Prints Pi estimated to n terms of the Nilakantha series.", \
                "instead was {}".format(executeAndReadErr("abc"))

    def test_specs(self):
        assert execute(100) == "Our estimate of Pi is 3.14159241097198238535", "instead was {}".format(execute(100))
        assert execute(0) == "Our estimate of Pi is 3.00000000000000000000", "instead was {}".format(execute(0))
        

if __name__ == "__main__":
    t = Test()
    t.run()
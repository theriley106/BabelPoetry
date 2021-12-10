import glob
import random
generated = []

for fileval in glob.glob("generated*.txt"):
    for val in open(fileval).read().split("<|startoftext|>"):
        poems = [""]
        x = list(val.partition("<|")[0])
        while len(x) > 0:
            if x[0] == "=":
                poems.append("")
            while len(x) > 0 and x[0] == "=":
                x.pop(0)
            poems[-1] += x.pop(0)

        generated += poems
all_vals = []
for val in generated:
    # print(len(val))
    if len(val) > 1:
        all_vals.append(val)



def generate():
    return random.choice(all_vals)

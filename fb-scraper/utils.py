import csv

# creating CSV header
def create_csv(filename):
    with open(filename, "w+", newline='', encoding="utf-8") as save_file:
        writer = csv.writer(save_file)
        writer.writerow(["Author", "uTime", "Text"])

# clean all non-alphanumberic characters       
def strip(string):
    words = string.split()
    words = [word for word in words if "#" not in word]
    string = " ".join(words)
    return string

def write_to_csv(filename, data):
    with open(filename, "a+", newline='', encoding="utf-8") as save_file:
        writer = csv.writer(save_file)
        writer.writerow(data)
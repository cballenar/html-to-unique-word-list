import re
source_file = open("source.txt","r")
source = source_file.readlines()

print("Reading {} lines...".format(len(source)))
output_set = set()

count = 0
for line in source:
    count += 1
    print("Reading line {}...".format(count))
    if line == "NULL\n": continue        # skip nulls
    line = re.sub("<[^<]+?>", " ", line) # strip html, replace with space to prevent merging of words
    line = re.sub("[^\w ]"  , " ", line) # remove symbols, replace with space to prevent merging of words
    line = re.sub("_"       , " ", line) # remove underscores, these are left behind by the above
    line = re.sub("[\d]"    , " ", line) # remove numbers, numbers aren't needed in dictionary
    words = line.split()                 # split into words
    for word in words:
        output_set.add(word)             # send to output_set

output_list = list(output_set)
output_list.sort()

with open("output.txt", "w") as output_file:
    for output_list_item in output_list:
        output_file.write("{}\n".format(output_list_item))

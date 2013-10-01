from sys import argv

script, filename = argv 

read_file = open(filename)
filetext = read_file.read()

lower_case = filetext.lower()

spaced_words = lower_case.split()

new_dict = {}

for item in spaced_words:
    # temp holds the character that gets stripped
    temp = item.strip(";,.?")
    #get returns the value of 'item', it does not return the key itself
    #get is using the item's key to find its value and incriment it up by 1
    new_dict[temp] = new_dict.get(temp, 0) + 1

for key, value in new_dict.iteritems():
    print "%s %r" % (key, value)

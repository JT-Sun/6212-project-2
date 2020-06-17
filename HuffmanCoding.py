# Huffman Coding in python
import time
import matplotlib.pyplot as plot
from matplotlib.pyplot import MultipleLocator

N = list(range(10000, 110000, 10000))

string_list = []
with open("1.txt", "r") as f:
    for i in N:
        char = f.read(i)
        char = char.replace("\n", "")
        string_list.append(char)
        print(len(char))


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def nodes(self):
        return (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.nodes()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


on_list = []
tn_list = []
for string in string_list:
    time1 = time.time_ns()
    # Calculating frequency
    freq1 = {} # dictionary {key: value, key2: value}
    for c in string:
        if c in freq1:
            freq1[c] += 1
        else:
            freq1[c] = 1

    freq = sorted(freq1.items(), key=lambda x: x[1], reverse=True)

    nodes = freq
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffmanCode = huffman_code_tree(nodes[0][0])


    time2 = time.time_ns()
    time3 = time2 - time1
    n = len(string)
    x = n*log(n,2)
    on_list.append(x)
    tn_list.append(time3)

    bit_dict = {}
    for char in huffmanCode:

        bit_dict [char] = freq1[char]* len(huffmanCode[char])
    xx = []
    for i in bit_dict:
        xx.append(bit_dict[i])
    a = sum(xx)
    # print('total bits of huffman coding =',a)

    print(' Char |   Huffman code   |  bits')
    print('---------------------------------')
    for (char, frequency) in freq:
        print(' %-4r |%12s|%12s' % (char, huffmanCode[char], bit_dict[char]))
    print('total bits of huffman coding =',a)


constant = sum(tn_list) / sum(on_list)
for i in range(len(on_list)):
    on_list[i] = on_list[i] * constant

x_major_locator=MultipleLocator(1)
plot.plot(on_list, label= "Adjusted Theoretical Result - adjustment constant=%s" % constant, color="red")
plot.plot(tn_list, label = "Experimental Result", color="blue")
plot.legend(loc="upper left")
plot.ylabel("time:ns")
plot.xlabel("n: input string length")
plot.xticks(range(len(N)), N, rotation=90)
plot.show()
plot.savefig("result.png")

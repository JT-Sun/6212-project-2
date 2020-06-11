# Huffman Coding in python

string = 'this is the test file for project 2: hoffman coding'

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def nodes(self):
        return (self.left, self.right)

    # def __str__(self):
    #     return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.nodes()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


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

####
bit_dict = {}
for char in huffmanCode:

    bit_dict [char] = freq1[char]* len(huffmanCode[char])
xx = []
for i in bit_dict:
    xx.append(bit_dict[i])
a = sum(xx)
print('total bits of huffman coding =',a)

####

print(' Char   |   Huffman code   |   bits')
print('---------------------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s|%12s' % (char, huffmanCode[char], bit_dict[char]))

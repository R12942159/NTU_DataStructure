import argparse
import time


class MyNode(object):
    # this class infor testing
    # Do Not Modify
    def __init__(self, value):
        self.value = value
        self.right = self
        self.left = self

    def __repr__(self):
        return 'Node%s' % (self.value)


class MyStack(object):
    def __init__(self):
        self.num_element = 0
        self.root = MyNode(None)

    def pop(self):
        if self.num_element == 0:
            raise ValueError('Can not execute pop() on an empty stack')
        else:
            self.num_element -= 1
            # ---TODO:
            # Connect the second last element >> root
            # Connect root >> the second last element
            # ---
            top_node = self.root.left  # Node to pop is the current top
            self.root.left = top_node.left  # The root's left should now point to the node before the top
            top_node.left.right = self.root  # Setting the right of the second last node to root

    def push(self, node):
        self.num_element += 1
        # ---TODO:
        # Connect the last element >> inserted node
        # Connect the inserted node >> root
        # ---
        last_node = self.root.left  # Node that is currently at the end
        node.left = last_node  # New node's left should point to the current end node
        node.right = self.root  # New node's right should point to the root
        last_node.right = node  # The end node's right should now point to the new node
        self.root.left = node  # Root's left should point to the new node


    def __repr__(self):
        ret = ''
        node = self.root.right
        while node != self.root:
            ret = ret + '>>' + str(node)
            node = node.right
        return ret


def main(input_file, output_file, has_ofile):
    myStack = MyStack()

    ifile = open(input_file)
    if has_ofile:
        ofile = open(output_file, 'w')
    else:
        ofile = None
    for line in ifile.readlines():
        items = line.strip().split(" ")
        if items[0] == 'PUSH':
            myVal = int(items[1])
            myStack.push(MyNode(myVal))
        else:
            myStack.pop()
        if has_ofile:
            ofile.write(str(myStack) + '\n')

        # testing output
        # print(str(myStack) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='./input_1.txt')
    parser.add_argument('--output', default='')
    args = parser.parse_args()
    if len(args.output) > 0:
        has_ofile = True
    else:
        has_ofile = False
    ts = time.time()
    main(args.input, args.output, has_ofile)
    te = time.time()
    if not has_ofile:
        print('stack.py run time of %s: %.5fs' % (args.input, te - ts))
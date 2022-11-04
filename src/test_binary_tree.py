import pytest
from .binary_tree import Node

def test_show_node(capfd):
	node = Node("test")	
	node.show_node()	
	out, _ = capfd.readputerr()
	assert out == "test"



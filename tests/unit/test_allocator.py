import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/main/python')))
from allocator import get_namespace_costs

def test_get_namespace_costs():
    costs = get_namespace_costs()
    assert "backend-team" in costs
    assert costs["backend-team"]["cpu_cost"] == 1.50
    assert costs["backend-team"]["mem_cost"] == 0.80
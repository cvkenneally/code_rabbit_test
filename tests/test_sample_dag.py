import pytest
from src.sample_dag import task_1

def test_task_1():
    assert task_1() == 'Task 1 complete.'
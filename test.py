import subprocess
import re

name = "lab_for.sh" 

def test_reverse_arguments():
    command = ['bash', name, 'a', 'b', 'c']
    result = subprocess.run(command, stdout=subprocess.PIPE)
    assert re.fullmatch(r'c b a\s*', result.stdout.decode("utf-8"))

def test_empty_arguments():
    command = ['bash', name]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    assert re.fullmatch(r'\s*', result.stdout.decode("utf-8")) 

def test_single_argument():
    command = ['bash', name, 'a']
    result = subprocess.run(command, stdout=subprocess.PIPE)
    assert re.fullmatch(r'a\s*', result.stdout.decode("utf-8"))

from headtail import *
import subprocess
import pytest


def capture(command):               # got capture() from code0mavin.com (https://code-maven.com/slides/python/pytest-test-cli)
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    out,err = proc.communicate()
    return out, err, proc.returncode


# verify there is help string and that it contains references to 'filename' and the start & end options
def test_headtail_help():
    command = ["python", "headtail.py", "-h"]
    out, err, exitcode = capture(command)
    idx_filename = out.find(b'filename')
    idx_start = out.find(b'--start')
    idx_end = out.find(b'-e')
    assert idx_filename > 0
    assert idx_start > 0
    assert idx_end >0
    assert err == b''
    assert exitcode == 0

# just run the defaults to verify the simple case works
def test_headtail_defaults(tmp_path):

    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()
    s = b'line 1\r\nline 2\r\nline 3\r\nline 4\r\nline 5\r\nline 6\r\nline 7\r\nline 8\r\nline 9\r\nline 10\r\nline 11\r\nline 12'
    with open(test_directory / 'samplefile.txt', 'wb') as f:
        f.write(s)
    samplefile = str(test_directory / 'samplefile.txt')  

    command = ["python", "headtail.py", samplefile]
    out, err, exitcode = capture(command)
    assert out == b'line 1\r\nline 2\r\nline 3\r\nline 10\r\nline 11\r\nline 12'
    assert err == b''
    assert exitcode == 0

def test_headtail_no_head(tmp_path):
    
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()
    s = b'line 1\r\nline 2\r\nline 3\r\nline 4\r\nline 5\r\nline 6\r\nline 7\r\nline 8\r\nline 9\r\nline 10\r\nline 11\r\nline 12'
    with open(test_directory / 'samplefile.txt', 'wb') as f:
        f.write(s)
    samplefile = str(test_directory / 'samplefile.txt') 

    command = ["python", "headtail.py", "samplefile.txt", "-s 0"]
    out, err, exitcode = capture(command)
    assert out == b'line 10\r\nline 11\r\nline 12'
    assert err == b''
    assert exitcode == 0

def test_headtail_no_tail(tmp_path):
    
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()
    s = b'line 1\r\nline 2\r\nline 3\r\nline 4\r\nline 5\r\nline 6\r\nline 7\r\nline 8\r\nline 9\r\nline 10\r\nline 11\r\nline 12'
    with open(test_directory / 'samplefile.txt', 'wb') as f:
        f.write(s)
    samplefile = str(test_directory / 'samplefile.txt') 

    command = ["python", "headtail.py", "samplefile.txt", "-e 0"]
    out, err, exitcode = capture(command)
    assert out == b'line 1\r\nline 2\r\nline 3\r\n'
    assert err == b''
    assert exitcode == 0

def test_headtail_no_lines_requested(tmp_path):
    
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()
    s = b'line 1\r\nline 2\r\nline 3\r\nline 4\r\nline 5\r\nline 6\r\nline 7\r\nline 8\r\nline 9\r\nline 10\r\nline 11\r\nline 12'
    with open(test_directory / 'samplefile.txt', 'wb') as f:
        f.write(s)
    samplefile = str(test_directory / 'samplefile.txt') 

    command = ["python", "headtail.py", "samplefile.txt", "-e 0", "-s 0"]
    out, err, exitcode = capture(command)
    assert out == b''
    assert err == b''
    assert exitcode == 0

# the entire file should be returned, but not copies of the file, if more lines are requested than are in the file
def test_headtail_too_many_lines_requested(tmp_path):
    
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()
    s = b'line 1\r\nline 2\r\nline 3\r\nline 4\r\nline 5\r\nline 6\r\nline 7\r\nline 8\r\nline 9\r\nline 10\r\nline 11\r\nline 12'
    with open(test_directory / 'samplefile.txt', 'wb') as f:
        f.write(s)
    samplefile = str(test_directory / 'samplefile.txt') 

    command = ["python", "headtail.py", "samplefile.txt", "-e 100", "-s 100"]
    out, err, exitcode = capture(command)
    assert out == b'line 1\r\nline 2\r\nline 3\r\nline 4\r\nline 5\r\nline 6\r\nline 7\r\nline 8\r\nline 9\r\nline 10\r\nline 11\r\nline 12'
    assert err == b''
    assert exitcode == 0

# try to sneak in a non-integer option
def test_headtail_nonInteger_option(tmp_path):
    
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()
    s = b'line 1\r\nline 2\r\nline 3\r\nline 4\r\nline 5\r\nline 6\r\nline 7\r\nline 8\r\nline 9\r\nline 10\r\nline 11\r\nline 12'
    with open(test_directory / 'samplefile.txt', 'wb') as f:
        f.write(s)
    samplefile = str(test_directory / 'samplefile.txt') 

    command = ["python", "headtail.py", "samplefile.txt", "-s O"]
    out, err, exitcode = capture(command)
    idx = err.find(b'invalid int value')
    assert idx > 0
    assert exitcode == 2

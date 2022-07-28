import subprocess


def execute(cmd, encoding="UTF-8", timeout=None, shell=False):
    """Execute a shell command/binary.
    If you are using this function in a script ran by a priviliged user,
    be careful as to what your are executing.
    Arguments:
    cmd:        List[str] -- splitted command (ex: ['ls', '-la', '~'])
    encoding:   str (default: 'UTF-8') -- used for decoding the command output
    timeout:    int (default: None) -- in seconds, raises TimeoutExpired
    result: a tuple coontaining stdout, the returncode and stderr
    """

    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=shell,
    )
    output, error = proc.communicate(timeout=timeout)
    output = output.decode(encoding).rstrip()
    error = error.decode(encoding).rstrip()
    rc = proc.returncode
    return (output, rc, error)

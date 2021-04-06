import sys, os, hashlib, pathlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..' )))
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import dpdispatcher
# from dpdispatcher.local_context import LocalSession
from dpdispatcher.local_context import LocalContext
# from dpdispatcher.local_context import local_context
from dpdispatcher.lazy_local_context import LazyLocalContext
from dpdispatcher.ssh_context import SSHSession
from dpdispatcher.ssh_context import SSHContext
# from dpgen.dispatcher.Dispatcher import FinRecord
from dpdispatcher.JobStatus import JobStatus
from dpdispatcher.pbs import PBS
from dpdispatcher.slurm import Slurm
from dpdispatcher.local_context import _identical_files
from dpdispatcher.submission import Submission, Job, Task, Resources

def setUpModule():
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

def get_file_md5(file_path):
    return hashlib.md5(pathlib.Path(file_path).read_bytes()).hexdigest()
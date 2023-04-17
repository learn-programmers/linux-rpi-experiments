import cProfile
import re

def run_re():
    re.compile("foo|bar")

cProfile.run("run_re()")

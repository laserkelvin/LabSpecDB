"""
    generate_catalog.py

    Script that will generate a new catalog entry with a given `.var` file.
    This will ensure that the parameters for intensity generation and whatnot
    are standardized, and also moves the resulting catalog files into the right
    place.
"""

from subprocess import Popen, PIPE


def run_spcat(filename):
    # Function that will call SPCAT. This is a lower level function which does
    # not factor in the partition function
    command = [
        "spcat",
        filename + ".int",
        filename + ".var"
    ]
    # Run SPCAT
    with Popen(command, stdout=PIPE) as spcat:
        output, error = spcat.communicate()
    return output, error


def format_int(filename, dipoles=[0., 0., 0.], q=1000.):
    # Formats a .int file. The only required input is the filename and the
    # dipole moments
    with open("../input/template.int")

def call_spcat(filename):
    # Function

    process = subprocess.Popen(["spcat", filename + ".int", parameter_file],
                     stdout=subprocess.PIPE            # suppress stdout
                     )
    process.wait()
    # Extract the partition function at the specified temperature
    if temperature is not None:
        # Read in the piped standard output, and format into a list
        stdout = str(process.communicate()[0]).split("\\n")
        for line in stdout:
            if temperature in line:
                # If the specified temperature is found, get the partition
                # function
                Q = float(line.split()[1])
        return Q

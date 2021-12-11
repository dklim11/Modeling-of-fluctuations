from Pendulum_objects import pendulum

def read_parameters_of_pendulum_from_file(input_filename, pend):
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # pass empty lines and lines with commits
            else:
                parse_parameters(line, pend)
    return pend


def parse_parameters(line, pend):
    """Read data of pendulum from line. Line must have next view:
    <x0> <k> <A> <alpha0> <v0> <w0> <mu/m> <A4> <B> <C> <D> <E>

    x0 - initial length of spring without deformatiom
    k - asperity of spring
    A - amplitude of motor fluctuations
    alpha0 - the start-up angle
    v0 - initial speed of body along the rod
    w0 - initial angular speed of body
    mu/m - ratio coefficient of friction to mass
    A4 - coefficient at t^4
    B - coefficient at t^3
    C - coefficient at t^2
    D - coefficient at t
    E - free member
    fi is function of time. fi specifies phase change of motor. fi is polynomial of degree 4. fi = A_4t^4 + Bt^3 + Ct^2 + Dt + E

    Parameters of function:

    **line** — line with description of pendulum's parameters
    **pend** - object of class pendulum
    """
    line_prepared = line.strip()
    line_internals = line_prepared.split()

    pend.x0 = int(line_internals[0])
    pend.k = int(line_internals[1])
    pend.A = int(line_internals[2])
    pend.alpha0 = float(line_internals[3])
    pend.v0 = int(line_internals[4])
    pend.w0 = float(line_internals[5])
    pend.mu_m = float(line_internals[6])
    pend.A4 = float(line_internals[7])
    pend.B = float(line_internals[8])
    pend.C = float(line_internals[9])
    pend.D = float(line_internals[10])
    pend.E = float(line_internals[11])

pend = pendulum(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
read_parameters_of_pendulum_from_file('Desktop\Labs Python\Modeling-of-fluctuations\input.txt', pend)
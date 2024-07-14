import re
import matplotlib.pyplot as plt

def parse_namd_log(log_file):
    # Regular expressions to match lines in the log file
    energy_re = re.compile(
        r"^ENERGY:\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)"
    )

    # Lists to hold the parsed data
    steps = []
    bond_energies = []
    kinetic_energies = []
    total_energies = []
    temperatures = []

    # Open and parse the log file
    with open(log_file, 'r') as file:
        for line in file:
            match = energy_re.match(line)
            if match:
                steps.append(int(match.group(1)))
                bond_energies.append(float(match.group(2)))
                kinetic_energies.append(float(match.group(7)))
                total_energies.append(float(match.group(11)))
                temperatures.append(float(match.group(10)))

    return steps, bond_energies, kinetic_energies, total_energies, temperatures

def plot_energies(steps, bond_energies, kinetic_energies, total_energies, temperatures):
    plt.figure(figsize=(14, 8))

    # Plot bond energies
    plt.plot(steps, bond_energies, label='Bond Energy', color='blue')

    # Plot kinetic energies
    plt.plot(steps, kinetic_energies, label='Kinetic Energy', color='orange')

    # Plot temperatures
    plt.plot(steps, temperatures, label='Temperature', color='red')

    # Plot total energies
    plt.plot(steps, total_energies, label='Total Energy', color='green')

    plt.xlabel('Steps')
    plt.ylabel('Energy (kcal/mol) / Temperature (K)')
    plt.title('NAMD Simulation Energies and Temperature')
    plt.legend()
    plt.grid(True)
    plt.show()

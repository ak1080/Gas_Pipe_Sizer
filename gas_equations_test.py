"""
This module is intended to be used for testing. I'm NOT actually importing it into the main gas_pipe_calcs module.
The equations for low pressure and high pressure in the plumbing code are solving for diameter.
My table in the gas_calculator module is solving for capacity (had to rearrange equations).

I want this to be a separate calculator that solves for diameter, so I can check table values.

"""

PSI_TO_INWC = 27.7
# Dictionary of pipe sizes
metallic_pipe_sizes = {
    0.5: 0.622, 0.75: 0.824, 1: 1.049, 1.25: 1.380, 1.5: 1.610, 2: 2.067, 2.5: 2.469,
    3: 3.068, 4: 4.026, 5: 5.047, 6: 6.065,
}

def req_pipe_diam(inlet_pressure_psi, capacity_cfh, press_drop_inwc, length, gas_type):
    if gas_type.lower() == 'natural':
        Cr = 0.6094
        Y = 0.9992
    elif gas_type.lower() == 'propane':
        Cr = 1.2462
        Y = 0.9910
    else:
        raise ValueError("Invalid gas type.")
    # Condition for using low pressure equation (less than 1.5 psi incoming)
    if inlet_pressure_psi < 1.5:
        pipe_diam = capacity_cfh**0.381 / (19.17 * (press_drop_inwc / (Cr * length))**0.206)
    else:
        P1 = inlet_pressure_psi + 14.7
        P2 = P1 - press_drop_inwc / PSI_TO_INWC
        pipe_diam = capacity_cfh**0.381 / (18.93 * (((P1**2 - P2**2) * Y) / (Cr*length))**0.206)

    return round(pipe_diam, 4)

# User can modify inputs to the req_pipe_diam function here. Be careful with units!
pipe_diam = req_pipe_diam(inlet_pressure_psi=4, capacity_cfh=1260, press_drop_inwc=2.5*PSI_TO_INWC, length=700, gas_type='natural')
print(pipe_diam)



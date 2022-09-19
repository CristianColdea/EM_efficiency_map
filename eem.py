"""
Script for Electric Motor Efficiency computation.
"""

def eem(t_max, omg_max, t, omg, type='IPM', t_const=False, P_const=False):
    """
    Function to compute efficiency based on regression.
    Takes as inputs maximum torque, maximum speed/rpm, instantaneous torque and speed,
    EM type, wether the motor works in constant torque or power regimes.
    Outputs the EM efficiency on the given conditions.
    """
    if(t_const or P_const):  # if EM is under constant torque or power regimes
        if(type == 'IPM'):
            efficiency = 1
        else: print("Two equation fitting is computed for IPM motor type only.")
    else:
        if(type == 'SPM'):
            efficiency = 2 2 

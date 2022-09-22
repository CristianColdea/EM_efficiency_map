"""
Script for Electric Motor Efficiency computation.
"""

def eem(t, omg, type='IPM', t_const=False, P_const=False):
    """
    Function to compute efficiency based on regression.
    Takes as inputss instantaneous torque and speed,
    EM type, wether the motor works in constant torque or power regime.
    Outputs the EM efficiency on the given conditions.
    """
    if(t_const or P_const):  # if EM is under constant torque or power regimes
        if(type == 'IPM'):
            # loss for the constant torque working regime
            if(t_const):
                loss = -0.004 + (0.117 * omg) + (0.175 * t) - 
                       (0.316 * (omg**2)) - (0.028 * t * omg) + (0.64 * (t**2)) +
                       (0.131 * (omg**3)) + (0.8 * (omg**2) * t) -
                       (0.034 * (t**2) * omg) + (0.084 * (t**3))
            # loss for the constant power working regime
            if(P_const):
                loss = 0.103 - (0.647 * omg) + (0.958 * t) + (1.2 * (omg**2)) -
                       (1.547 * t * omg) - (0.944 * (t**2)) -
                       (0.626 * (omg**3)) + (0.728 * (omg**2) * t) +
                       (1.466 * (t**2) * omg) + (1.008 * (t**3))
        else: print("Two equation fitting is computed for IPM motor type only.")
    else:
        if(type == 'SPM'):
            loss = -0.002 + (0.175 * omg) - (0.065 * t) + (0.181 * (omg**2)) +
                   (0.577 * t * omg) + (0.697 * (t**2)) + (0.443 * (omg**3)) -
                   (0.542 * (omg**2) * t) - (1.043 * (t**2) * omg) +
                   (0.942 * (t**3))
        if(type == 'IPM'):
            loss = -0.033 + (0.239 * omg) + (0.47 * t) - (0.334 * (omg**2)) -
                   (1.022 * t * omg) + (0.103 * (t**2)) + (0.171 * (omg**3)) +
                   (0.534 * (omg**2) * t) + (1.071 * (t**2) * omg) +
                   (0.339 * (t**3))
    
    return (t * omg * (11 / 105000)) / (t * omg * (11 / 105000) + loss)

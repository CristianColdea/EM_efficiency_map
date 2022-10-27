"""
Script for Electric Motor (EM) Efficiency computation.
"""

import sys

def eem(T_inst, n, T_ovr, type='IPM', T_const=False, P_const=False):
    """
    Function to compute efficiency based on regression.
    Takes as inputs instantaneous torque, in Newton x meter
    and speed, in krpm, overload torque capability,
    in Newton x meter, EM type, wether the motor works in
    constant torque or power regime.
    Outputs the EM efficiency on the given conditions.
    """

    # check for the instant torque in relation to overload
    if(T_inst > T_ovr):
        sys.exit("The instantaneous torque cannot exceed overload capability")
    else:
        T = T_inst / T_ovr
        if(T_const or P_const):  # if EM is under constant torque or power regimes
            if(type == 'IPM'):
                # loss for the constant torque working regime
                if(T_const):
                    loss = (-0.004 + (0.117 * n) + (0.175 * T) - 
                           (0.316 * (n**2)) - (0.028 * T * n) + (0.64 * (T**2)) +
                           (0.131 * (n**3)) + (0.8 * (n**2) * T) -
                           (0.034 * (T**2) * n) + (0.084 * (T**3)))
                # loss for the constant power working regime
                if(P_const):
                    loss = (0.103 - (0.647 * n) + (0.958 * T) + (1.2 * (n**2)) -
                           (1.547 * T * n) - (0.944 * (T**2)) -
                           (0.626 * (n**3)) + (0.728 * (n**2) * T) +
                           (1.466 * (T**2) * n) + (1.008 * (T**3)))
            else: print("Two equation fitting is computed for IPM motor type only.")
        else:
            if(type == 'SPM'):
                loss = (-0.002 + (0.175 * n) - (0.065 * T) + (0.181 * (n**2)) +
                       (0.577 * T * n) + (0.697 * (T**2)) + (0.443 * (n**3)) -
                       (0.542 * (n**2) * T) - (1.043 * (T**2) * n) +
                       (0.942 * (T**3)))
            if(type == 'IPM'):
                loss = (-0.033 + (0.239 * n) + (0.47 * T) - (0.334 * (n**2)) -
                       (1.022 * T * n) + (0.103 * (T**2)) + (0.171 * (n**3)) +
                       (0.534 * (n**2) * T) + (1.071 * (T**2) * n) +
                       (0.339 * (T**3)))

    print("The loss is: ", loss, " [kW]")
    
    return (T * n * (1 / 9550)) / (T * n * (1 / 9550) + loss)

print(eem(150, 8500))

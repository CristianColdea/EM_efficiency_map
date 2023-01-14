# Electric Motor (EM) efficiency map model
> This is a project for model the electric motor efficiency map based on a published scientific paper.

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
* The final objective is to have a script/module able to deliver the efficiency value for a certain electric motor working on a specific torque and speed/rpm.
* This is necessary for a Hybrid Electric Vehicle (HEV) Reinforcement Learning optimization.
* CAVEAT_1 The regression coefficients were normalised to base values (i.e. torque overload and maximum speed), which are mostly inherent to the electric motor.
* CAVEAT_2 The script covers the situation of motor operating under constant torque and power. The user must be sure the motor works under this regimes     indeed. Moreover, the  motor speed border between the two aforementioned working regimes must be known (e.g., (3-3.3) kr/min as upper limit of constant   torque regime).

## Screenshots
![Example screenshot](EM_efficiency.png)

## Technologies
* Plain _Python_ and some of its specialized lybraries.

## Setup
* Keep the scripts and files in the same folder.

## Code Examples
Show examples of usage:
* Import the script as a _Python_ module.
```
import eem.py as eem
```
* Call the efficiency function within the module with the appropriated args.
```
efficiency = eem.eem(arg1, arg2, ...)
```

## Features
List of features ready and TODOs for future development:
* The loss function for both IPM and ISM motor types, operating under one regime (i.e., no constant torque or power regimes) are covered already in the     script.

To-do list:
* ~~Understand the EM model~~.
* ~~Efficiency is computed based on regression => we need a function(s) to implement the regressor so efficiency could be delivered continuously across speed     and torque ranges~~.
* ~~Implement regressor for IPM and ISM motor types, operating under one regime~~.
* ~~Implement regressors for IPM motor type, operating under constant torque and power regimes (one regressor for each regime)~~.
* ~~Test the script.~~


## Status
* Project is: _finished_.

## Inspiration
https://www.researchgate.net/publication/308830029_Efficiency_maps_of_electrical_machines

## Contact
rdt333@gmail.com - feel free to contact me!

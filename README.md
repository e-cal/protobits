# Protobits

> [WIP]; stale atm

_Protobits_ is my take on an artificial life simulation.

The agents (protobits) are able to learn over the course of their lifetime, through
a reinforcement learning powered brain, and over generations through reproduction
passing down and mutating a genome.

## Plan

- protobit actions
  - multiple decision points:
    - empty space: move? direction? velocity?
    - food: eat? carry/drop?
    - protobit: attack? reproduce?

Variables:
location (x,y)
direction (degrees)
velocity

Actions:
adjust variable
eat / carry / drop
attack / reproduce

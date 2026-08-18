# Pendulum Timing and Gravitational Acceleration Measurement

## Overview
A simple pendulum rig using a raspberry pi pico 2WW and IR beam break light gate to measure the oscillation period via interrupt-driven timing, then derive the local gravitational acceleration (g) from the pendulum period formula, with the full uncertainty propagation from raw timing data through to final result.

## Motivation
This originated for a PH320 Lab assignment done in  the University of Strathclyde, measuring pendulum period via a light gate. This project extends that with an independent analysis pipeline: satistical treatment of raw timing data, propagation of measurement uncertainty into the derived value of g, and a comparison against a known local reference value.

## Method
**Data Collection
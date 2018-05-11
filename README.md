# TextToLED

A package to control a 5x5x5 LED cube using a CMOD S6 FPGA device and a Raspberry Pi.

Sends bit strings from RasPi to FPGA. Signals are mutliplexed and forwarded to LED cube.

Cube is built with 25 columns and 5 layers. Each column is powered by a unique VCC pin. Each layer is grounded to a unique 0V pin.

When a 5V signal is sent to a specific column, and a 0V signal is sent to a specific layer, a single LED can be illuminated.

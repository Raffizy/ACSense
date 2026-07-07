import ctypes
import mmap
import time
import tkinter as tk
from pydualsense import *


class SPageFilePhysics(ctypes.Structure):
    _fields_ = [
        ("packetId", ctypes.c_int),
        ("gas", ctypes.c_float),
        ("brake", ctypes.c_float),
        ("fuel", ctypes.c_float),
        ("gear", ctypes.c_int),
        ("rpms", ctypes.c_int),
        ("steerAngle", ctypes.c_float),
        ("speedKmh", ctypes.c_float),
    ]


mm = mmap.mmap(0, ctypes.sizeof(SPageFilePhysics), "acpmf_physics")


ds = pydualsense()
ds.init()



print("Drive Simulation prototype")

ds.triggerR.setMode(TriggerModes.Rigid)
ds.triggerL.setMode(TriggerModes.Rigid)


while not ds.state.R1:

    #telemetry
    physics = SPageFilePhysics.from_buffer_copy(mm)

    rpm = physics.rpms
    brake = physics.brake
    gas = physics.gas
    speed = physics.speedKmh
    #debug
    time.sleep(1)
    print(f"Speed: {speed:.1f} | RPM: {rpm} | Gas: {gas:.2f} | Brake: {brake:.2f}")

    


    #brake_force = int(brake * 1)
    #brake_force = max(0, min(255, brake_force))

    #gas_force = int((gas ** 1.5) * 200)  # smoother curve
    #gas_force = max(0, min(255, gas_force))


    ds.triggerL.setForce(1, 240)
    ds.triggerR.setForce(1, 250)

    time.sleep(0.01)


ds.triggerR.setMode(TriggerModes.Off)
ds.triggerL.setMode(TriggerModes.Off)
time.sleep(0.02)
ds.close()

print("Device Closed")


import ctypes
import mmap
import time
from tkinter import *
from pydualsense import *


# Assetto Corsa telemetry structure
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


# Connect to Assetto Corsa shared memory
mm = mmap.mmap(0, ctypes.sizeof(SPageFilePhysics), "acpmf_physics")


# ---------------- GUI ---------------- #

root = Tk()
root.geometry("180x150")
root.title("Trigger Tester")

Label(root, text="Left Bump").grid(row=0, column=0)
Label(root, text="Right Bump").grid(row=0, column=1)

LeftBump = Scale(root, from_=255, to=0)
RightBump = Scale(root, from_=255, to=0)

LeftBump.grid(row=1, column=0, padx=20, pady=10)
RightBump.grid(row=1, column=1, padx=20, pady=10)


# ------------- DualSense ------------ #

ds = pydualsense()
ds.init()

ds.triggerL.setMode(TriggerModes.Rigid)
ds.triggerR.setMode(TriggerModes.Rigid)

print("Drive Simulation Prototype")
print("Press R1 to exit")


# -------------- Main Loop ------------ #

while not ds.state.R1:
    root.update()

    physics = SPageFilePhysics.from_buffer_copy(mm)

    rpm = physics.rpms
    brake = physics.brake
    gas = physics.gas
    speed = physics.speedKmh

    ds.triggerL.setForce(1, LeftBump.get())
    ds.triggerR.setForce(1, RightBump.get())

    print(
        f"Speed: {speed:.1f} | "
        f"RPM: {rpm} | "
        f"Gas: {gas:.2f} | "
        f"Brake: {brake:.2f}"
    )

    time.sleep(0.01)


# -------------- Cleanup -------------- #

ds.triggerL.setMode(TriggerModes.Off)
ds.triggerR.setMode(TriggerModes.Off)

time.sleep(0.02)

ds.close()
root.destroy()

print("Device Closed")

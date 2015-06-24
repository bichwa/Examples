#Scratch_n_sketch scripting

b = scratch_n_sketch()
b.connect('com16')

b.sensorData()
console(b.A1)

b.disconnect()
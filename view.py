from diode_experiment import DiodeExperiment

# file diode_experiment ivoke
port = "ASRL5::INSTR"
experiment = DiodeExperiment(port = port)
experiment.scan(start = 0, stop = 1024)
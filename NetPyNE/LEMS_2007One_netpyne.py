'''
NetPyNE simulator compliant export for:

Components:
    RS (Type: izhikevich2007Cell:  v0=-0.06 (SI voltage) k=7.0E-7 (SI conductance_per_voltage) vr=-0.06 (SI voltage) vt=-0.04 (SI voltage) vpeak=0.035 (SI voltage) a=30.0 (SI per_time) b=-2.0E-9 (SI conductance) c=-0.05 (SI voltage) d=1.0E-10 (SI current) C=1.0E-10 (SI capacitance))
    RS_Iext (Type: pulseGenerator:  delay=0.0 (SI time) duration=0.52 (SI time) amplitude=1.0E-10 (SI current))
    net1 (Type: network)
    sim1 (Type: Simulation:  length=0.52 (SI time) step=1.0E-6 (SI time))


    This NetPyNE file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.4.6
         org.neuroml.model   v1.4.6
         jLEMS               v0.9.8.6

'''
# Main NetPyNE script for: net1

# See https://github.com/Neurosim-lab/netpyne

from netpyne import sim  # import netpyne sim module


###############################################################################
# NETWORK PARAMETERS
###############################################################################

netParams = {}  # dictionary to store sets of network parameters

# Cell properties list
netParams['cellParams'] = []

next_gid = 0
gids = {} # Require these in this file for plotting etc.

     
# cell params for cell RS in population RS_pop
cellRule = {'label': 'RS_pop', 'conditions': {'cellType': 'RS'}, 'sections': {}}
RS_pop_soma = {'geom': {}, 'topol': {}, 'mechs': {}, 'pointps':{}, 'syns': {}}  #  soma
RS_pop_soma['pointps']['RS'] = { 'mod':'RS', 'v0':-60.0,  'k':7.0E-4,  'vr':-60.0,  'vt':-40.0,  'vpeak':35.0,  'a':0.030000001,  'b':-0.0019999999,  'c':-50.0,  'd':0.1,  'C':1.00000005E-4,  } 

# Todo: work this out here from area etc.
cm = (318309 * RS_pop_soma['pointps']['RS']['C'] if RS_pop_soma['pointps']['RS'].has_key('C') else 318.31927 )

RS_pop_soma['geom'] = {'diam': 10, 'L': 10, 'Ra': 1, 'cm': cm}

cellRule['sections'] = {'soma': RS_pop_soma}  # add sections to dict
netParams['cellParams'].append(cellRule)  # add dict to list of cell properties

      
# Population parameters

netParams['popParams'] = []  # create list of populations - each item will contain dict with pop params


# Population: RS_pop, size: 1, component: RS

size_RS_pop = 1
netParams['popParams'].append({'popLabel': 'RS_pop', 'cellModel': 'RS_pop', 'cellType': 'RS', 'numCells': size_RS_pop}) # add dict with params for this pop 
gids['RS_pop'] = [i+next_gid for i in range(size_RS_pop)]
next_gid += size_RS_pop



# Inputs...
# Input: RS_Iext0 which is RS_Iext on cell 0 in RS_pop

RS_pop_soma['pointps']['RS_pop'] = { 'mod':'RS_Iext' } 



# SIMULATION PARAMETERS

simConfig = {}  # dictionary to store simConfig

# Simulation parameters
simConfig['duration'] = simConfig['tstop'] = 520.0 # Duration of the simulation, in ms
simConfig['dt'] = 0.001 # Internal integration timestep to use
simConfig['randseed'] = 1 # Random seed to use
simConfig['createNEURONObj'] = 1  # create HOC objects when instantiating network
simConfig['createPyStruct'] = 1  # create Python structure (simulator-independent) when instantiating network
simConfig['verbose'] = True  # show detailed messages 

# Recording 
simConfig['recordCells'] = [0]  
simConfig['recordTraces'] = {'Vsoma':{'sec':'soma','loc':0.5,'var':'v'}}

simConfig['plotCells'] = []
# Display id: d1
# Line id: RS v; displaying v on cell: 0 in population: RS_pop;
if 'v'=='v':
    simConfig['plotCells'].append(gids['RS_pop'][0]) # plot recorded traces for this list of cells

simConfig['recordStim'] = True  # record spikes of cell stims
simConfig['recordStep'] = simConfig['dt'] # Step size in ms to save data (eg. V traces, LFP, etc)



# Analysis and plotting 
simConfig['plotRaster'] = True # Whether or not to plot a raster
simConfig['plotLFPSpectrum'] = False # plot power spectral density
simConfig['maxspikestoplot'] = 3e8 # Maximum number of spikes to plot
simConfig['plotConn'] = False # whether to plot conn matrix
simConfig['plotWeightChanges'] = False # whether to plot weight changes (shown in conn matrix)
#simConfig['plot3dArch'] = True # plot 3d architecture

# Saving
simConfig['filename'] = 'net1.txt'  # Set file output name
simConfig['saveFileStep'] = simConfig['dt'] # step size in ms to save data to disk
simConfig['saveDat'] = True # save to dat file


print("Running a NetPyNE based simulation for %sms (dt: %sms)"%(simConfig['duration'], simConfig['dt']))
sim.createAndSimulate(                   
    simConfig = simConfig, 
    netParams = netParams)

print("Finished simulation")

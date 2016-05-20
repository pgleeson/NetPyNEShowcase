"""
params.py 

netParams is a dict containing a set of network parameters using a standardized structure

simConfig is a dict containing a set of simulation configurations using a standardized structure

Contributors: salvadordura@gmail.com
"""

netParams = {}  # dictionary to store sets of network parameters
simConfig = {}  # dictionary to store sets of simulation configurations


###############################################################################
#
# MPI HH TUTORIAL PARAMS
#
###############################################################################

###############################################################################
# NETWORK PARAMETERS
###############################################################################

pop_size = 3

# Population parameters
netParams['popParams'] = []  # create list of populations - each item will contain dict with pop params
netParams['popParams'].append({'popLabel': 'PYR_HH', 'cellModel': 'HH', 'cellType': 'PYR', 'numCells': pop_size}) # add dict with params for this pop 
netParams['popParams'].append({'popLabel': 'PYR_Izhi', 'cellModel': 'Izhi2007b', 'cellType': 'PYR', 'numCells': pop_size}) # add dict with params for this pop 
netParams['popParams'].append({'popLabel': 'background1', 'cellModel': 'NetStim', 'rate': 20, 'noise': 0, 'source': 'random'})  # background inputs
netParams['popParams'].append({'popLabel': 'background2', 'cellModel': 'NetStim', 'rate': 20, 'noise': 1, 'source': 'random'})  # background inputs


# Cell parameters list
netParams['cellParams'] = []

## PYR cell properties (HH)
cellRule = {'label': 'PYR_HH', 'conditions': {'cellType': 'PYR', 'cellModel': 'HH'},  'sections': {}}

soma = {'geom': {}, 'topol': {}, 'mechs': {}}  # soma properties
soma['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0, 'pt3d':[]}
soma['geom']['pt3d'].append((0, 0, 0, 18.8))
soma['geom']['pt3d'].append((0, 0, 18.8, 18.8))
soma['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70} 

cellRule['sections'] = {'soma': soma}  # add sections to dict
netParams['cellParams'].append(cellRule)  # add dict to list of cell properties

## PYR cell properties (Izhi)
cellRule = {'label': 'PYR_Izhi', 'conditions': {'cellType': 'PYR', 'cellModel': 'Izhi2007b'},  'sections': {}}

soma = {'geom': {}, 'pointps':{}}  # soma properties
soma['geom'] = {'diam': 10, 'L': 10, 'cm': 31.831}
soma['pointps']['Izhi'] = {'_type':'Izhi2007b', 'C':1, 'k':0.7, 'vr':-60, 'vt':-40, 'vpeak':35, 'a':0.03, 'b':-2, 'c':-50, 'd':100, 'celltype':1}
cellRule['sections'] = {'soma': soma}  # add sections to dict
netParams['cellParams'].append(cellRule)  # add dict to list of cell properties


# Synaptic mechanism parameters
netParams['synMechParams'] = []
netParams['synMechParams'].append({'label': 'syn1', 'mod': 'ExpSyn', 'tau': 30, 'e': 0})
netParams['synMechParams'].append({'label': 'syn2', 'mod': 'ExpSyn', 'tau': 4, 'e': 0})
 

# Connectivity parameters
netParams['connParams'] = []  

netParams['connParams'].append(
    {'preTags': {'cellType': 'PYR'}, 'postTags': {'cellType': 'PYR'},
    'weight': 0.00,                    # weight of each connection
    'delay': '0.2+gauss(13.0,1.4)',     # delay min=0.2, mean=13.0, var = 1.4
    'threshold': 10,                    # threshold
    'convergence': 'uniform(0,5)',       # convergence (num presyn targeting postsyn) is uniformly distributed between 1 and 10
    'synMech': 'syn1'})   


netParams['connParams'].append(
    {'preTags': {'popLabel': 'background1'}, 'postTags': {'cellType': 'PYR','cellModel': 'Izhi2007b'}, # background -> PYR (Izhi2007b)
    'connFunc': 'fullConn',
    'weight': 0.01, 
    'delay': 0,
    'synMech': 'syn2'})  


netParams['connParams'].append(
    {'preTags': {'popLabel': 'background2'}, 'postTags': {'cellType': 'PYR', 'cellModel': 'HH'}, # background -> PYR (HH)
    'connFunc': 'fullConn',
    'weight': 0.005, 
    'synMech': 'syn1',
    'sec': 'soma',
    'loc': 1.0,
    'delay': 0})  



###############################################################################
# SIMULATION PARAMETERS
###############################################################################

simConfig = {}  # dictionary to store simConfig

# Simulation parameters
simConfig['duration'] = 1000 # Duration of the simulation, in ms
simConfig['dt'] = 0.01 # Internal integration timestep to use
simConfig['randseed'] = 1 # Random seed to use
simConfig['createNEURONObj'] = True  # create HOC objects when instantiating network
simConfig['createPyStruct'] = True  # create Python structure (simulator-independent) when instantiating network
simConfig['timing'] = True  # show timing  and save to file
simConfig['verbose'] = True # show detailed messages 


all_cells=range(pop_size*2)
# Recording 
simConfig['recordCells'] = all_cells  # list of cells to record from 
simConfig['recordTraces'] = {'V':{'sec':'soma','loc':0.5,'var':'v'}}
simConfig['recordStim'] = True  # record spikes of cell stims
simConfig['recordStep'] = simConfig['dt'] # Step size in ms to save data (eg. V traces, LFP, etc)

# Saving
simConfig['filename'] = 'HybridSmall'  # Set file output name
simConfig['saveFileStep'] = simConfig['dt'] # step size in ms to save data to disk
simConfig['saveDat'] = True # save traces


# Analysis and plotting 
simConfig['plotRaster'] = True # Whether or not to plot a raster
simConfig['plotCells'] = all_cells # plot recorded traces for this list of cells
simConfig['plotLFPSpectrum'] = False # plot power spectral density
simConfig['maxspikestoplot'] = 3e8 # Maximum number of spikes to plot
simConfig['plotConn'] = False # whether to plot conn matrix
simConfig['plotWeightChanges'] = False # whether to plot weight changes (shown in conn matrix)
simConfig['plot3dArch'] = False # plot 3d architecture

#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

from  PhysicsTools.NanoAODTools.postprocessing.examples.exampleModule import *
#from  PhysicsTools.NanoAODTools.postprocessing.dpanalysis.dpanalysisModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *

#files=["root://xrootd-cms.infn.it///store/user/legianni/Nano01_17Nov17/DoubleEG/RunII2017ReReco17Nov17-94X-Nano01Run2017B-17Nov2017-v1/180307_182136/0000/test_data_94X_NANO_91.root"]

#p=PostProcessor(".",inputFiles(),"Jet_pt>200",modules=[exampleModule()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())
p=PostProcessor(".",inputFiles(),"",modules=[exampleModule()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())
#p=PostProcessor(".",files,"",modules=[exampleModule()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())

p.run()

print "DONE"
os.system("ls -lR")


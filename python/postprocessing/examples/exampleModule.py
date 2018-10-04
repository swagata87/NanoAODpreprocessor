import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class exampleProducer(Module):
    def __init__(self):
#        self.jetSel = jetSelection
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        #self.out.branch("EventMass",  "F");
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        keepIt = True
        eventLeptons = 0
        for lep in muons :
            if lep.mediumId and lep.pfRelIso04_all < 0.4:
                eventLeptons += 1

        if eventLeptons < 2:
            keepIt = False

        return keepIt
        #jets = Collection(event, "Jet")
        #eventSum = ROOT.TLorentzVector()
        #for lep in muons :
         #   eventSum += lep.p4()
        #for lep in electrons :
         #   eventSum += lep.p4()
        #for j in filter(self.jetSel,jets):
         #   eventSum += j.p4()
        #self.out.fillBranch("EventMass",eventSum.M())
        #return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

exampleModule = lambda : exampleProducer() # (jetSelection= lambda j : j.pt > 30) 
 

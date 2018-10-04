#!/bin/bash

samplesAndDatasets[0]="/DoubleMuon/Run2017B-31Mar2018-v1/NANOAOD"
samplesAndDatasets[1]="/DoubleMuon/Run2017C-31Mar2018-v1/NANOAOD"
samplesAndDatasets[2]="/DoubleMuon/Run2017D-31Mar2018-v1/NANOAOD"
samplesAndDatasets[3]="/DoubleMuon/Run2017E-31Mar2018-v1/NANOAOD"
samplesAndDatasets[4]="/DoubleMuon/Run2017F-31Mar2018-v1/NANOAOD"

# ZG sample missing (general)
#WWZ sample missing
#WZZ sample missing
#ZZZ sample missing
#WJe sample missing
#tZq sample missing


#IFS='/' read -r -a array <<EOF
#< "$samplesAndDatasets[1]"
#echo ${array[1]}


for j in {0..4}; do
    echo ${samplesAndDatasets[j]}
    IFS='/' read -r -a array <<< "${samplesAndDatasets[j]}"
# echo ${array[1]}${array[2]:42:8}
# echo crab_cfg.py General.requestName=new${array[2]}_try2 Data.inputDataset=${samplesAndDatasets[j]} Data.outputDatasetTag=${array[2]}
crab submit -c crab_cfg.py General.requestName=Without_lumimask_${array[2]} Data.inputDataset=${samplesAndDatasets[j]} Data.outputDatasetTag=${array[2]}
array=0

done
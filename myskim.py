from cmath import sqrt
from numpy import true_divide
import pandas as pd
import json


df = pd.read_json('test.json')

conditions = [
 "At least four muons",
 "Require good isolation",
 "Good muon kinematics",
 "Track close to primary vertex with small uncertainty",
 "Two positive and two negative muons"
  ]

# Selection of minimal requirementes of 4 muons event
def check4Muons(df, number):
    #At least four muons
    if number == 1: 
        return df[(df['nMuon'] >= 4)]
    #Require good isolation
    if number == 2:
        return df[df["Muon_pfRelIso04_all"].apply(lambda x: all(abs(i) < 0.4 for i in x))]
    #Track close to primary vertex with small uncertainty
    if number == 3:
        df.insert(32, "Muon_ip3d", vectorsum(vectorply(df["Muon_dxy"]), vectorply(df["Muon_dz"])))
        df.insert(33, "Muon_sip3d", vectordivide(df["Muon_ip3d"], vectorsum(vectorply(df["Muon_dxyErr"]), vectorply(df["Muon_dzErr"]))) )
        return df[df["Muon_sip3d"].apply(lambda x: all(abs(i) < 4 for i in x))&df["Muon_dxy"].apply(lambda x: all(abs(i) < 0.5 for i in x))&df["Muon_dz"].apply(lambda x: all(abs(i) < 1.0 for i in x))]
    #Two positive and two negative muons
    if number == 4:
        return df[df["nMuon"]==4&(df["Muon_charge"].apply(lambda x: (vectorSpecial(x, 1) and vectorSpecial(x,-1))))]


def check4Electrons(df, number):
    if number not in range(1,4):
        print("Choose a number between 1 and 4")
        return df
    if number == 1:
        return df[df['nElectron'] >= 4]
    if number == 2:
        return df[df["Electron_pfRelIso03_all"].apply(lambda x: any(abs(i) >= 0.4 for i in x))]
    if number == 3:
        return df[(df["Electron_pt"].apply(lambda x: all(i > 7 for i in x)))&(df["Electron_eta"].apply(lambda x: all(abs(i) < 2.5 for i in x)))]
    if number == 4:
        df.insert(32, "Electron_ip3d", vectorsum(vectorply(df["Electron_dxy"]), vectorply(df["Electron_dz"])))
        df.insert(33, "Electron_sip3d", vectordivide(df["Electron_ip3d"], vectorsum(vectorply(df["Electron_dxyErr"]), vectorply(df["Electron_dzErr"]))) )
        df[(df["Electron_sip3d"].apply(lambda x: all(abs(i) < 4 for i in x)))&(df["Electron_dxy"].apply(lambda x: all(abs(i) < 0.5 for i in x)))&(df["Electron_dz"].apply(lambda x: all(abs(i) < 1.0 for i in x)))]
    if number == 4:
        return df[(df["nElectron"]==4)&(df["Electron_charge"].apply(lambda x: (vectorSpecial(x, 1) and vectorSpecial(x,-1))))]

    return False



# math operations:

#Multiply vectors in list of vectors
def vectorply(vectorList):
    result = []
    for vector in vectorList:
        n = []
        for number in vector:
            n.append(number*number)
        result.append(n)
    return result


# square root and addition of vectors in list of vectors
def vectorsum(vectorlist1, vectorlist2):
    result = []
    for i in range(0,len(vectorlist2)):
        n = []
        for j in range(0, len(vectorlist2[i])):
            a = sqrt(vectorlist2[i][j] + vectorlist1[i][j])
            n.append(a)
        result.append(n)
    return result

# divide vectors in list of vectors
def vectordivide(vectorlist1, vectorlist2):
    result = []
    for i in range(0,len(vectorlist2)):
        n = []
        for j in range(0, len(vectorlist2[i])):
            a =  vectorlist1[i][j] / vectorlist2[i][j]
            n.append(a)
        result.append(n)
    return result

#See if charge meets a condition, and count how many meet the condition
def vectorSpecial(vector, condition):
    c = 0
    for i in vector:
        if i == condition:
            c+=1
    return c == 2




print(check4Electrons(df, 3)["Electron_pt"])

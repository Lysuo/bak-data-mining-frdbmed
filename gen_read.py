import os
import re

with open('effets_notoires.csv') as f:
  contentEffets = f.readlines()
  print contentEffets[0:3]
  contentEffets[0] = contentEffets[0][3:]
  print contentEffets[0:3]


with open('generiques3.csv') as f:
  content = f.readlines()
  content[0] = content[0][3:]

with open('compo.csv') as g:
  contentCompo = g.readlines()
  contentCompo[0] = contentCompo[0][3:]

with open('prix_mod.csv') as g:
  contentPres = g.readlines()
  contentPres[0] = contentPres[0][3:]

with open('labos_mod.csv') as g:
  contentLabos = g.readlines()
  contentLabos[0] = contentLabos[0][3:]

def rewriteEffets(compoGen, compoGenE):
  out31 = open("out_effets.csv", "w")
  out32 = open("out_effets_ind.csv", "w")
  out33 = open("out_MES_sorted.csv", "w")

  outL = []
  outLL = []
  lasti = -1

  for e in contentEffets:
    l = e[0:-2].split(",")
    if len(l) < 3:
      outL[lasti] += l[0]
    elif len(l[0]) < 1 or len(l[1]) < 1:
      if len(l[0]) > 1:
        outL[lasti] += l[0]
    else:
      outL.append(",".join(l))
      lasti += 1

  for i,e in enumerate(outL):
    out31.write(e)
    out31.write("\n")
    l = e.split(",")
    if not l[2] in outLL:
      outLL.append(l[2])

  for i,e in enumerate(outLL):
    if "NULL" in e:
      e = "N/A"
    out32.write('"'+str(i)+'"')
    out32.write(",")
    out32.write(e)
    out32.write("\n")

  CMER = []
  for i,l in enumerate(outL):
    e = l.split(",")
    gen = compoGen[compoGenE.index(e[0])]
    effet = e[2]
    if "NULL" in effet:
      effet = "N/A"

    if not (gen, effet) in CMER:
      CMER.append((gen, effet))

  for i,e in enumerate(CMER):
    out33.write('"'+str(i)+'"')
    out33.write(",")
    out33.write(e[0])
    out33.write(",")
    out33.write(e[1])
    out33.write("\n")

  out31.close()
  out32.close()
  out33.close()

def sortLabos():
  print "sort"

def sort():
  out2 = open("out_sorted2.txt", "w")
  lout = sorted([e[0:-2] for e in content])

  for e in lout:
    out2.write(e+"\n")

  out2.close()
  print "nombre de generiques a la base : " + str(len(lout))

def sortFirst():
  out1 = open("out_gen_first_sorted.txt", "w")

  lloutname = [] 
  lloutocc = []

  for i, l in enumerate(content):
    lsplit = l[0:-2].split(" ")
    strB = ""
    strB += lsplit[0]

    if not (strB in lloutname):
      lloutname.append(strB)
      lloutocc.append(1)
    else:
      j = lloutname.index(strB)
      lloutocc[j] += 1

  llout = []
  for i, e in enumerate(lloutname):
    llout.append((lloutname[i], lloutocc[i]))

  lout = sorted(llout)
  for i, e in enumerate(lout):
    out1.write(e[0] +" : "+ str(e[1]) + "\n")

  out1.close()
  print "nombre de generiques en se basant juste sur le premier mot : " + str(len(llout))


def sortGen(listIn):
  lloutname = [] 
  lloutocc = []
  listGenerique = []
  listGenEnt = []
  listDosage = []
  listFormes = []
  listLabos = []
  listAll = []
  
  listLabos = [
      "BGA", "BGC", "BGR", "FRK", "HPI", "MDC", "MYL", "TYP", "ZTL", "EG", "ARW", "CCD", "TCO", "AGT", "ACT", "AWC", "CRT", "DKT", "EVO", "IVX", "MKG", "RTC", "MYP", "SDC", "SSP", "SUB", "ALM", "ALT", "BAY", "CRT", "GGA", "GNR", "IRX", "QUA", "RPG", "RBX", "TVC", "ZEN", "ZYD", "SDZ", "RTP", "ITA", "GENEVRIER", "HERMES", "BBM", "AGT", "CPF", "REN", "BOIR", "BOIRON", "EVL", "GIFRER", "ISD", "PFZ", "PHR", "WTP", "BMS", "MSD", "SET", "DCI", "GIF", "HXS", "IREX", "LYOC", "TEVA", "VRF", "ZYF", "BCR", "BLF", "KRK", "LAB", "NIALEX", "PFILL", "PFIZER", "LAV", "BLZ", "PROAMP", "BAX", "MACO", "ELB", "BSD", "LIP", "SANOFI", "BIOGA", "MERCK", "ABBOT", "RENAUD","PASTEUR", "GENEVAR", "GALLIER", "HEXAL", "HXL", "GERDA", "EFFIK", "PANPHARMA", "INT", "ARG", "LOBICA", "ISM", "PHR", "AP-HP", "WTR", "STORZ", "EEB", "NOVOLET", "PENFILL", "EGL", "TVS", "BSC", "CIS", "LEUR", "IPR", "MRM", "LFR", "PAN",
      ]

  listToCheck = [
      "SCH",
      "ATU", 
      "INSTIL", "INSTILL", "INSTI",
      "BDB",
      "SAC", 
      "FP", 
      "TRAC", "TRACES", "TRACE",
      "CPRESS", "COMPRESSE",
      "CR", "CREME",
      "PD", "POUDRE",
      "EF", "EFFERVESCENT",
      "VAGINAL", "VAGINALE",
      "CARTOUCHE", 
      "LP", "LIBERATION PROLONGE",
      "CPR+GLE",
      "ENR", "ENROBE",
      "IRRIG",
      "INJ", "INJECTABLE",
      "SUBLINGUAL",
      "MOUSSE",
      "LOTION",
      "BATON",
      "URETRAL",
      "SOL", "SOLUTION",
      "COLLU", "COLLUTOIRE", "COL",
      "COLLYRE", "COLLY",
      "PELLICULE",
      "BANDE",
      "STYLO",
      "TIS", "TISANE", "TISA",
      "PATE",
      "GLE", "BDB", 
      "ORODISP",
      "OPH", "OPHT",
      "DISP",
      "AURICULAIRE",
      "PDE", "POMMADE", "POM",
      "BUV", "BUVABLE",
      "TABLETTE",
      "PDR", "POUDRE", "POUD", "PDRE", "PDR+SOL",
      "VACCIN",
      "INTESTINAL",
      "CPR", "COMPR", "COMPRIME", "COMPRIMES",
      "CAPSULE", "CAPS",
      "GELULE", "GEL",
      "GRANULE", "GRL", "GRLS", "GRANULES", "GRANU", "GRANUL",
      "SUSP", "SUSPENSION",
      "NC",
      "BT",
      "BUCCAL", "BUC",
      "PULV",
      "NAS", "NASAL",
      "NSFP",
      "GBQ",
      "EMPLATRE", "EMPL", "EMP",
      "FL", "FLACON",
      "EFF",
      "ORAL",
      "SER",
      "ENF",
      "AMP", "AMPOULE",
      "PAST", "PASTILLE",
      "BOIR",
      "GTT", "GOUTTE", "GOUTTES",
      "IMPLANT",
      "MONODOSE",
      "SACH", "SACHET", "SACHETS",
      "TUBE", "TB", "TBE", "TUBES", 
      "CREME",
      "PCH", "POC", "POCHE",
      "ASSOC", "ASSOCIATION", "ASOCIATION", "ASSOCIATIONS",
      "MOLLE",
      "AB",
      "FV",
      "CP",
      "APP", "APPLICATION",
      "CUTANEE", "CUT", "CUTANE", "CUTA",
      "UNIDOSE", "UNID",
      "OVULE",
      "SUP", "SUPP", "SUPPOSITOIRE", "SUPPO",
      "SUCER",
      "INHAL", "INHALATION",
      "SHAMPOING",
      "COMP", "COMPOSE",
      "EMULSION",
      "ORALE",
      "INTRAOCUL",
      "HEMOFILT", "HEMOFILTRATION",
      "POUR", "PR", "NFSP",
      "EN",
      "DISP", 
      "AURICULAIRE",
      "SIROP", "SP",
      "BUCCALE",
      "NASALE",
      "TAMPONNE",
      "PERF", "PERFUSION",
      "COMPRESSE",
      "SECABLE",
      "BAUME",
      "MECHE",
      "SIRIOP",
      ]

  countNSFP = 0
  for i, l in enumerate(listIn):
    lsplit = l[0:-2].split(" ")
    strB = ""
    strF = ""
    strFE = True
    strD = ""
    strL = ""
    strPoubelle = ""

    for i,e in enumerate(lsplit):
      if i > 0:
        if lsplit[i] == "313":
          strB += lsplit[i]+" "
        elif (not re.match("\d", lsplit[i], 0) is None) and strD != "" and strF != "" :
    #      strF += lsplit[i]+" "
           strF += ""
           strFE = False
        elif not (re.match("\d", lsplit[i], 0) is None):
          strD += lsplit[i]+" "
          countD = 1
        elif not (re.match("(CEI)|(CEIP)|(MIGROG)|(MIGROGRAMME)|(%)|(MG)|(ML)|(UI)|([A-Z]{1,}/[A-Z]{1,})", lsplit[i], 0) is None):
          strD += lsplit[i]+" "
        elif lsplit[i] in ["NA"]:
          strPoubelle += lsplit[i] + " "
        elif lsplit[i] in listToCheck:
    #      strF += lsplit[i]+" "
          strF += ""
          strFE = False
          if lsplit[i] == "NSFP":
            countNSFP += 1
    #    elif lsplit[i] in ["ET", "EN", "OU", "A"] and strF != "":
        elif lsplit[i] in ["ET", "EN", "OU", "A"] and not strFE:
    #      strF += lsplit[i]+" "
           strF += ""
        elif lsplit[i] in listLabos:
          strL += lsplit[i]+ " "
        else:
          strB += lsplit[i]+" "
      else:
        strB += lsplit[i]+" "

    listGenEnt.append(l[0:-2])
    listDosage.append(strD)
    listFormes.append(strF)
    listGenerique.append(strB)
    listLabos.append(strL)
    listAll.append((strB, strD, strF, strL))

    if not (strB in lloutname):
      lloutname.append(strB)
      lloutocc.append(1)
    else:
      j = lloutname.index(strB)
      lloutocc[j] += 1

  llout = []
  for i, e in enumerate(lloutname):
    llout.append((lloutname[i], lloutocc[i]))

  print countNSFP

  return [listGenEnt, listGenerique, listFormes, listDosage, llout, listAll, listLabos]


def sortRegex(res):
  out4 = open("out_gen_regex_sorted.csv", "w")
  out10 = open("out_gen_formes_dosages.csv", "w")

  #res = sortGen(content)
  lloutE = sorted(res[0])
  llout = res[4]
  listAll = res[5]

  lout = sorted(llout)
  for i, e in enumerate(lout):
    out4.write(e[0] +" : "+ str(e[1]) + "\n")

  lAll = sorted(listAll)
  for i, e in enumerate(lAll):
    out10.write(lloutE[i] + "," + e[0] +","+ str(e[1]) +","+ str(e[2]) +","+ str(e[3]) +"\n")

  out4.close()
  out10.close()
  print "nombre de generiques en s'arretant au premier 'mot-nombre' trouve : " + str(len(llout))

  return lout


def detailsCompo(compoGen, compoGenE):
  out6 = open("out_gen_compo_sorted.csv", "w")
  out20 = open("out_med_sorted.csv", "w")
  out21 = open("out_sub_sorted.csv", "w")
  out22 = open("out_MSR_sorted.csv", "w")

  gen = ""
  sub = ""
  CGen = []
  CMSR = []
  CSub = []
  CCount = []
  CSubs = []
  countGenCompoNotFound = 0

  for i, l in enumerate(contentCompo):

    e = l[0:-2].split(",")
    gen = compoGen[compoGenE.index(e[0])] 
    sub = e[1] 
    if "NULL" in sub:
      sub = "N/A"

    if not (gen, sub) in CMSR:
      CMSR.append((gen, sub))

    if not sub in CSub:
      CSub.append(sub)

    if not gen in CGen:
      CGen.append(gen)
      CSubs.append([sub])

      if "N/A" in sub:
        CCount.append(0)
      else:
        CCount.append(1)

    else:
      if not sub in CSubs[CGen.index(gen)]:
        CSubs[CGen.index(gen)].append(sub)
        CCount[CGen.index(gen)] += 1

      if "N/A" in sub:
        countGenCompoNotFound += 1 
  
  for i,e in enumerate(CGen):
    out6.write('"'+str(i)+'"')
    out6.write(",")
    out6.write('"'+e+'"')
    out6.write(",")
    out6.write(str(CCount[i]))
    out6.write(",")
    for ee in CSubs[i]:
      out6.write('"'+ee+'"')
      out6.write(",")
    out6.write("\n")

    out20.write('"'+str(i)+'"')
    out20.write(",")
    out20.write('"'+e+'"')
    out20.write("\n")

  for i,e in enumerate(CSub):
    out21.write('"'+str(i)+'"')
    out21.write(",")
    out21.write('"'+e+'"')
    out21.write("\n")

  for i,e in enumerate(CMSR):
    out22.write('"'+str(i)+'"')
    out22.write(",")
    out22.write('"'+e[0]+'"')
    out22.write(",")
    out22.write('"'+e[1]+'"')
    out22.write("\n")

  print "compo not found for : " + str(countGenCompoNotFound)
  out6.close()
  out20.close()
  out21.close()
  out22.close()

def detailsFormes(res):
  out7 = open("out_gen_formes_sorted.csv", "w")
  out8 = open("out_gen_formesGen.csv", "w")

  formesGenI = []
  formesSub = []
  for l in contentFormes:
    e = l[0:-2].split(",")
    formesGenI.append(e[0]) 
    if e[1] != e[2]:
      formesSub.append("FORME: "+e[1]+ " - CPLT : "+e[2]) 
    else:
      formesSub.append("FORME: "+e[1]) 

  formesGen = sortGen(formesGenI)[2]

  for e in formesGen:
    out8.write(e+"\n")
  out8.close()

  countNull = 0
  resD = []
  countGenFormesNotFound = 0
  for e in res:
    gen = e[0]
    genDetails = []
    
    boolGen = False
    if gen in formesGen:
      boolGen = True
      indices = [i for i, x in enumerate(formesGen) if x == gen]
      for j in indices:
        if not (formesSub[j] in genDetails):
          if "NULL" in formesSub[j]:
            countNull += 1
          else:
            genDetails.append(formesSub[j]) 

    if boolGen is False:
      countGenFormesNotFound += 1

    resD.append((e[0], e[1], genDetails))

    out7.write('"'+e[0]+'"')
    out7.write(",")
    out7.write(str(e[1]))
    out7.write(",")
    out7.write(str(len(genDetails)))
    out7.write(",")
    for e in genDetails:
      out7.write('"'+e+'"')
      out7.write(",")
    out7.write("\n")
 
  print "formes not found for : " + str(countGenFormesNotFound)
  print "formes etant a NULL : " + str(countNull)
  out7.close()


def detailsFormesDosagePres(listGenEnt, listForme, listDosage, listGen):
  out11 = open("out_gen_FDP_sorted.csv", "w")

  FDPGenE = []
  FDPGen = []
  FDPForme = []
  FDPDosage = []
  FDPPres = []
  FDPPrix = []
  FDPRembours = []
  FDPFacto = []

  countPresBDDNull = 0
  countFormeBDDNull = 0
  countFormeNull = 0
  countDosageBDDNull = 0
  countDosageNull = 0
  countPrixBDDNull = 0
  countRemboursBDDNull = 0

  genEnt = ""
  gen = ""
  forme = ""
  dosage = ""
  pres = ""
  prix = ""
  remboursement = ""
  lasti = -1

  for i,l in enumerate(contentPres): 
    e = l[0:-2].split(",")
    if len(e)>5:

      if e[0] != "":
        genEnt = e[0]
        gen = listGen[listGenEnt.index(e[0])]

        # forme
        if e[1] != "" or e[2] != "":
          if e[1] != e[2] and not (e[1] in e[2]): 
            forme = e[1]+ " " + e[2]
          else:
            forme = e[2]
        else:
          countFormeBDDNull += 1
          if listForme[listGenEnt.index(e[0])] != "":
            forme = listForme[listGenEnt.index(e[0])]
          else:
            countFormeNull += 1
            forme = "N/A"


        # dosage
        if e[3] != "" or e[4] != "":
          dosage = e[3] + " " + e[4]
        else:
          countDosageBDDNull += 1
          if listDosage[listGenEnt.index(e[0])] != "":
            dosage = listDosage[listGenEnt.index(e[0])]
          else:
            countDosageNull += 1
            dosage = "N/A"

        # presentation
        if e[7] != "" or e[8] != "":
          if e[7] != "":
            pres = e[7] + " unites; " + e[8]
          else:
            pres = e[8]
        else:
          countPresBDDNull += 1
          pres = "N/A"

        # prix
        if e[5] != "":
          prix = e[5]
        else:
          countPrixBDDNull += 1
          prix = "N/A"

        # remboursement 
        if e[6] != "":
          remboursement = e[6]
        else:
          countRemboursBDDNull += 1
          remboursement = "N/A"

      if i>0:
        j = 0
        modFormer = False
        #while j < min(len(FDPGen), 50):
        #  if (gen == FDPGen[lasti-j] and e[1] in FDPForme[lasti-j] and dosage == FDPDosage[lasti-j] and pres == FDPPres[lasti-j] and prix == FDPPrix[lasti-j] and remboursement == FDPRembours[lasti-j]):
 #      #     if not e[2] in FDPForme[lasti]:
        #    FDPForme[lasti-j] += " " + e[2]
        #    FDPFacto[lasti-j] += 1
        #    modFormer = True
        #    if forme == "N/A":
        #      countFormeBDDNull -= 1
        #    if dosage == "N/A":
        #      countDosageBDDNull -= 1
        #    if pres == "N/A":
        #      countPresBDDNull -= 1
        #    if prix == "N/A":
        #      countPrixBDDNull -= 1
        #    if remboursement == "N/A":
        #      countRemboursBDDNull -= 1
        #  j += 1
        if not modFormer:
          FDPGenE.append(genEnt)
          FDPFacto.append(1)
          FDPGen.append(gen)
          FDPForme.append(forme)
          FDPDosage.append(dosage)
          FDPPres.append(pres)
          FDPPrix.append(prix)
          FDPRembours.append(remboursement)
          lasti += 1
      else:
        FDPGenE.append(genEnt)
        FDPFacto.append(1)
        FDPGen.append(gen)
        FDPForme.append(forme)
        FDPDosage.append(dosage)
        FDPPres.append(pres)
        FDPPrix.append(prix)
        FDPRembours.append(remboursement)
        lasti += 1

  for i,e in enumerate(FDPForme):
    l = e.split()
    ll = []
    for ee in l:
      if ee not in ll:
        ll.append(ee)
    FDPForme[i] = " ".join(ll)

  for i,l in enumerate(FDPGenE): 
    out11.write('"'+str(FDPFacto[i])+'"')
    out11.write(",")
    out11.write('"'+FDPGenE[i]+'"')
    out11.write(",")
    out11.write('"'+FDPGen[i]+'"')
    out11.write(",")
    out11.write('"'+FDPForme[i]+'"')
    out11.write(",")
    out11.write('"'+FDPDosage[i]+'"')
    out11.write(",")
    out11.write('"'+FDPPres[i]+'"')
    out11.write(",")
    out11.write('"'+FDPPrix[i]+'"')
    out11.write(",")
    out11.write('"'+FDPRembours[i]+'"')
    out11.write("\n")

  print "FDP Forme BDD NULL : " + str(countFormeBDDNull)
  print "FDP Forme NULL : " + str(countFormeNull)
  print "FDP Dosage BDD NULL : " + str(countDosageBDDNull)
  print "FDP Dosage NULL : " + str(countDosageNull)
  print "FDP Pres BDD NULL : " + str(countPresBDDNull)
  print "FDP Prix NULL : " + str(countPrixBDDNull)
  print "FDP Remboursement NULL : " + str(countRemboursBDDNull)
  print len(FDPGen)
  out11.close()

if __name__ == "__main__":
  print "-------| Executing sort function"
  sort()

  #print "-------| Executing sortFirst function"
  #sortFirst()

  print "-------| Executing sortGen function"
  res = sortGen(content)
  listGenEnt = res[0]
  listGen = res[1]
  listForme = res[2]
  listDosage = res[3]

  print "-------| Executing detailsCompo function"
  sortRegex(res)
  detailsCompo(listGen, listGenEnt)

  #print "-------| Executing detailsFormesDosagePres function"
  detailsFormesDosagePres(listGenEnt, listForme, listDosage, listGen)

  #print "-------| Rewriting effets file"
  #rewriteEffets(listGen, listGenEnt)

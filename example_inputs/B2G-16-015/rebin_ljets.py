#!/usr/bin/env python

import ROOT

f = ROOT.TFile("ljets_signals.root")

hists = f.GetListOfKeys()
hists2 = []

for k in hists:
    hist = k.ReadObj()
    if isinstance(hist,ROOT.TH1F):
        hist.Rebin(2)
        hists2.append(hist)

fout = ROOT.TFile("ljets_signals_rebinned.root", "RECREATE")
fout.cd()
for hist in hists2:
    hist.Write()

fout.Close()
f.Close()

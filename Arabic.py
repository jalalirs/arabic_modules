#!/usr/bin/python 
# -*- coding: UTF-8 -*-
from datetime import datetime
import parser
import sys
import re
import os
import glob
import json
import tashaphyne as tph

# from snowballstemmer import stemmer
# ar_stemmer = stemmer("arabic")



######################Globals#########################
unicodeArabic = {
u'\u0624':'HAMZA',u'\ufe84':'HAMZA',u'\ufe85':'HAMZA',u'\ufe8a':'HAMZA',u'\u0625':'HAMZA',u'\ufefa':'HAMZA',u'\ufe83':'HAMZA',
u'\ufe88':'HAMZA',u'\u0623':'HAMZA',u'\ufe89':'HAMZA',u'\ufef9':'HAMZA',u'\ufe87':'HAMZA',u'\ufef7':'HAMZA',u'\ufe8c':'HAMZA',
u'\ufe86':'HAMZA',u'\ufe8b':'HAMZA',u'\ufe80':'HAMZA',u'\u0626':'HAMZA',u'\u0621':'HAMZA',
u'\ufeef':'ALEF',u'\ufb50':'ALEF',u'\ufe8e':'ALEF',u'\u0649':'ALEF',u'\u0627':'ALEF',u'\ufe8d':'ALEF',u'\u0622':'ALEF',u'\u0670':'ALEF',
u'\ufef0':'ALEF',u'\ufe81':'ALEF',u'\u0671':'ALEF',
u'\ufe8f':'BEH',u'\u0628':'BEH',u'\ufe92':'BEH',u'\ufe90':'BEH',u'\ufe91':'BEH',u'\u001a':'BEH',
u'\ufe94':'TEH',u'\ufe95':'TEH',u'\u062a':'TEH',u'\ufe93':'TEH',u'\ufe98':'TEH',u'\u0629':'TEH',u'\ufe97':'TEH',u'\ufe96':'TEH',
u'\ufe9a':'THEH',u'\ufe99':'THEH',u'\ufe9c':'THEH',u'\ufe9b':'THEH',u'\u062b':'THEH',u'\ufe9f':'JEEM',u'\u062c':'JEEM',u'\ufe9e':'JEEM',
u'\ufe9d':'JEEM',u'\ufea0':'JEEM',
u'\ufea4':'HAH',u'\ufea3':'HAH',u'\ufea2':'HAH',u'\u062d':'HAH',u'\ufea1':'HAH',
u'\ufea8':'KHAH',u'\u062e':'KHAH',u'\ufea7':'KHAH',u'\ufea6':'KHAH',
u'\u062f':'DAL',u'\ufeaa':'DAL',u'\ufea9':'DAL',
u'\ufeac':'THAL',u'\ufeab':'THAL',u'\u0630':'THAL',
u'\u0686':'TCHEH',
u'\ufeae':'REH',u'\ufead':'REH',u'\u0631':'REH',
u'\ufeaf':'ZAIN',u'\u0632':'ZAIN',u'\ufeb0':'ZAIN',
u'\ufeb4':'SEEN',u'\ufeb3':'SEEN',u'\u0633':'SEEN',u'\ufeb2':'SEEN',u'\ufeb1':'SEEN',
u'\u0634':'SHEEN',u'\ufeb5':'SHEEN',u'\ufeb8':'SHEEN',u'\ufeb7':'SHEEN',u'\ufeb6':'SHEEN',
u'\u0635':'SAD',u'\ufeba':'SAD',u'\ufebc':'SAD',u'\ufebb':'SAD',u'\ufebf':'DAD',u'\ufebe':'DAD',u'\ufebd':'DAD',u'\ufec0':'DAD',u'\u0636':'DAD',
u'\ufec4':'TAH',u'\ufec3':'TAH',u'\u0637':'TAH',u'\ufec2':'TAH',u'\ufec1':'TAH',
u'\ufec5':'ZAH',u'\u0638':'ZAH',u'\ufec8':'ZAH',u'\ufec7':'ZAH',
u'\ufeca':'AIN',u'\ufec9':'AIN',u'\u0639':'AIN',u'\ufecc':'AIN',u'\ufecb':'AIN',
u'\ufecf':'GHAIN',u'\u063a':'GHAIN',u'\ufece':'GHAIN',u'\ufed0':'GHAIN',
u'\ufed4':'FEH',u'\ufed3':'FEH',u'\ufed2':'FEH',u'\ufed1':'FEH',u'\u0641':'FEH',
u'\u06a4':'VEH',
u'\ufed5':'QAF',u'\ufed8':'QAF',u'\ufed7':'QAF',u'\u0642':'QAF',u'\ufed6':'QAF',
u'\u06af':'GAF',u'\ufb95':'GAF',u'\ufb94':'GAF',
u'\ufeda':'KAF',u'\u0643':'KAF',u'\ufed9':'KAF',u'\ufedc':'KAF',u'\ufedb':'KAF',
u'\u0644':'LAM',u'\ufedf':'LAM',u'\ufef5':'LAM',u'\ufefa':'LAM',u'\ufef9':'LAM',u'\ufede':'LAM',u'\ufef7':'LAM',u'\ufefc':'LAM',
u'\ufedd':'LAM',u'\ufefb':'LAM',u'\ufee0':'LAM',
u'\ufee4':'MEEM',u'\u0645':'MEEM',u'\ufee3':'MEEM',u'\ufee2':'MEEM',u'\ufee1':'MEEM',
u'\ufee5':'NOON',u'\ufee8':'NOON',u'\ufee7':'NOON',u'\u0646':'NOON',u'\ufee6':'NOON',
u'\ufeea':'HEH',u'\ufee9':'HEH',u'\u0647':'HEH',u'\ufeec':'HEH',u'\ufeeb':'HEH',
u'\u0648':'WAW',u'\ufeee':'WAW',u'\ufeed':'WAW',
u'\ufef4':'YEH',u'\u064a':'YEH',u'\ufef3':'YEH',u'\u06cc':'YEH',u'\ufef2':'YEH',u'\ufef1':'YEH',
u'\u0660':'ZERO',u'\u0661':'ONE',u'\u0662':'TWO',u'\u0663':'THREE',u'\u0664':'FOUR',u'\u0665':'FIVE',u'\u0666':'SIX',u'\u0667':'SEVEN',u'\u0668':'EIGHT',
u'\u0669':'NINE',
u' ': 'SPACE'
}
Harakat = {
u'\u064B': 'Fathatan',
u'\u064C': 'Dammatan',
u'\u064D': 'Kasratan',
u'\u064E': 'Fatha',
u'\u064F': 'Damma',
u'\u0650': 'Kasra',
u'\u0651': 'Shadda',
u'\u0652': 'Sukun',
u'\u0653': 'Maddah Above',
u'\u0654': 'Hamza Above',
u'\u0655': 'Hamza Below',
u'\u0656': 'Subscript Alef',
u'\u0657': 'Inverted Damma',
u'\u0658': 'Mark Noon Ghunna',
u'\u0659': 'Zwarakay',
u'\u065A': 'Vowel Sign Small V Above',
u'\u065B': 'Vowel Sign Inverted Small V Above',
u'\u065C': 'Vowel Sign Dot Below',
u'\u065D': 'Reversed Damma',
u'\u065E': 'Fatha With Two Dots',
u'\u065F': 'Wavy Hamza Below'
}
lettersWaits = {
"HAMZA":0.01,
"ALEF":0.07,
"BEH":0.26,
"TEH":0.17,
"THEH":0.25,
"JEEM":0.08,
"HAH":0.02,
"KHAH":0.03,
"DAL":0.14,
"THAL":0.23,
"TCHEH":0.24,
"REH":0.20,
"ZAIN":0.19,
"SEEN":0.16,
"SHEEN":0.09,
"SAD":0.12,
"DAD":0.18,
"TAH":0.10,
"ZAH":0.21,
"AIN":0.02,
"GHAIN":0.03,
"FEH":0.26,
"VEH":0.26,
"QAF":0.04,
"GAF":0.06,
"KAF":0.05,
"LAM":0.15,
"MEEM":0.26,
"NOON":0.22,
"HEH":0.01,
"WAW":0.11,
"YEH":0.13
}
lettersIndex = {"HAMZA":0,"ALEF":1,"BEH":2,"TEH":3,"THEH":4,"JEEM":5,"HAH":6,
"KHAH":7,"DAL":8,"THAL":9,"TCHEH":10,"REH":11,"ZAIN":12,"SEEN":13,"SHEEN":14,"SAD":15,"DAD":16,
"TAH":17,"ZAH":18,"AIN":19,"GHAIN":20,"FEH":21,"VEH":22,"QAF":23,"GAF":24,"KAF":25,"LAM":26,"MEEM":27,
"NOON":28,"HEH":29,"WAW":30,"YEH":31}
######################################################
# ######################Filters#########################
# with open(ARABIC_STOPWORDS) as f:
# 	STOPWORDS = f.read().strip().split("\n")
# 	STOPWORDS = [s.strip().decode("utf-8") for s in STOPWORDS]
def clean_harakat(txt):
	decoded_text = txt
	try:
		decoded_text = txt.decode('utf-8')
	except UnicodeError:
		pass
	harakats_order = Harakat.keys()
	clean = [i for i in decoded_text if i not in harakats_order]
	return "".join(clean)
def clean_text(txt):
	decoded_text = txt
	try:
		decoded_text = txt.decode('utf-8')
	except UnicodeError:
		pass
	clean = tph.strip_tashkeel(decoded_text)
	clean = tph.strip_tatweel(clean)
	clean = tph.normalize_hamza(clean)
	clean = tph.normalize_lamalef(clean)
	return clean

def stem(txt):
	decoded_text = txt
	try:
		decoded_text = txt.decode('utf-8')
	except UnicodeError:
		pass
	try:
		words = decoded_text.split()
		stemmed_txt = ""
		for w in words:
			stemmed_txt += "%s " % (ar_stemmer.stemWord(w))
		return stemmed_txt
	except:
		return txt

def is_arabic(txt):
	decoded_text = txt
	try:
		decoded_text = txt.decode('utf-8')
	except UnicodeError:
		pass
	acceptedLetters = unicodeArabic.keys() + Harakat.keys()
	for c in decoded_text:
		if c not in acceptedLetters:
			return False
	return True

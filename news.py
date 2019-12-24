#!/usr/bin/python 
# -*- coding: UTF-8 -*-
from datetime import datetime
import parser
import sys
import re
import os
import glob
import json
import arabic
from utils import exists, is_file, ls
#sys.setdefaultencoding('utf8')

######################Utils###########################
#--------------------------------------------------#
def stringfile(filePath):
	f = open(filePath, 'r')
	s = f.read()
	f.close()
	return s
#--------------------------------------------------#
def fix_dirpath(dirpath):
	fixedDirPath = dirpath
	if len(dirpath) > 0 and dirpath[-1] != "/":
		fixedDirPath += "/"
	return fixedDirPath
#--------------------------------------------------#
def purify_txt(txt):
	# remove hyperlink: needed when a tweet contains a link that is not of concerned 
	# at this level of the project (code from stackoverflow.com)
	patterns = [r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',r'[^\w#]']
	for p in patterns:
		pattern = re.compile(p,re.UNICODE)
		p_cut = pattern.sub(' ', txt)
	
	return p_cut
######################################################

###################i/o functions####################
def news_decoder(dic):
	title = None
	content = None
	author = None
	url = None
	source = None
	ext_date = None
	return Article(dic["title"],dic["content"],dic["author"],dic["url"],dic["source"],dic["date_extracted"])
#--------------------------------------------------#
def load_news(path,decoder):
	newsOjectsList = None
	newsFiles = []
	if not is_file(path):
		newsFiles = ls(fix_dirpath(path)+"*.json",pattern=True)	
	else:
		newsFiles = [path]

	if len(newsFiles) <= 0:
		print("No files found")
		return None

	newsOjectsList = load_files(newsFiles,decoder)
	if len(newsOjectsList) <= 0:
		return None

	collectedReads = []
	globalId = 0
	for i in newsOjectsList:
		for a in i:
			globalId += 1
			a.set_id(globalId)
			collectedReads.append(a)
	return collectedReads
#--------------------------------------------------#
def load_files(files,decoder):
	fileObjects = []
	for f in files:
		if exists(f) and is_file(f):
			obj = json.loads(stringfile(f), object_hook=decoder)
			fileObjects.append(obj)
	return fileObjects
######################################################

######################Classes#########################
class Article:
	def __init__(self,title=None,content=None,author=None,url=None,source=None,ext_date=None):
		self.title = title
		self.content = content
		self.clean_content = arabic.clean_text(purify_txt(content))
		self.author=author
		self.url = url
		self.source = source
		if ext_date:
			self.ext_date = datetime.strptime(ext_date, '%Y-%m-%d %H:%M:%S')
	
	def set_id(self,id):
		self.id = id

	def __str__(self):
		return self.content

	def __len__(self):
		return len(self.content)


class NewsCorpus:
	def __init__(self,id,name=None, fileName = None):
		self.id = id
		self.name = name
		self.start = 0
		self.articles = []
		if fileName:
			self.populate(fileName)

	def populate(self,path):
		articles = load_news(path,news_decoder)
		if articles:
			self.articles = articles
		else:
			sys.exit()

	def __getitem__(self,index):
		return self.articles[index]

	def __len__(self):
		return len(self.articles)

	def __iter__(self):
		return self

	def __next__(self):
		if self.start >= len(self.articles):
			self.start = 0
			raise StopIteration
		else:
			self.start += 1
			return self.articles[self.start-1]

	def get_articles_by_author(self,author):
		aToReturn = []
		if author:
			for a in self.articles:
				if unicode(author).encode('utf-8') == unicode(a.author).encode('utf-8'):
					aToReturn.append(a)
		return aToReturn

	def get_article_by_id(self,id):
		if id > 0  and id < len(self.articles):
			return self.articles[id]
		return None

	def get_all_articles_contents(self,threshold=-1):
		"""
		threshold: minmum number of characters in the content
		"""
		contents = []
		for a in self.articles:
			if len(a.content) > threshold:
				contents.append(a.content)
		return contents

	def search(self,query):
		hits = []
		for a in self.articles:
			occurs = [m.start() for m in re.finditer(query, a.clean_content)]
			if len(occurs) > 0:
				hits.append((a.id,len(occurs)))
		return hits

####################################################







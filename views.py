import os
import json
from flask import render_template, jsonify, request, send_from_directory, session
from app import app
from parsemodels import Parser, EnrollmentParser
from models import Bot

globalBot = {}
app.secret_key = os.urandom(24)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Kevin'}
    return render_template('index.html', title="test", user = user)

@app.route('/school')
def inst():
	key = os.urandom(64).encode('base-64')

	if session.get('key') is not None:
		if globalBot.get(session['key']) is not None:
			globalBot.remove(session['key'])

	session['key'] = key
	globalBot[session['key']] = Bot()

	PARSER = globalBot[session['key']]
	PARSER.startConnection()
	inst = PARSER.getListOfInsts()
	sortedlist = sorted(inst, key = inst.get)
	return render_template('index.html',
	    title = "Course Search", dictionary = inst, sortedlist = sortedlist)

@app.route('/results', methods = ['GET', 'POST'])
def results():
	PARSER = globalBot[session['key']]
	checkboxValue = request.form.get('checkboxValue')
	resultHtml = PARSER.submit(checkboxValue)
	parsedBot = Parser(resultHtml)
	results = parsedBot.getDictionary()
	return json.dumps(results)

@app.route('/getSeats', methods = ['GET', 'POST'])
def getSeats():
	PARSER = globalBot[session['key']]
	htmlKey = request.form.get('key')
	resultHtml = PARSER.clickClass(htmlKey)
	parsedBot = EnrollmentParser(resultHtml)
	results = parsedBot.getDictionary()
	return json.dumps(results)

@app.route('/term', methods = ['GET', 'POST'])
def term():
	PARSER = globalBot[session['key']]
	results = PARSER.getListOfTerms()
	return jsonify(** results)

@app.route('/dept', methods = ['GET', 'POST'])
def dept():
	PARSER = globalBot[session['key']]
	results = PARSER.getListOfDepts()
	return jsonify(** results)

@app.route('/instChange', methods = ['GET', 'POST'])
def instChange():
	PARSER = globalBot[session['key']]
	newInst = request.form.get('newInst')
	PARSER.setInst(newInst)
	return jsonify({'sample' : 'sample'})

@app.route('/termChange', methods = ['GET', 'POST'])
def termChange():
	PARSER = globalBot[session['key']]
	newTerm = request.form.get('newTerm')
	PARSER.setTerm(newTerm)
	return jsonify({'sample' : 'sample'})

@app.route('/deptChange', methods = ['GET', 'POST'])
def deptChange():
	PARSER = globalBot[session['key']]
	newDept = request.form.get('newDept')
	PARSER.setDept(newDept)
	return jsonify({'sample' : 'sample'})

@app.route('/getTable', methods = ['GET', 'POST'])
def getTable():
	with open ("app/templates/table.html", "r") as htmlfile:
		data = htmlfile.read()
	return data
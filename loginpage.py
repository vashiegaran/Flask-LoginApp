from flask import Flask,render_template,flash,request,redirect, jsonify
import json
app = Flask(__name__)
import pymongo

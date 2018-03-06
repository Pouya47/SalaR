from flask import Flask, flash, redirect, render_template, request#, url_for
from datetime import datetime 
from dbWorker import  *
from salarIntro import *
from scan import nmscan
from httpConnect import httpConnectAsync

app = Flask(__name__)
app.secret_key = 'salar_secret'

@app.route('/')
def Results():
    return render_template('layout.html', 
    time=datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'), scanOpen=5, scanAllPorts=10)
@app.route('/about')
def about():
    about =salar() 
    return render_template('layout.html',about= about)

#REGIN Run
## Sacn ******
@app.route('/scan')
def scan():
    return render_template('portScan.html')

@app.route('/runscan', methods=['POST'])
def runscan():
    nmscan(request.form['target'], request.form['ports'], request.form['args'])
    flash('Port Scan of '+request.form['target']+' Done :)')
    return redirect('portScanResults')
## Sacn ******

## DOS ******
@app.route('/dos')
def dos():
    return render_template('dos.html')

@app.route('/runHttpDos', methods=['POST'])
def runHttpDos():
    sent=httpConnectAsync(request.form['url'], int(request.form['port']), int(request.form['count']))
    flash(str(sent)+' from '+request.form['count'] +' HTTP request sent to '+request.form['url'])
    return redirect('httpDosResults')

@app.route('/runSynFlood', methods=['POST'])
def runSynFlood():
    #TODO: implement synflood  
    nmscan(request.form['target'], request.form['ports'], request.form['args'])
    flash('Port Scan of '+request.form['target']+' Done :)')
    return redirect('portScanResults')
## DOS ******

#ENDREGIN Run

#REGIN Rporter
@app.route('/portScanResults')
def scanResult():
    ent=getScanResult()
    return render_template('portScanResults.html', entries=ent, time=datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))

def getScanResult():
    return connect_db("select * from scanResults order by testID desc").fetchall()

@app.route('/httpDosResults')
def httpDosResults():
    ent=connect_db("select * from httpDosResults order by testID desc").fetchall()
    return render_template('httpDosResults.html',entries =ent, time=datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))


#END REGION reporter
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=90)

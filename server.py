from crypt import methods
from email.mime import audio
from flask import request
from flask import Flask, render_template
app = Flask(__name__)
import csv
import csvWriter
import combiningClips
import trimMedia


@app.route('/')
def index():
  print("is is just refreshing this?")
  return render_template('index.html')


@app.route('/openCombineClips', methods=['POST','GET'])
def openCombine():
  print("is is just refreshing this?")
  return render_template('combineClips.html')


@app.route('/trimClips', methods=['GET', 'POST'])
def openTrimClips():
  return render_template('trimClips.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
    
  csvWriter.csv_writing_module()
  return "Dont know how to stay on the same page the button was clicked yet"


 
@app.route('/go', methods=['POST','GET'])
def goCombine():
  if request.method == "POST":
    stringTakenIn = request.form.get('numClips')
    print ('I a different button got clicked! '+ stringTakenIn)
      
    #csvWriter.csv_writing_module(stringTakenIn)
    return "Bing bong ahoy there"

  elif request.method == "GET":
    # THis is the path we want it to go through
    numClips = request.args.get('numClips')
    clips = int(numClips)
    i = 1
    clipsSaved = []
    while i <= clips:
      getString = 'clip' + str(i-1)
      clipsSaved.append(request.args.get(getString))
      i += 1
    #clip1Location = request.args.get('clip1')
    print (f'Combining {str(numClips)} clips and the locations are:  {str(clipsSaved)}')


    combiningClips.combineFiles(clips,clipsSaved)
    return render_template('success.html')
  else:
    print("Nothing. Youre crap out of luck!")
    return "<h1>Nothing. You're crap out of luck!</h1>"

@app.route('/trimClips', methods=['GET', 'POST'])
def trimClips():
  if request.method == "POST":
    stringTakenIn = request.form.get('numClips')
    print ('I a different button got clicked! '+ stringTakenIn)
      
    #csvWriter.csv_writing_module(stringTakenIn)
    return "Bing bong ahoy there"

  elif request.method == "GET":
    txtFile = request.args.get('txtFile')
    audioFile = request.args.get('audioFile')
    forwardGoPro = request.args.get('forwardGoPro')
    faceGoPro = request.args.get('faceGoPro')
    
    print (f'Trimming clips and the locations are: \n{txtFile}\n{audioFile}\n{forwardGoPro}]\n{faceGoPro}')

    trimClips.run(txtFile,audioFile,forwardGoPro,faceGoPro)
    return render_template('success.html')
  else:
    print("Nothing. Youre crap out of luck!")
    return "<h1>Nothing. You're crap out of luck!</h1>"


@app.route('/why', methods=['POST','GET'])
def my_link_2():
  if request.method == "POST":
    stringTakenIn = request.form.get('numClips')
    print ('I a different button got clicked! '+ stringTakenIn)
      
    #csvWriter.csv_writing_module(stringTakenIn)
    return "Bing bong ahoy there"
  elif request.method == "GET":
    stringTakenIn = request.args.get('numClips')
    print ('A different button got clicked! '+ str(stringTakenIn))
    return 'A different button got clicked! '+ str(stringTakenIn)
  else:
    print("Nothing. Youre shit out of luck!")
    return "<h1>Nothing. You're shit out of luck!</h1>"

  #return render_template('/templates/pass.html', stringParsed=stringTakenIn)
if __name__ == '__main__':
  app.run(debug=True)
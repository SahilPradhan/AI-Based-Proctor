import speech_recognition as sr
import pyaudio
import wave
import time
import threading
from multiprocessing import Process
import os
import re
import nltk
import pymysql

p = pyaudio.PyAudio()  # Create an interface to PortAudio
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100

def read_audio(stream, filename):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 10 # Number of seconds to record at once
    filename = filename
    frames = []  # Initialize array to store frames
    
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    # Stop and close the stream
    stream.stop_stream()
    stream.close()

def convert(i):
    if i >= 0:
        sound = 'record' + str(i) +'.wav'
        r = sr.Recognizer()
        
        with sr.AudioFile(sound) as source:
            r.adjust_for_ambient_noise(source)
            print("Converting Audio To Text and saving to file..... ") 
            audio = r.listen(source)
        try:
            value = r.recognize_google(audio) ##### API call to google for speech recognition
            os.remove(sound)
            if str is bytes: 
                result = u"{}".format(value).encode("utf-8")
            else: 
                result = "{}".format(value)
 
            with open("test.txt","a") as f:
                f.write(result)
                f.write(" ")
                f.close()
                
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("{0}".format(e))
        except KeyboardInterrupt:
            pass



def save_audios(i):
    stream = p.open(format=sample_format,channels=channels,rate=fs,frames_per_buffer=chunk,input=True)
    filename = 'record'+str(i)+'.wav'
    read_audio(stream, filename)



def common_member(a, b):     
    a_set = set(a) 
    b_set = set(b) 
      
    # check length  
    if len(a_set.intersection(b_set)) > 0: 
        return(a_set.intersection(b_set))   
    else: 
        return([]) 

    


def start_audio(time,email,TestID):
    #p = pyaudio.PyAudio()  # Create an interface to PortAudio
    #chunk = 1024  # Record in chunks of 1024 samples
    #sample_format = pyaudio.paInt16  # 16 bits per sample
    #channels = 2
    #fs = 44100

    flag = False


    for i in range(time//10): # Number of total seconds to record/ Number of seconds per recording
        #print([i])
        t1 = threading.Thread(target=save_audios, args=[i]) 
        x = i-1
        t2 = threading.Thread(target=convert, args=[x]) # send one earlier than being recorded
        t1.start() 
        t2.start() 
        t1.join() 
        t2.join() 
        if i==2:
            flag = True
        #if stop():
         #   break
    if flag:
        convert(i)
        p.terminate()


    from nltk.corpus import stopwords 
    from nltk.tokenize import word_tokenize 

    file = open("test.txt") ## Student speech file
    data = file.read()
    file.close()
    stop_words = set(stopwords.words('english'))   
    word_tokens = word_tokenize(data) ######### tokenizing sentence
    filtered_sentence = [w for w in word_tokens if not w in stop_words]  
    filtered_sentence = [] 
  
    for w in word_tokens:   ####### Removing stop words
        if w not in stop_words: 
            filtered_sentence.append(w) 

    ####### creating a final file
    f=open('final.txt','w')
    for ele in filtered_sentence:
        f.write(ele+' ')
    f.close()
    
    ##### checking whether proctor needs to be alerted or not
    file = open("paper.txt") ## Question file
    data = file.read()
    file.close()
    stop_words = set(stopwords.words('english'))   
    word_tokens = word_tokenize(data) ######### tokenizing sentence
    filtered_questions = [w for w in word_tokens if not w in stop_words]  
    filtered_questions = [] 
  
    for w in word_tokens:   ####### Removing stop words
        if w not in stop_words: 
            filtered_questions.append(w) 
        


    comm = common_member(filtered_questions, filtered_sentence)
    connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
    curr = connect.cursor()
    if len(comm) > 0:
        curr.execute("UPDATE ONLINE SET WORDS_SPOKEN=%s WHERE EMAIL=%s AND TEST_ID=%s",(len(comm),email,TestID))
    else:
        curr.execute("UPDATE ONLINE SET WORDS_SPOKEN=%s WHERE EMAIL=%s AND TEST_ID=%s",(0,email,TestID))
    connect.commit()
    connect.close()

    f = open("final.txt", "r+")  
    f.seek(0)  
    f.truncate()
    f.close()

    f1 = open("test.txt", "r+")
    f1.seek(0)
    f1.truncate()
    f1.close()

    dirs = os.listdir()
    for file in dirs:
        if re.findall(".wav",file):
            os.remove(file)
    
            
        
    
    #print('Number of common elements:', len(comm))
    #print(comm)
        
#start_audio('pmm','45')
#Last edited by Sahil Pradhan & Purushottam Madye

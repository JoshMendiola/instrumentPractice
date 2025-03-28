import random, time
note = ["A","A","A#","Bb","B","C","C#","D","D#","Eb","E","F","F#","Gb","G","G#","Ab"]
def menu():
    print("Welcome to Joshuas Music Practice Routine")
    print("1. String Instrument Practice")
    print("2. Wind Instrument Practice")
    direct = input("\nPlease Enter the number of your routine\n")
    if(direct == "1"):
        stringFretboardMemorization()
    elif(direct == "2"):
        windFingeringMemorization()

def stringFretboardMemorization():
    choice = input("\nWhat instrument are you playing?"
                   "\nType the name of the instrument or type \"menu\" for list of instruments\n")
    choice.lower()
    if(choice == "menu"):
        stringInstrumentList()
        stringFretboardMemorization()
    sec = input("\nHow many seconds inbetween?\n")
    sec = float(sec)
    runtime = input("\nHow many times would you like it to run?\n")
    runtime = int(runtime)
    if choice == "bass" or choice == "violin":
        print("\n")
        string = ["E", "A", "D", "G"]
        noteGeneratorString(string,sec,runtime)

def noteGeneratorString(string,sec,runtime):
    if runtime == 0:
        menu()
    print("Your string is " + random.choice(string))
    print("Your note is " + random.choice(note))
    time.sleep(sec)
    runtime -= 1
    noteGeneratorString(string,sec,runtime)

def stringInstrumentList():
    print("1. Bass")
    print("2. Cello")
    print("3. Guitar")
    print("4. Viola")
    print("5. Violin")


def windFingeringMemorization():
    choice = input("\nWhat instrument are you playing?" +
                   "\nType the name of the instrument or type \"menu\" for list of instruments\n")
    choice.lower()
    if(choice == "menu"):
        windInstrumentList()
    sec = input("\nHow many seconds inbetween?\n")
    sec = float(sec)
    runtime = input("\nHow many times would you like it to run?\n")
    runtime = int(runtime)
    if choice == "oboe" or choice == "bassoon" or choice == "trumpet" or choice == "flute" or choice == "trombone":
        print("\n")
        octave = ["low","middle","high"]
        noteGeneratorWind(octave, sec, choice, runtime)

def noteGeneratorWind(octave, sec, choice, runtime):
    if runtime == 0:
        menu()
    windNote = random.choice(note)
    windOctave = random.choice(octave)
    if(choice == "oboe"):
        if windOctave == "low" and (windNote == "A" or windNote == "G" or windNote == "G#" or windNote == "Ab"):
            windOctave = "middle"
        elif windOctave == "high" and (windNote == "G#" or windNote == "Ab" or windNote == "F#" or windNote == "Gb" or windNote == "G"):
            windOctave = "middle"
    elif(choice == "bassoon"):
        if windOctave == "low" and (windNote == "G#" or windNote == "Ab" or windNote == "A"):
            windOctave = "middle"
        elif windOctave == "high" and (windNote == "G#" or windNote == "Ab" or windNote == "G"):
            windOctave = "middle"
    elif choice == "trumpet":
        if windOctave == "low" and (windNote == "G" or windNote == "G#" or windNote == "Ab"):
            windOctave = "middle"
        elif windOctave == "high" and (windNote == "G" or windNote == "G#" or windNote == "Ab"):
            windOctave = "middle"
    elif choice == "flute":
        if windOctave == "low" and (windNote == "A" or windNote == "Bb" or windNote == "A#" or windNote == "B"):
            windOctave = "middle"
        elif windOctave == "high" and (windNote == "A" or windNote == "Bb" or windNote == "A#" or windNote == "B"):
            windOctave = "middle"
    elif choice == "trumpet":
        if windOctave == "low" and (windNote == "E" or windNote == "F" or windNote == "F#" or windNote == "Gb" or windNote == "G" or windNote == "G#" or windNote == "Ab"):
            windOctave = "middle"
        elif windOctave == "high" and (windNote == "G" or windNote == "G#" or windNote == "Ab" or windNote == "F#" or windNote == "Gb"):
            windOctave = "middle"
    print("Your note is : " + windOctave + " " + windNote + "\n")
    time.sleep(sec)
    runtime -= 1
    noteGeneratorWind(octave, sec, choice, runtime)

def windInstrumentList():
    print("1. Bassoon")
    print("2. Flute")
    print("3. Oboe")
    print("4. Trombone")
    print("5. Trumpet")
    windOctave = input("\nWhat instrument are you playing?\n")
menu()





import re
#-----------------------------------------------------------------------------------
g = open('it010801.aiml','w')

COURSECODE = "010801"
PROFESSOR = "Mr. Santhanu P Mohan"
CREDITS = "4"
SYLLABUS = "To introduce the underlying technologies of wireless communication.To explain the benefits and limitations of various techniques for providing multiple users access to scarce radio spectrum resources. To provide a detailed study of the four generations of wireless cellular and mobile telephony, technologies, applications and other issues."
TITLE = "Wireless Communication"
REFERENCES = "1. Juha Korhonen, Introduction to 3G Mobile communications, Artech House, 2001, 2. Miikka Poikselka, Aki Niemi, Hisham Khartabil, Georg Mayer, The IMS: IP Multimedia Concepts and Services, 2nd Edition John Wiley and Sons 2006 3. Jeffrey G. Andrews Fundamentals of WiMAX: Understanding Broadband Wireless Networking, Prentice Hall, 2007 4. Clint Smith, Daniel Collins, Daniel Collins, 3G Wireless Networks, McGraw-Hill Companies, 2006 5. Garg.V.K IS-95 CDMA and cdma 2000, first Indian reprint 2002, Pearson Education 6. Heikki Kaaranen, Siamak Naghian, Lauri Laitinen, Ari Ahtiainen , Valtteri Niemi, UMTS Networks: Architecture, Mobility and Services, John Wiley and Sons; 1 st edition 2001 7. Frank Ohrtman, WiMAX Handbook, McGraw-Hill Professional; 1 edition 2005"
TYPE = "Theory"
DURATION = "Full Semester"
#-----------------------------------------------------------------------------------

def add_underscore(sentence):
    try:
        words = re.compile('\w+').findall(sentence)
        new_sentence = ""
        for index, word in enumerate(words):
            if new_sentence == "":
                new_sentence = word
            else:
                new_sentence = new_sentence + " _ " + word
        return new_sentence
    except:
        return sentence
#--------------------prof---------------------------------------------------------------------------
f = open('reduced/reduced_prof','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close
lines.sort()

header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "\n" + "<aiml version=\"1.0\">"
g.write(header+"\n\n")

lines = list(set(lines))
for line in lines:
    sentence = line[:-1]
    new_sentence = sentence.upper()
    for i in [0,1]:
        if i==0:
            sentence = add_underscore(new_sentence)
        else:
            sentence = new_sentence
        new_line = ""
        s = "<category>"
        new_line = new_line + s + "\n"
        s = "\t" + "<pattern>" + sentence + "</pattern>"
        new_line = new_line + s + "\n"
        s = "\t" + "<template><srai>INSTRUCTOR "+COURSECODE+"</srai></template>"
        new_line = new_line + s + "\n"
        s = "</category>"
        new_line = new_line + s + "\n"
        g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>INSTRUCTOR "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$Professor "+PROFESSOR+" is teaching IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$Professor "+PROFESSOR+" will be teaching IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$Instructor of IT"+COURSECODE+" is Professor "+PROFESSOR+". </li>\n"
s = s + "\t\t\t<li>$IT"+COURSECODE+" is running under instruction of Professor "+PROFESSOR+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#-------------------------prof ends------------------------------------------------------------------

#--------------------------credits--------------------------------------------------------------------
f = open('reduced/reduced_credits','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>CREDITS "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>CREDITS "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$IT "+COURSECODE+" is worth "+CREDITS+" credits. </li>\n"
s = s + "\t\t\t<li>$IT "+COURSECODE+" is of "+CREDITS+" credits. </li>\n"
s = s + "\t\t\t<li>$"+CREDITS+" credits are awarded on successful completion of IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$"+CREDITS+" credits. </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#-----------------------------------credits end--------------------------------------------------------

#-------------------------------------syllabus-----------------------------------------------------------
f = open('reduced/reduced_syllabus','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>SYLLABUS "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>SYLLABUS "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$The syllabus for IT"+COURSECODE+" is "+SYLLABUS+". </li>\n"
s = s + "\t\t\t<li>$"+SYLLABUS+" is taught in IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$Prof. "+PROFESSOR+" will teach "+SYLLABUS+" in IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$"+SYLLABUS+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#-------------------------------------syllabus ends---------------------------------------------------------

#-----------------title-----------------------------------------------------------------------------
f = open('reduced/reduced_title','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>TITLE "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>TITLE "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$The course name of IT"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$The course title of IT"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$Course code IT"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$IT"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$"+TITLE+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#--------------------title ends--------------------------------------------------------------------------

#----------------------------------------references--------------------------------------------------------
f = open('reduced/reduced_references','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>REFERENCES "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>REFERENCES "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$The references are "+REFERENCES+" for IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$The references are "+REFERENCES+" for "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$References according to Professor "+PROFESSOR+" are "+REFERENCES+" for IT"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$"+REFERENCES+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#--------------------------------------references ends--------------------------------------------------------

#----------------------------------------type--------------------------------------------------------
f = open('reduced/reduced_type','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>TYPE "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>TYPE "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$IT"+COURSECODE+" is a "+TYPE+" course. </li>\n"
s = s + "\t\t\t<li>$It's a "+TYPE+" course "+". </li>\n"
s = s + "\t\t\t<li>$"+TYPE+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#--------------------------------------type ends--------------------------------------------------------

#----------------------------------------duration--------------------------------------------------------
f = open('reduced/reduced_duration','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>DURATION "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>DURATION "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$IT"+COURSECODE+" is a "+DURATION+" course. </li>\n"
s = s + "\t\t\t<li>$It's a "+DURATION+" course "+". </li>\n"
s = s + "\t\t\t<li>$IT"+COURSECODE+" is "+DURATION+" long "+". </li>\n"
s = s + "\t\t\t<li>$"+DURATION+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#--------------------------------------duration ends--------------------------------------------------------

g.write("</aiml>")
g.close()

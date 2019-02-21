import sys
import os
import sox


op_system = 'WINDOWS'
#op_system = 'Unix'


# Store the directory where all the audio files are saved
genre_dirs = ['data\\genres\\blues','data\\genres\\classical','data\\genres\\country',
'data\\genres\\disco','data\\genres\\hiphop','data\\genres\\jazz','data\\genres\\metal',
'data\\genres\\pop','data\\genres\\reggae','data\\genres\\rock'
]
os.chdir("../")
retval = os.getcwd()
print ("Current working directory %s" % retval)

for genre_dir in genre_dirs:
	k = retval +"\\"+ genre_dir
	print(k)
	# change directory to genre_dir
	os.chdir(k)

	# echo contents before altering
	print('Contents of ' + genre_dir + ' before conversion: ')
	if(op_system =='Unix'):
		os.system("ls")
	else:
		os.system("dir")


	# loop through each file in current dir
	for file in os.listdir(k):
		# SOX
		#if having the data folder in current directory and want to remove au files ---also uncomment the "delete .au from current dir" section
		#os.system("sox " + str(file) + " " + "+str(file[:-3]) + ".wav")
		
		os.system("sox " + str(file) + " " + "..\\..\\..\\wav model\\data\\genres\\"+str(file[:-9])+"\\"+str(file[:-3]) + ".wav")
		#The -v stands for very high quality.

	"""
	# delete .au from current dir
	if(op_system =='Unix'):
		os.system("rm *.au")
	else:
		os.system("del *.au")
	"""

	# echo contents of current dir
	print('After conversion:')
	if(op_system =='Unix'):
		os.system("ls")
	else:
		os.system("dir")

	print('\n')

print("Conversion complete. Check respective directories.")

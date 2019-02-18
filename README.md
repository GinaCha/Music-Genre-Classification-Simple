### MUSIC GENRE CLASSIFICATION WITH MACHINE LEARNING TECHNIQUES	

#### To use this work on your researches or projects you need:
* Python 3.7
* Python packages:
* run requirement.txt file with pip
* Jupyter Notebook (with IPython kernel)
	
**To install Python:**

_First, check if you already have it installed or not_.
~~~~
python3.7 --version
~~~~
_You should check and update your pip_:
~~~~
pip3 install --upgrade pip
~~~~

Algorithms used:
K-Nearest Neighbor
Random Forest
Support Vector Machine
Neural Network
ExtraTreesClassifier
SVM Poly Kernel

### INFORMATION ABOUT THE REPOSITORY  -  How to use project for testing:

1. Download dataset from: http://opihi.cs.uvic.ca/sound/genres.tar.gz. if data folders not include any au files
A brief of the data set: 

* This dataset was used for the well known paper in genre classification " Musical genre classification of audio signals " by G. Tzanetakis and P. Cook in IEEE Transactions on Audio and Speech Processing 2002.
* The dataset consists of 1000 audio tracks each 30 seconds long. It contains 10 genres, each represented by 100 tracks. The tracks are all 22050Hz Mono 16-bit audio files in .au format.
* To run the model located to Genre_Classification_by _Wav_files  you need to transform the audios to wav format as descibed later on.
* Download size: Approximately 1.3GB
* Download link: [Download the GTZAN genre collection-dataset](http://opihi.cs.uvic.ca/sound/genres.tar.gz)

To run The Machine Learning Solution you should:
* Run config.py file that includes some properties like dataset directory, test directory and some properties for signal processing and feature extraction.
	-	you have to change them to you project path
* Run CreateDataset.py file is used for feature extraction and creating the dataset -a csv file inside data folder.

* Run ModelTrain.py file to creating and training the model. -- optional, prefer the GenreClassification.ipynb file
* RunGenreRecognition.py file to predict the genres of test music files. If you want to change the folder simply change the path in the config.py file  -- optional, prefer the test_genre_by_uploading_au_file.ipynb file
* The CreateThenTrain.py file runs CreateDataset.py and ModelTrain.py sequentially. 
* Run GenreClassification.ipynb file to create and traine the model through 5 Algorithms.
* Run test_genre_by_uploading_au_file to choose a file though a PyQt5.QtWidgets widget, find its genre, and then listen to it through IPython.display

* The functions.ipynb file contails functions for the model training and testing like extraction of features creation of the dataset,locating test files and also some custome functions to present the confusion matrixes
* The MusicSignalAnalysis.ipynb file contains signal analysis about all the genre we study here for the wav file format.










### Genre_Classification_by _Wav_files
Automatic music genre classification using Machine Learning algorithms like- Logistic Regression and K-Nearest Neighbours,Svc


This repository consists of development code that classifies music according to the following genres: 

1. Blues

2. Classical (Western)

3. Country

4. Disco

5. Metal

6. Pop

## Feature of .wav files are generated using:
1. Fast fourier Transform (FFT) (Classification accuracy- **~72%**)
2. Mel Frequency Cepstral Coefficients (MFCC) (Classification accuracy- **~77%**)

## Algorithms used:
1. Logistic Regression
2. K-Nearest Neighbours


## How to use project for testing:
*config1.py file contains paths and necessary lists for the model
1. Run convert-to-wav.py on each subdir of data/genres dir. 
	- if you running on Linux change <op_system = 'WINDOWS'> to <op_system = 'Linux'>

2. Run fft-features.py on each subdir of data/genres dir.

3. Run mfcc-features.py on each subdir of data/genres dir.

4. Run ModelTrain.py according to run instruction provided in the code file.

5. Run tester_audio_genre.py with an audio file to predict the genre 
	-Please not that it is required wav file format
	
6. Run GenreClassification.ipynb file to create and traine the model through 2 Algorithms.

7. Run test_genre_by_uploading_au_file to choose a file though a PyQt5.QtWidgets widget, find its genre, and then listen to it through IPython.display

	
	
Conclusion
We have tried various machine learning algorithms for this project. Our aim is to get maximum accuracy. We have found from our research that we can a get maximum accuracy of 67% by using poly SVM for 10 genre classes. We have also tried to find the best combination of genre classes which will result in maximum accuracy. If we choose 6 genre classes we were able to get an accuracy of 84%. More specificaly we choose [classical, hip-hop, jazz, metal, pop and rock] For some songs we can say that it has feature of multiple genres. So we have also tried to get multiple label outputs based on the probability.	


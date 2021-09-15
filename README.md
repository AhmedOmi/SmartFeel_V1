# Portfolio Projects Machine Learning Specialization
## Project Name : SMARTFEEL
![icon](icon.png)
## Authors :
#### Ahmed Omar Miladi Cohert2 Holberton School Tunisia. < ahmedomarmiledi@gmail.com >

## Project Description :

SMARTFEEL is a mobile application based on machine learning and face detection. It works in the background while users use their smartphones and detects their emotions using the face recognition. The application does a psychological analysis and gives the users all the information about their psychological healthcare.

## Make the project working :
### clone repo:
```bash
git clone https://github.com/AhmedOmi/SmartFeel_V1.git
````
### Download Datasets, Face models and put it in the main directory of project
FaceModel link
```bash
https://drive.google.com/file/d/1SHwAveFhEIresLatir7yi_hCKrig6cIa/view?usp=sharing
```
Datasets link
```bash
https://drive.google.com/file/d/13fkfiEG57hZfRLUi1s4Iob1eSsQAF2bD/view?usp=sharing
```
### working in new environment and install libraries
create virtualenv :
```bash
python3 -m venv venv
```
activate the environment:
```bash
source venv/bin/activate
```
install libraries :
```bash
pip3 install -r requirement.txt
```
### training models and testing
enter to src :
```bash
cd src 
```
start with training this steps can take more times
```bash
python3 emotions.py --mode train
```
this step create a model.h5 it's the machine learning model.
######
After that we testing the projects by doing this commande
```bash
python3 emotions.py --mode display
```
#
#
2021

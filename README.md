# KNN-Recommendation-System
 
This uses centered-cosine similarity and is user-based, so the entire algorithm only predicts by comparing users only. There are no external libraries installed (probably a mistake). 

To set up the script locally:
1. Download the data.zip folder and "Recommendation System.py" and "Search.py" files into the same folder on your computer. The other scripts are experiments, a control algorithm, a data cleaner, and some other random stuff you can check out if you feel like it.

2. The data.zip folder contains all the data files for the algorithm to automatically connect to. If you want to use your own data, you'll probably need to clean it up for the algorithm first, just try to mimick whatever my data looks like in the end. The functions are adjustable for specific column numbers if needed.

3. Open "Recommendation System.py" and go all the way to the bottom, where an example is commented out with an example user. This will show you how to format your user's data and how to run the program to save the data to a location within the unzipped data folder from earlier.

4. 

5. If you want, you can use these functions on your own, identify interesting things about them, try changing the parameters of kNN, or alter the way the algorithm calculates predictions, the comments should be able to help you in deciphering what does what.
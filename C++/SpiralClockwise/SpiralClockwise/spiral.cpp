#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

void userDataPrompt(const int maxAllowedUserNum)
{
	cout << "Enter a positive integer 1-" << maxAllowedUserNum << ":" << endl;
}

bool getUserInput(int &userNumber, const int maxAllowedUserNum)
{
    int maxNumber = 0;

	while(!(cin >> maxNumber)) // handles invalid numbers like letters, symbols, or numbers too large for data type
	{
		cin.clear();
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		userDataPrompt(maxAllowedUserNum);
	}

	if(maxNumber > 0 && maxNumber <= maxAllowedUserNum)
	{
	    userNumber = maxNumber;
	    return true;
	}
    return false;
}

/* Adds padding to printed numbers so they print at a consistent length and thus the output
   file is easy to read and the right lines align (no ragged right) */
string addPadding(int value, short maxLength)
{
    string sValue = to_string(value);
    short valueLength = sValue.length();
    for(int i = 0; i < (maxLength - valueLength); i++)
        sValue += " ";
    
    return sValue;
}

int main() {
    int maxNumber = 0;
	const int maxAllowedUserNum = 1024; //Set to largest square that fits on laptop screen w/o scrolling. Could be increased

    userDataPrompt(maxAllowedUserNum);
    while(!getUserInput(maxNumber, maxAllowedUserNum))
    {
        // wait for valid input
		userDataPrompt(maxAllowedUserNum); // handles valid numbers outside the specified range
    }

    int length = (int)ceil(sqrt(maxNumber));
    
    // initialize array
    int **array;
    array = new int*[length];
    for(int i = 0; i < length; i++)
        array[i] = new int[length];
	
	// zero out array
	for(int row = 0; row < length; row++)
	{
	    for(int col = 0; col < length; col++)
	    {
	        array[col][row] = 0;
	    }
	}

	/* Filling out array will treat the position where 1 is located as (0,0) then
	   a shift will take place for storing each number in the appropriate location
	   in the 2d array. Shift actually takes place from bottom left corner.*/
	int xShift = (int)floor((length - 1) / 2);
	int yShift = (int)floor(length / 2);

	int x = 0, y = 0;
	
	// fill in array
	for(int curNum = 1; curNum < maxNumber; curNum++)
	{
	    array[x + xShift][y + yShift] = curNum;
	    if(abs(x) <= abs(y) && (x >= 0 /* handles (0,0) to (1,0) */ || x != y))
	        x += ((y >= 0) ? 1 : -1);
	    else
	        y += ((x >= 0) ? -1 : 1);
	}
	array[x + xShift][y + yShift] = maxNumber;

	// print array for user
	short maxLength = to_string(maxNumber).length();
	ofstream myfile;
    myfile.open ("output.txt");

	for(int row = length - 1; row >= 0; row--)
	{
	    for(int col = 0; col < length; col++)
	    {
	        int value = array[col][row];
	        myfile << addPadding(value, maxLength) << " ";
	    }
	    myfile << endl;
	}
	myfile.close();

	// free allocated array memory
	for(int i = 0; i < length; i++)
	    delete[] array[i];
	delete[] array;
	
	return 0;
}

#include <iostream>
#include <fstream>
#include <list>
using namespace std;
bool compare (const int& first, const int& second)
{
    return first>second;
}
int main()
{
    ifstream inputFile;
    inputFile.open ("data.txt");

    list<int> numbers;
    list<int>::iterator it;
    int current_number = 0;

    while (inputFile >> current_number)
    {
        numbers.push_back(current_number);
    }
    inputFile.close();


    double procent=(double) numbers.back()/100;
    cout<<"Procent:"<<procent<<endl;
    numbers.pop_back();

    cout << "The numbers are: ";
    for (it=numbers.begin(); it!=numbers.end(); ++it)
        cout << ' ' << *it;
    cout << endl;

    numbers.sort(compare);


    int size=numbers.size();
    size=(int) size/3;
    double sum=0;
    int count =0;

    it=numbers.begin();
    while( it!=numbers.end())
    {
        if(count<size)
        {
            sum+=*it*(1-procent);
        }
        else
        {
            sum+=*it;
        }

        count++;
        ++it;
    }
    cout<<sum;
}

#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

class Bank{
 private:
    string name;
    int numberOfCustomers;
    int numberOfCredits;
 public:
    Bank(){}
    Bank(string name, int numberOfCustomers, int numberOfCredits){
        this->name=name;
        this->numberOfCustomers=numberOfCustomers;
        this->numberOfCredits=numberOfCredits;
        }
    void ToString(){
        cout<<"Name:"<<this->name<<" :"<<this->numberOfCustomers<<" "<<this->numberOfCredits<<endl;
    }
    int getNumberOfCustomers(){
    return this->numberOfCustomers;
    }
    int getnumberOfCredits(){
    return this->numberOfCredits;
    }

};
int numberOfBanks;
Bank **readDataFromFile(Bank **banks){


    string line;
    ifstream input ("data.txt");
    string delimiter=",";
    int i=0;
    if (input.is_open())
      {
        string name="";
        int pre=0;
        int numberOfCustomers, numberOfCredits;

        while ( getline (input,line) ){
        ++numberOfBanks;
        }

        input.close();
        ifstream input ("data.txt");
        typedef Bank* BankPointer;

        BankPointer *banks = new BankPointer[numberOfBanks];
         while ( getline (input,line) )
        {

          name= line.substr(0, line.find(delimiter));
          pre=line.find(delimiter);
          numberOfCustomers = atoi(line.substr(pre+1,line.find(delimiter, pre)-pre-1).c_str());
          pre=line.find(delimiter, pre+1);
          numberOfCredits = atoi(line.substr(pre+1, line.size()-pre-1).c_str());
          banks[i]=new Bank(name, numberOfCustomers, numberOfCredits);

          i++;

        }

        input.close();
        return banks;
      }

      else cout << "Unable to open file";

    };
void bubbleSort(Bank **bankss, int n)
{
    typedef Bank* BankPointer;
    BankPointer *banks=bankss;
    BankPointer *banks1=new BankPointer[2];

   int i, j;
   for (i = 0; i < n-1; i++)
       for (j = 0; j < n-i-1; j++)
           if (banks[j]->getNumberOfCustomers() > banks[j+1]->getNumberOfCustomers()){

                banks1[i] = banks[j];
                banks[j]=banks[j+1];
                banks[j+1]=banks1[i];
           }
}
void merge(Bank **bankss, int leftIndex, int mid, int rightIndex)
{
    typedef Bank* BankPointer;
    BankPointer *banks=bankss;
    int i, j, k;
    int leftLenght = mid - leftIndex + 1;
    int rightLength =  rightIndex - mid;


    BankPointer Left[leftLenght], Right[rightLength];

    for (i = 0; i < leftLenght; i++)
        Left[i] = banks[leftIndex + i];
    for (j = 0; j < rightLength; j++)
        Right[j] = banks[mid + 1+ j];


    i = 0;
    j = 0;
    k = leftIndex;
    while (i < leftLenght && j < rightLength)
    {
        if (Left[i]->getnumberOfCredits() <= Right[j]->getnumberOfCredits())
        {
            banks[k] = Left[i];
            i++;
        }
        else
        {
            banks[k] = Right[j];
            j++;
        }
        k++;
    }

    while (i < leftLenght)
    {
        banks[k] = Left[i];
        i++;
        k++;
    }

    while (j < rightLength)
    {
        banks[k] = Right[j];
        j++;
        k++;
    }
}

void mergeSort(Bank **bankss, int leftIndex, int rightIndex)
{
    typedef Bank* BankPointer;
    BankPointer *banks=bankss;
    if (leftIndex < rightIndex)
    {
        int mid = leftIndex+(rightIndex-leftIndex)/2;

        mergeSort(banks, leftIndex, mid);
        mergeSort(banks, mid+1, rightIndex);

        merge(banks, leftIndex, mid, rightIndex);
    }
}
void printList(Bank **banks, int n){
    for (int i=0;i<n;i++){
        banks[i]->ToString();
    }
    cout<<endl;
}


int main()
{
    typedef Bank* BankPointer;
    BankPointer *banks;
    banks=readDataFromFile(banks);
    bubbleSort(banks, numberOfBanks);
    cout<<"BubbleSort:"<<endl;
    printList(banks, numberOfBanks);
    mergeSort(banks, 0, numberOfBanks - 1);
    cout<<"MergeSort:"<<endl;
    printList(banks, numberOfBanks);
    return 0;
}

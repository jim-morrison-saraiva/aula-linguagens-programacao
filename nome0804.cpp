#include <iostream>
#include <string>
using namespace std;
int main ()
{
    string nome, snome; 
    char tamanho;
     cout << "Digite seu nome: " << endl;
    cin >> nome; 
     cout << "Digite seu sobrenome: " << endl;
    cin >> snome; 
    tamanho = nome[nome.length() -1];
     cout << snome << ","<< nome[0]<< tamanho << endl;
    return 0;

    }
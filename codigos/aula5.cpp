#include <iostream>
using namespace std;
struct lista{
    int v[10];
    int fim;
};

void insert(lista & l, int pos, int novoElemento){
    if(pos != l.fim){for(int i=l.fim;i>pos;i--){l.v[i]=l.v[i-1];}}
    l.v[pos]=novoElemento;
    l.fim++;
}

void imprime(lista l){for(int i=0;i<l.fim;i++){cout<<l.v[i]<<" ";}cout<<endl;}

void remove(lista & l, int pos){
    if(pos!=l.fim-1){for(int i=pos;i<l.fim-1;i++){l.v[i]=l.v[i+1];}}
    l.fim--;
}

int element(lista l, int pos){return l.v[pos];}

int pos(lista l, int elemento){
    for(int i=0;i<l.fim;i++){if(l.v[i] == elemento){return i;}}
    return -1;
}

int main(){

}
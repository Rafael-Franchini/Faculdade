#include <iostream>
using namespace std;

struct no{
  int valor;
  no * proximo;
};

no * inicio= NULL;

no * fim = NULL;

void enqueue(int novoValor){
  no * novoNo =(no*)malloc(sizeof(no));
  novoNo -> valor = novoValor;
  novoNo -> proximo = NULL;
  if(inicio==NULL){
    inicio = novoNo;
    fim = novoNo;
  }
  else{
    fim -> proximo = novoNo;
    fim = novoNo;
  }
}

int first(){
  return inicio->valor;
}

int main(){
  cout<<"FUNFO";
}


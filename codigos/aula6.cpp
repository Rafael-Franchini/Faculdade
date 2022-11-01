
#include <iostream>
using namespace std;

//estrutura
struct no{
  int valor;
  no * proximo;
};

//retorna primeiro valor
int first(){
  return inicio -> valor;
}
//retorna ultimo valor
int back(){
  return fim -> valor;
}
//ponteiros inicio e fim
no * inicio= NULL;
no * fim = NULL;

//colocar/enfileirar 
void enqueue(int novoValor){
  no * novoNo =(no*)malloc(sizeof(no));
  novoNo -> valor = novoValor;
  novoNo -> proximo = NULL;
  //se inicio estiver vazio criar valor apenas...
  if(inicio==NULL){
    inicio = novoNo;
    fim = novoNo;
  }
  //senao fazer final do primeiro elemento apontar o proximo ...
  else{
    fim -> proximo = novoNo;
    fim = novoNo;
  }
}

//retirar valor
void dequeue(){
  no * removido = inicio;
  //se o inicio for igual ao fim ele zera tudo... 
  if(inicio==fim){
    inicio = NULL;
    fim = NULL;
  }
  //senao colocar o proximo valor como inicio...
  else{
    inicio=inicio->proximo;
  }
  free(removido);
}

int main(){
  cout<<"FUNFO";
}


//bibliotecas...
#include <iostream>
#include<cstdlib>
using namespace std;
//estrutura
struct no{
  int valor;
  no * proximo;
};
//ponteiro para marcar o inicio...
no * inicio = NULL;
//
int pos(){

}
//
void element(){

}
//adiciona valor na posição
void insert(int pos, int novoValor){
    no * novoNo = (no*)malloc(sizeof(no));
    novoNo -> valor = novoValor;
    //inserção na posição 0
    if(pos == 0){
        //se a lista estiver vazia...
        if(inicio == NULL){
            inicio = novoNo;
            novoNo -> proximo = NULL;
        }
        //lista nao esta vazia
        else{
            novoNo -> proximo=inicio;
            inicio = novoNo;
            }
    }
    // posição maior que 0
    else{
        //localizar o elemento anterior da posição
        no * aux = inicio;
        for(int i = 0 ; i < pos ; i++){
            aux = aux -> proximo;
        }
        //final da lista
        if(aux -> proximo == NULL){
            aux -> proximo = novoNo;
            novoNo -> proximo = NULL;
        }
        //meio da lista
        else{
            novoNo -> proximo = aux -> proximo;
            aux -> proximo = novoNo;
        }
    }
}
//remove elemento da posição....
void remove(){

}
//imprime lista...
void imprimelista(){
    for(no * aux = inicio ; aux != NULL ; aux = aux -> proximo){
    cout<<aux->valor<<" ";
  }
  cout<<endl<<endl;
}
int main(){
    cout<<"FUNFO"<<endl;
    cout<<endl;
}
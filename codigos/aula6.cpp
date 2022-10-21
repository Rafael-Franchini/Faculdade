#include <iostream>

using namespace std;

struct aluno{
    int ra;
    float nota;
};

int main(){
  aluno a;//variavel do tipo aluno
  aluno*pa; //ponteiro para struct
  pa= &a;//ponteiro "pa" aponta a variavel "a"
  pa->ra=123;//o campo "ra" da struct apontada por "pa" sera alterado
  pa->nota=9.5;//o campo "nota" da struct apontada por "pa" sera alterada
  
  return 0;  
}
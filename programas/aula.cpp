/*f8 para rodar*/
#include <iostream>
using namespace std;

int soma(int a,int b){
    return a+b;   
}
int media(int v[],int tamanho){
    int soma= 0;
    for (int i=0;i<tamanho;i++){
        soma+=v[i];
    }
    return soma/tamanho;
}

int main(){
    int a[]={1,2,3};
    int b[]={2,3,4,6,8,0};
    
    cout<<"Media de a= "<<media(a,3)<<endl;
    cout<<"Media de a= "<<media(b,6)<<endl;
    
    
    return 0;
}

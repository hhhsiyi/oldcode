#include<iostream>
#include<Windows.h>
#include<cmath>
using namespace std;


//encrypt
void encrypt1(char *str,int pk,int n,int *a1){
    int i=0;
    while(1){
            if(str[i]>='a'&&str[i]<='z'){
                str[i]=str[i]-97;//97
            }
            if(str[i]>='A'&&str[i]<='Z'){
                str[i]=str[i]-65;//65
            }
            if(str[i]=='#'){
                break;
            }
            int b=pow((int)str[i],(float)pk);
            a1[i]=b%n;
            i++;
        }
}
void encrypt(int MM,int sk,int n,int *a1)
{
    int i;
    cout<<sk<<endl;
    int TT=(int)pow(MM,sk)%n;
}

//decipher
void decipher(char* str,int sk,int n,int* a2,int& length){
            for(int i=0;i<length;i++){
            int b=pow(a2[i],(float)sk);
            str[i]=char((b%n)+97);
    }
        str[length]='#';
}


int main(){
    int p,q,sk,pk,r,i,length;
    int MM,TT;
    char str1[100],str2[100];
    int a1[100]={0},a2[100]={0};
    cout<<"please input two different prime:"<<endl;
    cin>>p>>q;
    int n=p*q;
    int M=(p-1)*(q-1);
    cout<<"please input (e)sk,sk<"<<M<<endl;
    cin>>sk;
    cout<<"please input (d)pk,pk=sk^(-1)mod"<<M<<endl;
    cin>>pk;
    cout<<n<<" "<<M<<endl;
    cout<<"choose encrypt(input 1) or decipher(input 2)"<<endl;
    cin>>r;
    switch(r){
        case 1:
            cout<<"Ã÷ÎÄ"<<endl;
            cin>>MM;
            encrypt(MM,sk,n,a1);
            cout<<"the ciphertext is:"<<endl;
//            for(int j=0;j<i;j++){
//                cout<<a1[j]<<"\t";
//            }
            cout<<MM<<endl;
            break;
        case 2:
            cout<<"please input the length of your ciphertext!"<<endl;
            cin>>length;
            cout<<"ÃÜÎÄ"<<endl;
            for(i=0;i<length;i++){
                cin>>a2[i];
            }
            decipher(str2,sk,n,a2,length);
            cout<<"the plaintext is:"<<endl;
            for(i=0;i<=length;i++){
                if(str2[i]=='#')
                    break;
                cout<<str2[i]<<"\t";
            }
            break;
        default:
            break;
    }
    return 0;
}

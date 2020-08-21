#include <iostream>

using namespace std;

int main()
{
    cout << "Hello World!" << endl;
    int t=10000;
    int a[4]={0};
    a[0]=1;
    a[1]=1;
    a[2]=1;
    int n;
    cin>>n;
    for(int i =3;i<n;i++)
    {
        a[3]=(a[0]+a[2]+a[1])%t;
        a[0]=a[1];
        a[1]=a[2];
        a[2]=a[3];
    }
    cout<<a[3]<<endl;
    return 0;
}

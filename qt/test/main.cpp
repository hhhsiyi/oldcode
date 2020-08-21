#include <iostream>
#include <cstring>
using namespace std;
enum season
{
    spr=0,
    sum,
    aut,
    win,
    win2,
};
struct student{
    int id;
    char name[64];
};
struct typeA{
    int &a;
};
struct typeB{
    int *a;
};

void printS(struct student s)//结构体整个值拷贝
{
    cout<<s.id<<" "<<s.name<<endl;
}
void printS1(struct student *sp)
{
    cout<<sp->id<<" "<<sp->name<<endl;
}
void printS2(struct student &s)
{
    cout<<s.id<<" "<<s.name<<endl;
}

void test6()
{
    enum season s =aut;
}

void test5()
{
    const int a = 10;
//    int *p = &a;
//    *p = 70;
    cout <<"a=  "<<a<<endl;
    cout<<"*p"<<endl;
}
void change_value(int *p)
{
    *p = 30;
}
void swap(int *a,int *b)
{
    int temp;
    temp =*a;
    *a = *b;
    *b = temp;
}
void myswap(int &a,int &b)
{
    int temp = a;
    a=  b;
    b=temp;

}

int main()
{
    int a=  20;
    int b =  30;
    int *p = &a;
    *p=30;
    p=&b;
    int &re = a;
    re = 50;
     re =  b;
    re = 50;

    cout<<a<<endl;
    cout<<b<<endl;
    change_value(&a);
    cout<<a<<endl;

    //test6();
    int t=10;
    int tt = 100;
    myswap(t,tt);
    cout<<t<<"\n"<<tt<<endl;
    student s1 = {10,"hewen"};

    printS(s1);
    printS1(&s1);
    printS2(s1);
    cout<<sizeof(struct typeA)<<" "<<sizeof(struct typeB)<<endl;
return 0;
}

//class B
//{
//private:
//    int width;
//public:
//    B()
//    {
//        cout<<"调用构造函数"<<endl;
//    }
//    ~B()
//    {
//        cout<<"调用析构函数"<<endl;
//    }
//};

//int main(int argc, char *argv[])
//{
//    B* bb = new B[4];
//    delete []bb;

//    cout << "Hello World!" << endl;
//    return 0;
//}

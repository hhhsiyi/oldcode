#include<iostream>

using namespace std;

void test()
{
    while (1)
    {
        cout << "输入桩长：\n";
        double chang, ci, liang;
        cin >> chang;
        cout << "锤击次数是:" << chang * 40 <<
            "    实际填料量是：" << chang * 0.1 << endl;
        system("pause");
        system("cls");
    }

}
int main()
{
    test();
    return 0;
}

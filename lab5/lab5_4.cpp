#include <iostream>

using namespace std;

double hesapla(int n) {

    if (n == 0) {
        return 0.0;
    }
    double sign = (n % 2 != 0) ? 1.0 : -1.0;

    double now = sign / n;

    return hesapla(n - 1) + now;
}

int main() {
    int n;

    cout << "enter valuen: ";
    cin >> n;


    double result = hesapla(n);

    cout << "result: " << result << endl;

    return 0;
}


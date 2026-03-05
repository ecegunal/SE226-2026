#include <iostream>

using namespace std;

int main() {
    int n;
    int m = 0;

    cout << "please enter a positive integer greater than 1: ";
    cin >> n;
    cout << n;

    while (n != 1) {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = (n * 3) + 1;
        }

        cout << " -> " << n;
        m++;
    }

    cout << endl;
    cout << "total steps: " << m << endl;

    return 0;
} 

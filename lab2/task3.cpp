#include <iostream>

using namespace std;

int main() {
    int n = 0;

    while (n < 3 || n > 9) {
        cout << "please enter a number between 3 and 9: ";
        cin >> n;
        if (n < 3 || n > 9) {
            cout << "invalid input." << endl;
        }
    }

    for (int i = 1; i <= 2 * n - 1; i++) {
        int a = n - i;

        if (a < 0) {
            a = -a;
        }

        int k = n - a;


        for (int j = 0; j < k; j++) {
            cout <<"*";
        }

        cout << endl;
    }

    return 0;
}

#include <iostream>
using namespace std;

int main() {
    int n = 0;

    while (n < 10 || n > 100) {
        cout << "Please enter a number between 10 and 100: ";
        cin >> n;
        if (n < 10 || n > 100) {
            cout << "Invalid input. Please enter a number between 10 and 100: " << endl;
        }
    }

    int fiz = 0;
    int buz = 0;
    int fizbuz = 0;

    for (int i = 1; i <= n; i++) {
        if (i % 7 == 0) {
            cout << "(" << i << " is skipped )" << endl;
            continue;
        }

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizbuz = fizbuz + 1;
        }
        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fiz = fiz + 1;
        }
        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buz = buz + 1;
        }
        else {
            cout << i << endl;
        }
    }

    cout << "--- Summary ---" << endl;
    cout << "Fizz count : " << fiz << endl;
    cout << "Buzz count : " << buz << endl;
    cout << "FizzBuzz count: " << fizbuz << endl;

    return 0;
}

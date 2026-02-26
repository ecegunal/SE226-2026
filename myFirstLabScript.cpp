#include <iostream>
#include <cmath>

using namespace std;

class myFirstLabScript {
public:

    static void task1() {
        string name;
        string studentID;

        cout << "What is your name?" << endl;
        cin >> name;

        cout << "Hello " << name << "." << endl;

        cout << "What is your Student id?" << endl;
        cin >> studentID;

        cout << "Your id is " << studentID << "." << endl;
    }

    static void task2() {
        int totalSeconds;

        cout << "Enter total seconds: ";
        cin >> totalSeconds;

        int hours = totalSeconds / 3600;
        int minutes = (totalSeconds % 3600) / 60;
        int seconds = totalSeconds % 60;

        cout << totalSeconds << " seconds is "
             << hours << " hours, "
             << minutes << " minutes, and "
             << seconds << " seconds." << endl;
    }

    static void task3() {
        double x1, y1, x2, y2;

        cout << "Enter x1: ";
        cin >> x1;

        cout << "Enter y1: ";
        cin >> y1;

        cout << "Enter x2: ";
        cin >> x2;

        cout << "Enter y2: ";
        cin >> y2;

        double distance = sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1));

        cout << "Distance = " << distance << endl;
    }

    static void task4() {
        cout << "*******\n ***** \n  ***  \n   *" << endl;
    }
};

int main() {

    myFirstLabScript::task1();
    cout << endl;

    myFirstLabScript::task2();
    cout << endl;

    myFirstLabScript::task3();
    cout << endl;

    myFirstLabScript::task4();

    return 0;
}

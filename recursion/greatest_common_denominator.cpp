#include <iostream>
// a > b
int GDC(int a, int b) {
    int remainder = a % b;
    std::cout << "remainder: " << remainder << std::endl;
    if (remainder == 0)
        return b;
    else 
        return GDC(b, remainder);
}

int main(int argc, char** argv) {
    int a = 255;
    int b = 35;
    std::cout << "Greatest Common Denominator of " << a << " " << b << " is " << GDC(a, b) << std::endl;
    return 0;
}
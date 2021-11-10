#include <iostream>

int factorial(int n) {
    if (n == 1) 
        return 1;
    else 
        return n * factorial(n-1);
}

int main(int argc, char** argv) {
    int n = 10;
    std::cout << n << "! = " << factorial(n) << std::endl;
    return 0;
}
#include <vector>
#include <iostream>

void fibonacci(int a, int b, std::vector<int> &answer) {
    if (answer.size() == 0) {
        answer.push_back(a);   
        answer.push_back(b);
    }
    answer.push_back(a+b);
    if (answer.size() == 20)
        return;
    else 
        fibonacci(b, a+b, answer);
}

int main(int argc, char** argv) {
    std::vector<int> answer;
    fibonacci(0, 1, answer);
    for (size_t i = 0; i < answer.size(); ++i) {
        std::cout << answer[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
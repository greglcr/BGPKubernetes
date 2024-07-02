#include <iostream>
#include <fstream>
#include "json.hpp"

using json = nlohmann::json;

int main() {    

    std::ifstream f("example.json");
    json data = json::parse(f);
    int a = data["variable1"];
    std::cout << a << std::endl;

}
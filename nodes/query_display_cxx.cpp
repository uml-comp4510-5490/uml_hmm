#include <random>

#include "display_hist.hpp"

using std::cout;
using std::cerr;
using std::endl;
using std::vector;

int main(int argc, char** argv)
{
    std::random_device rd;  //Will be used to obtain a seed for the random number engine
    std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
    std::uniform_real_distribution<> dis(0.0, 1.0);
    vector<float> vec;
    for(size_t n = 0; n < 10; n++)
    {
        vec.push_back(static_cast<float>(dis(gen)) );
    }

    //hmm::display_basic(vec);
    hmm::display_basic<vector<float> >(vec);


    return EXIT_SUCCESS;
}

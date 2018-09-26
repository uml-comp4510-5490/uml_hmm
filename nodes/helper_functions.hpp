#include <cmath>
#include <iostream>

namespace hmm
{
    // definition of normal curve
    float gauss(float x, float mu, float sigma);

    // this experimentally approximates door sensor performance
    float door(float mu, float x);

    // gives probability that you are in front of a door
    // doors are centered at 11m, 18.5m, and 41m
    float p_door(float x);
    
    // gives probability that you are in front of a wall
    float p_wall(float x);

    // displays everything nicely
    void display_basic(float hist[], int size);
}

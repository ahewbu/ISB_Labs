#include <iostream>
#include <random>
#include <ctime>

#define MAX_BIT 128

using namespace std;

/**
 * Generates a sequence of 128 random binary numbers.
 *
 * @param [in] rand_num generates a random number in the range from 0 to 32766.
 * @param [in] binary_num forms a binary sequence from the remainder of even and odd values
 * @return The randomly generated binary string.
 */
int generator()
{
    srand(time(0));
    for (int i = 0; i < MAX_BIT; ++i)
    {
        unsigned long long rand_num = rand() % 32767;
        bool binary_num = rand_num % 2;
        cout << binary_num;
    }
    return 0;
}

int main()
{
    cout << generator() << endl;
}
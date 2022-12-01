#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <numeric>

int main()
{
	std::ifstream file("input.txt");

	constexpr int c_bestElvesAmount = 3;
	int heap[c_bestElvesAmount] = {0};

	using SortingPred = std::greater<int>;

	int sum = 0;
	while (!file.eof())
	{
		std::string input;
		std::getline( file, input );

		if (input.empty())
		{
			if (sum > heap[c_bestElvesAmount - 1])
			{
				std::pop_heap(std::begin(heap), std::end(heap), SortingPred());
				heap[c_bestElvesAmount - 1] = sum;
				std::push_heap(std::begin(heap), std::end(heap), SortingPred());
			}

			sum = 0;
			continue;
		}
		else
		{
			sum += std::stoi( input );
		}	
	}

	std::cout << std::accumulate(std::begin(heap), std::end(heap), 0);
}

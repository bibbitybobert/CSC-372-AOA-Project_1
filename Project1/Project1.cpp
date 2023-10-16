#include "Header.h"

using namespace std;

int main(int argc, char** argv) {
	ifstream in_file;
	stations layout;

	switch (argc) {
	case 0: //HOW????
		cout << "How did you run this with no command line arguments?????\n";
		exit(0);
	case 1: //NO files given
		cout << "Please run with a file for data input\n";
		exit(0);
	case 2: //only input file given
		break;
	default:
		cout << "Too many command line arguments\n Please input only one input file name\n";
		exit(0);
	}

	string in_file_name(argv[1]);
	in_file = open_file(in_file_name);
	layout.create(in_file);
	in_file.close();

	layout.fastestTime = findFastest(layout.stations - 1, 0, layout);

	outputData(layout);

	return(0);
}

ifstream open_file(string fin_name) {
	ifstream fin;
	fin.open(fin_name);
	if (!fin.is_open()) {
		cout << "Error opening file.\nShutting program down\n";
		exit(1);
	}
	return fin;
}

int findFastest(int stage, int route, stations& map) {
	if (stage == 0)
		return map.stationWeights[route][0];

	for (int i = 0; i < map.lines; i++) {
		int sum_total = 0;

		if (map.lookup[stage - 1][1] != -1)
			sum_total += map.lookup[stage - 1][0];
		else
			sum_total = findFastest(stage - 1, i, map);


		//stay on same line
		if (i != route) {
			sum_total += map.transferWeight[stage - 1][i][route];
		}

		sum_total = sum_total + map.stationWeights[route][stage]
			+ map.transferWeight[stage][route - 1][route - 1];

		if (sum_total < map.lookup[stage][0]) {
			map.lookup[stage][0] = sum_total;
			map.lookup[stage][1] = i;
		}
	}
	return map.lookup[stage][0];
}

void outputData(stations& data) {
	cout << "Total time: " << data.fastestTime << endl;
	cout << "Line Progress: \n";
	for (int i = 0; i < data.lookup.size(); i++) {
		cout << data.lookup[i][0] << "(" << data.lookup[i][1] << ")\n";
	}
	cout << data.fastestTime << '(' << data.lookup[data.stations - 1][1] << ')\n';
}
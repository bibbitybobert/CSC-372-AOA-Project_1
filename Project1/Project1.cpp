#include "Header.h"

using namespace std;

int main(int argc, char** argv) {
	ifstream in_file;
	stations layout;
	bool testing = false;

	switch (argc) {
	case 0: //HOW????
		cout << "How did you run this with no command line arguments?????\n";
		exit(0);
	case 1: //NO files given
		cout << "Please run with a file for data input\n";
		exit(0);
	case 2: //only input file given
		break;
	case 3:
		if (argv[2][0] == '-' && argv[2][1] == 't') {
			testing = true;
		}
		break;
	default:
		cout << "Too many command line arguments\n Please input only one input file name\n";
		exit(0);
	}

	string in_file_name(argv[1]);
	in_file = open_file(in_file_name);
	layout.create(in_file);
	in_file.close();

	for (int i = 0; i < layout.lines; i++) {
		int temp = findFastest(layout.stations, i, layout);
		if (temp < layout.fastestTime) {
			layout.fastestTime = temp;
			layout.best_end = i;
		}
	}

	if (!testing) {
		outputData(layout);
	}

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
	if (stage == 0) {
		//GRADING:UPDATE
		map.lookup[stage][route][0] = map.stationWeights[route][0];
		map.lookup[stage][route][1] = -1;
		return map.stationWeights[route][0];
	}
	int return_data = INT_MAX;
	int best_line = -1;
	for (int i = 0; i < map.lines; i++) {
		int sum_total = 0;


		if (map.lookup[stage - 1][i][0] == INT_MAX) {
			sum_total = findFastest(stage - 1, i, map);
		}
		else {
			//GRADING:REUSE
			sum_total = map.lookup[stage-1][i][0]; 
		}
				

		//change lines
		if (i != route) {
			sum_total += map.transferWeight[stage - 1][i][route];
		}

		if (stage != map.stations) {
			sum_total += map.stationWeights[route][stage]
				+ map.transferWeight[stage - 1][route][route];
		}
		else {
			sum_total += map.transferWeight[stage -1][route][route];
		}

		if (sum_total < return_data) {
			return_data = sum_total;
			best_line = i;
		}

	}
	if (return_data < map.lookup[stage][route][0]) {
		//GRADING:UPDATE
		map.lookup[stage][route][0] = return_data;
		map.lookup[stage][route][1] = best_line;
	}
	return return_data;
}

void outputData(stations& data) {
	cout << "Total time: " << data.fastestTime << endl;
	cout << "Line Progress:\n";
	
	int curr_stage = data.stations - 1;
	int next = data.lookup[curr_stage +1][data.best_end][1];
	vector<vector<int>> pathing;
	while (next != -1) {
		vector<int> temp = { data.lookup[curr_stage][next][0], next };
		pathing.push_back(temp);
		next = data.lookup[curr_stage][next][1];
		curr_stage--;
	}
	for (int i = pathing.size() - 1; i >= 0; i--) {
		cout << pathing[i][0] << '(' << pathing[i][1] << ")\n";
	}
	cout << data.fastestTime << '(' << data.best_end << ")\n";
}
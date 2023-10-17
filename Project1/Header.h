#pragma once
#include <vector>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class stations {
public:
	//formatted as stationWeights[route][station]
	vector<vector<int>> stationWeights;

	//formatted as transferWeight[station][from][to]
	vector<vector<vector<int>>> transferWeight;

	//formatted as lookup[station][route][from]
	vector<vector<vector<int>>> lookup;

	vector<vector<int>> pathing;

	int stations;
	int lines;
	int fastestTime = INT_MAX;
	int best_end = -1;
	void create(ifstream& inputFile);
	void createLookup();
private:
	void fillTransAry(ifstream& fin);
	void fillStatAry(ifstream& fin);
};

void stations::create(ifstream& fin) {
	fin >> this->lines >> this->stations;

	//fill stations array
	fillStatAry(fin);

	//fill transfer array
	fillTransAry(fin);

	createLookup();
}

void stations::fillStatAry(ifstream& fin) {
	int new_data;
	for (int i = 0; i < this->lines; i++) {
		vector<int> temp;
		for (int j = 0; j < this->stations; j++) {
			fin >> new_data;
			temp.push_back(new_data);
		}
		this->stationWeights.push_back(temp);
	}
}

void stations::fillTransAry(ifstream& fin) {
	int new_data;
	for (int i = 0; i < this->stations; i++) {
		vector<vector<int>> station_transfer;
		for (int j = 0; j < this->lines; j++) {
			vector<int> single_transfer;
			for (int k = 0; k < this->lines; k++) {
				fin >> new_data;
				single_transfer.push_back(new_data);
			}
			station_transfer.push_back(single_transfer);
		}
		this->transferWeight.push_back(station_transfer);
	}
}

void stations::createLookup() {
	int new_data;
	for (int i = 0; i <= this->stations; i++) {
		vector<vector<int>> temp;
		for (int j = 0; j < this->lines; j++) {
			temp.push_back({ INT_MAX, -1 });
		}
		this->lookup.push_back(temp);
	}
}

ifstream open_file(string fin_name);

void outputData(stations& map);

int findFastest(int stage, int route, stations& map);


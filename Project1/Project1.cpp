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

	findPath(layout);

	outputData();

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

void findPath(stations& map) {

}

void outputData() {

}
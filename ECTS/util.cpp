#include "util.h"

#include <fstream>
#include <iostream>
#include <sstream>

namespace util {

// load data in UCR format to the 2d vector 'data' with corresponding 'labels'
bool readUCRData(const std::string &f,
                 std::vector<std::vector<double> > &data,
                 std::vector<int> &labels) {
    std::ifstream ifs(f);
    if (ifs.fail()) {
        std::cerr << "File \'" << f << "\' could not be opened for reading" << std::endl;
        return false;
    }

    std::string line;
    // double type of labels for compatibility with original files
    double label;
    std::vector<double> row;
    while (ifs >> label) {
        // the first value of each row is the label
        labels.push_back((int)label);
        // the remaining values are the time series
        // std::cout << label << std::endl;
        std::getline(ifs, line);
        // std::cout << line << std::endl;
        std::stringstream ss(line);
        std::string str;
        while (std::getline(ss, str, ',')) {
            if(str == "") continue;
            std::stringstream ss1(str);
            double num;
            ss1 >> num;
            // std::cout << num << " ";
            row.push_back(num);
        }
        // std::cout << std::endl;
        // std::cout<< row.size() <<std::endl;
        // for (std::vector<double>::iterator it = row.begin(); it != row.end(); it++){
		//     std::cout << *it << " ";
        // }
        // std::cout << std::endl;
        data.push_back(row);
        row.clear();
    }
    return true;
}

} // namespace util

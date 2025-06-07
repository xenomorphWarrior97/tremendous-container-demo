/*
Copyright 2025 xenomoprhWarrior97
*/
#include <algorithm>
#include <cctype>
#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>

std::string clean_word(const std::string &my_word) {
  std::string cleaned_word;
  for (char c : my_word) {
    if (std::isalnum(static_cast<unsigned char>(c))) {
      cleaned_word += std::tolower(c);
    }
  }
  return cleaned_word;
}

int main(int argc, char *argv[]) {
  if (argc != 2) {
    std::cerr << "Usage: word-counter <file_path>\n";
    return 0;
  }

  std::ifstream file(argv[1]);
  if (!file) {
    std::cerr << "Error: could not open file" << argv[1] << "\n";
    return 1;
  }

  std::unordered_map<std::string, int> word_count;
  std::string line;
  while (std::getline(file, line)) {
    std::stringstream ss(line);
    std::string word;
    while (ss >> word) {
      word = clean_word(word);
      if (!word.empty()) {
        ++word_count[word];
      }
    }
  }

  std::vector<std::pair<std::string, int>> sorted_words(word_count.begin(),
                                                        word_count.end());
  std::sort(sorted_words.begin(), sorted_words.end(),
            [](const auto &a, const auto &b) { return b.second < a.second; });

  for (const auto &[word, count] : sorted_words) {
    std::cout << word << " : " << count << " occurences.\n";
  }

  return 0;
}
